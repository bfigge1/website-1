"""
Generate placeholder featured images for blog posts.
Run this once to create featured.png files for each post.
Replace these with your actual figures once you export them from Stata/R.

Usage: python scripts/generate_featured_images.py
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Paths
POST_DIR = Path("content/post")

# Color palette (matches the paper's style)
DARK_GREEN = "#1a5c2a"
MED_GREEN = "#4a9c5a"
LIGHT_GREEN = "#8fcb8f"
PALE_GREEN = "#d4ecd4"
CPC_PINK = "#c07070"
PROVIDER_BLUE = "#2b4c7e"
BG_COLOR = "#fafafa"

def make_expansion_featured():
    """Featured image for the CPC expansion post: stylized map growth graphic."""
    fig, axes = plt.subplots(1, 4, figsize=(16, 4.5), facecolor=BG_COLOR)

    periods = ["Early 1990s", "Early 2000s", "Early 2010s", "Late 2010s"]
    cpc_counts = [62, 143, 113, 154]
    provider_counts = [18, 26, 25, 21]

    for ax, period, cpcs, provs in zip(axes, periods, cpc_counts, provider_counts):
        ax.set_facecolor(BG_COLOR)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.axis('off')

        # Draw state outline (simplified)
        state_x = [1, 9, 9.5, 8, 5, 1.5, 1]
        state_y = [7, 8, 5, 2, 1.5, 3, 7]
        ax.fill(state_x, state_y, color=MED_GREEN, alpha=0.3)
        ax.plot(state_x, state_y, color=DARK_GREEN, linewidth=2)

        # Scatter CPCs
        np.random.seed(42)
        n_dots = min(cpcs // 4, 40)
        cx = np.random.uniform(2, 8.5, n_dots)
        cy = np.random.uniform(2.5, 7, n_dots)
        ax.scatter(cx, cy, c=CPC_PINK, s=30, alpha=0.7, zorder=3, edgecolors='white', linewidths=0.5)

        # Scatter providers
        n_prov = min(provs // 3, 8)
        px = np.random.uniform(3, 7, n_prov)
        py = np.random.uniform(3, 6.5, n_prov)
        ax.scatter(px, py, c=PROVIDER_BLUE, s=60, marker='^', zorder=4, edgecolors='white', linewidths=0.5)

        ax.set_title(f"{period}\n{cpcs} CPCs | {provs} Providers",
                     fontsize=11, fontweight='bold', color='#333')

    fig.suptitle("Crisis Pregnancy Center Expansion in the Carolinas",
                 fontsize=16, fontweight='bold', y=1.02, color='#222')
    plt.tight_layout()
    fig.savefig(POST_DIR / "cpc-expansion-carolinas" / "featured.png",
                dpi=150, bbox_inches='tight', facecolor=BG_COLOR)
    plt.close()
    print("Created: cpc-expansion-carolinas/featured.png")


def make_age_effects_featured():
    """Featured image for the age heterogeneity post: coefficient plot."""
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    age_groups = ["10-19", "20-24", "25-29", "30-34", "35-44"]
    x = np.arange(len(age_groups))

    # Approximate values from the user's figure
    abort_coef = [-0.11, -0.18, -0.17, -0.12, -0.08]
    abort_ci = [0.08, 0.09, 0.10, 0.09, 0.10]
    birth_coef = [0.05, 0.04, 0.10, 0.10, 0.10]
    birth_ci = [0.06, 0.05, 0.04, 0.05, 0.04]

    width = 0.3
    ax.errorbar(x - width/2, abort_coef, yerr=[abort_ci, abort_ci],
                fmt='o', color=PROVIDER_BLUE, markersize=10, capsize=4,
                capthick=2, linewidth=2, label='Log abortion rate')
    ax.errorbar(x + width/2, birth_coef, yerr=[birth_ci, birth_ci],
                fmt='^', color='#8b2323', markersize=10, capsize=4,
                capthick=2, linewidth=2, label='Log birth rate')

    ax.axhline(y=0, color='#999', linewidth=1, linestyle='-')
    ax.set_xticks(x)
    ax.set_xticklabels(age_groups, fontsize=12)
    ax.set_xlabel("Age Group", fontsize=13)
    ax.set_ylabel("2SLS Coefficient (log outcome)", fontsize=13)
    ax.set_title("CPC Effects by Age Group", fontsize=16, fontweight='bold', color='#222')
    ax.legend(fontsize=11, framealpha=0.9)
    ax.set_ylim(-0.32, 0.22)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    fig.savefig(POST_DIR / "who-cpcs-affect" / "featured.png",
                dpi=150, bbox_inches='tight', facecolor=BG_COLOR)
    plt.close()
    print("Created: who-cpcs-affect/featured.png")


def make_monte_carlo_featured():
    """Featured image for the IV methodology post: kernel density grid."""
    fig, axes = plt.subplots(3, 3, figsize=(14, 10), facecolor=BG_COLOR)

    betas = [-0.30, -0.20, -0.10]
    specs = ["Correct spec", "Nonlinear\nconfounding", "Heterogeneous\neffects (age)"]
    biases = [
        [0.037, 0.003, -0.067],
        [-0.014, -0.023, 0.004],
        [0.032, 0.011, 0.009]
    ]
    sds = [
        [0.226, 0.192, 0.221],
        [0.194, 0.180, 0.253],
        [0.182, 0.183, 0.189]
    ]

    for i, beta in enumerate(betas):
        for j, spec in enumerate(specs):
            ax = axes[i, j]
            ax.set_facecolor('#f0f4f8')

            mean_est = beta + biases[i][j]
            sd = sds[i][j]
            x = np.linspace(beta - 4*sd, beta + 4*sd, 200)
            # Slight left skew to match the actual figures
            from scipy.stats import skewnorm
            y = skewnorm.pdf(x, -2, loc=mean_est + 0.03, scale=sd * 0.85)

            ax.fill_between(x, y, alpha=0.3, color='#6699cc')
            ax.plot(x, y, color='#336699', linewidth=2)
            ax.axvline(beta, color='#333', linewidth=1.5, linestyle='--', label=f'True beta')
            ax.axvline(mean_est, color='#666', linewidth=1, linestyle=':', label='IV mean')

            ax.text(0.95, 0.95, f"IV bias: {biases[i][j]:+.3f}\nIV SD: {sds[i][j]:.3f}",
                   transform=ax.transAxes, ha='right', va='top', fontsize=9,
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

            ax.set_yticks([])
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_visible(False)

            if i == 0:
                ax.set_title(spec, fontsize=12, fontweight='bold')
            if j == 0:
                ax.set_ylabel(f"beta = {beta}", fontsize=12, fontweight='bold')
            if i == 2:
                ax.set_xlabel("IV Coefficient", fontsize=10)

    fig.suptitle("Monte Carlo IV Validation", fontsize=18, fontweight='bold', y=1.01, color='#222')
    plt.tight_layout()
    fig.savefig(POST_DIR / "building-an-instrument" / "featured.png",
                dpi=150, bbox_inches='tight', facecolor=BG_COLOR)
    plt.close()
    print("Created: building-an-instrument/featured.png")


if __name__ == "__main__":
    try:
        from scipy.stats import skewnorm
    except ImportError:
        import subprocess
        subprocess.check_call(["pip", "install", "scipy", "--break-system-packages", "-q"])
        from scipy.stats import skewnorm

    make_expansion_featured()
    make_age_effects_featured()
    make_monte_carlo_featured()
    print("\nDone! Featured images created for all three posts.")
    print("\nNEXT STEPS:")
    print("1. Replace placeholder maps with your actual Stata/R map exports:")
    print("   - content/post/cpc-expansion-carolinas/map_1990s.png")
    print("   - content/post/cpc-expansion-carolinas/map_2000s.png")
    print("   - content/post/cpc-expansion-carolinas/map_2010s.png")
    print("   - content/post/cpc-expansion-carolinas/map_late2010s.png")
    print("2. Replace placeholder figures with your actual exports:")
    print("   - content/post/who-cpcs-affect/age_coefficients.png")
    print("   - content/post/who-cpcs-affect/event_study.png")
    print("   - content/post/building-an-instrument/monte_carlo.png")
    print("3. Or, update the featured images too if you prefer your Stata versions.")
