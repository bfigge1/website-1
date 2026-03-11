# ==============================================================================
# Export figures from CPC paper for blog posts
# ==============================================================================
#
# This script exports your existing Stata/R figures as web-ready PNGs.
#
# OPTION A: If you have the raw figures as PDF/EPS from Stata, just convert them:
#   - Place your exported PDFs in scripts/raw_figures/
#   - Run the conversion section below
#
# OPTION B: If you want to regenerate from data, adapt the ggplot sections.
#
# Output locations:
#   content/post/cpc-expansion-carolinas/map_1990s.png  (etc.)
#   content/post/who-cpcs-affect/age_coefficients.png
#   content/post/who-cpcs-affect/event_study.png
#   content/post/building-an-instrument/monte_carlo.png
# ==============================================================================

library(ggplot2)
library(dplyr)

# Set this to your website repo root
SITE_ROOT <- "/Users/lepus/Documents/GitHub/website-1"

# --- OPTION A: Convert existing PDFs to PNGs using magick ---
# install.packages("magick")
# library(magick)
#
# Convert your 4 map figures:
# for (f in c("map_1990s", "map_2000s", "map_2010s", "map_late2010s")) {
#   img <- image_read_pdf(file.path(SITE_ROOT, "scripts/raw_figures", paste0(f, ".pdf")), density = 200)
#   image_write(img, file.path(SITE_ROOT, "content/post/cpc-expansion-carolinas", paste0(f, ".png")))
# }
#
# Convert coefficient plot:
# img <- image_read_pdf(file.path(SITE_ROOT, "scripts/raw_figures/age_coefficients.pdf"), density = 200)
# image_write(img, file.path(SITE_ROOT, "content/post/who-cpcs-affect/age_coefficients.png"))
#
# Convert event study:
# img <- image_read_pdf(file.path(SITE_ROOT, "scripts/raw_figures/event_study.pdf"), density = 200)
# image_write(img, file.path(SITE_ROOT, "content/post/who-cpcs-affect/event_study.png"))
#
# Convert Monte Carlo:
# img <- image_read_pdf(file.path(SITE_ROOT, "scripts/raw_figures/monte_carlo.pdf"), density = 200)
# image_write(img, file.path(SITE_ROOT, "content/post/building-an-instrument/monte_carlo.png"))


# --- OPTION B: Regenerate coefficient plot in ggplot2 (NYT-style) ---

# Theme inspired by NYT graphics
theme_nyt <- function() {
  theme_minimal(base_size = 14, base_family = "Helvetica") +
    theme(
      plot.title = element_text(face = "bold", size = 18, margin = margin(b = 10)),
      plot.subtitle = element_text(color = "#666666", size = 13, margin = margin(b = 20)),
      plot.caption = element_text(color = "#999999", size = 10, hjust = 0),
      panel.grid.major.x = element_blank(),
      panel.grid.minor = element_blank(),
      panel.grid.major.y = element_line(color = "#e0e0e0"),
      axis.title = element_text(size = 12, color = "#333333"),
      axis.text = element_text(size = 11, color = "#555555"),
      legend.position = "bottom",
      legend.text = element_text(size = 11),
      plot.margin = margin(20, 20, 20, 20),
      plot.background = element_rect(fill = "#fafafa", color = NA),
      panel.background = element_rect(fill = "#fafafa", color = NA)
    )
}

# --- Coefficient plot by age group ---
# Replace these with your actual estimates and SEs

coef_data <- tribble(
  ~age_group, ~outcome,    ~estimate, ~ci_lower, ~ci_upper,
  "10-19",    "Abortion",  -0.11,     -0.19,     -0.03,
  "10-19",    "Birth",      0.05,     -0.01,      0.11,
  "20-24",    "Abortion",  -0.18,     -0.27,     -0.09,
  "20-24",    "Birth",      0.04,     -0.01,      0.09,
  "25-29",    "Abortion",  -0.17,     -0.27,     -0.07,
  "25-29",    "Birth",      0.10,      0.06,      0.14,
  "30-34",    "Abortion",  -0.12,     -0.21,     -0.03,
  "30-34",    "Birth",      0.10,      0.05,      0.15,
  "35-44",    "Abortion",  -0.08,     -0.18,      0.02,
  "35-44",    "Birth",      0.10,      0.06,      0.14
)

coef_data$age_group <- factor(coef_data$age_group,
                               levels = c("10-19", "20-24", "25-29", "30-34", "35-44"))

p_coef <- ggplot(coef_data, aes(x = age_group, y = estimate, color = outcome, shape = outcome)) +
  geom_hline(yintercept = 0, color = "#999999", linewidth = 0.5) +
  geom_pointrange(aes(ymin = ci_lower, ymax = ci_upper),
                  position = position_dodge(width = 0.4),
                  size = 0.8, linewidth = 0.8) +
  scale_color_manual(values = c("Abortion" = "#2b4c7e", "Birth" = "#8b2323")) +
  scale_shape_manual(values = c("Abortion" = 16, "Birth" = 17)) +
  labs(
    title = "Crisis Pregnancy Centers Reduce Abortions,\nIncrease Births Across All Age Groups",
    subtitle = "2SLS estimates using simulated CPC instrument. Each age group estimated separately.",
    x = "Age Group",
    y = "Effect on log rate",
    color = NULL,
    shape = NULL,
    caption = "Source: Figge (2025). 95% confidence intervals shown.\nCounty-year panel, North and South Carolina, 1990-2019."
  ) +
  theme_nyt() +
  coord_cartesian(ylim = c(-0.32, 0.20))

ggsave(file.path(SITE_ROOT, "content/post/who-cpcs-affect/age_coefficients.png"), p_coef,
       width = 10, height = 7, dpi = 200, bg = "#fafafa")

cat("Saved: content/post/who-cpcs-affect/age_coefficients.png\n")

# --- PLACEHOLDER: Event study ---
# Adapt from your Stata event study code. Key elements:
# - x-axis: years relative to first CPC opening
# - y-axis: coefficient
# - separate lines/colors for each age group
# - dashed vertical line at t=-1
# - pre-period coefficients should be near zero (your parallel trends check)

cat("\nREMAINING MANUAL STEPS:\n")
cat("1. Export your 4 map PDFs from Stata and convert using Option A above\n")
cat("2. Export your event study figure\n")
cat("3. Export your Monte Carlo figure\n")
cat("4. Place all PNGs in the paths listed at the top of this script\n")
