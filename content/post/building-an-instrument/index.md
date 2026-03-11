---
title: "How I Built an Instrument for CPC Expansion"
subtitle: "A simulated IV approach validated with Monte Carlo evidence"
summary: "Studying the causal effect of crisis pregnancy centers requires solving an endogeneity problem. Here's how a simulated instrumental variables strategy works, and Monte Carlo evidence that it recovers the true parameter."
authors:
- admin
tags:
- causal inference
- instrumental variables
- econometrics
- Monte Carlo
categories:
- Methods
date: "2026-03-01T00:00:00Z"
lastmod: "2026-03-01T00:00:00Z"
featured: true
draft: false

image:
  caption: "Monte Carlo validation of the simulated IV strategy"
  focal_point: ""
  placement: 2
  preview_only: false
---

The core empirical challenge in studying crisis pregnancy centers is familiar to any applied economist: selection on unobservables. CPCs do not open randomly. They tend to locate in areas with larger populations, more religious institutions, and potentially higher abortion rates. A naive regression of abortion rates on CPC counts would be biased.

This post explains the simulated instrumental variables (IV) strategy I developed for my [job market paper](/publication/figge_jmp/) and shows Monte Carlo evidence that it works.

## The idea

Simulated instruments have a long history in economics, dating back to [Currie and Gruber (1996)](https://doi.org/10.1086/262059) on Medicaid eligibility and used more recently in contexts like [Duggan and Scott Morton (2010)](https://doi.org/10.1257/aer.100.1.590) on prescription drug markets. The core logic is always the same: use a national policy or expansion pattern, applied to local baseline characteristics, to generate predicted exposure that is plausibly exogenous to local shocks.

For CPCs, the approach works as follows.

**Step 1.** I take county characteristics at a baseline year (before the CPC expansion I'm studying): population, religious adherence rates, urbanization, highway proximity, and other predictors of CPC location.

**Step 2.** I estimate the national relationship between these characteristics and CPC openings across all counties in the U.S., excluding the Carolinas.

**Step 3.** I apply these estimated coefficients to Carolinas county characteristics to get a predicted number of CPCs for each county-year. This "simulated" CPC count captures the component of CPC presence driven by predetermined local characteristics interacted with national trends, stripping out local demand shocks that might correlate with abortion rates.

**Step 4.** I use this simulated CPC count as an instrument for actual CPC presence in a 2SLS framework.

The exclusion restriction requires that baseline county characteristics affect abortion rates only through their influence on CPC presence, conditional on county and year fixed effects. The county fixed effects absorb all time-invariant county characteristics, so the instrument is identified off of differential changes in predicted CPC exposure over time across counties with different baseline characteristics.

## Monte Carlo validation

A simulated instrument can fail for several reasons: misspecification of the prediction model, nonlinear confounding, or heterogeneous treatment effects that the instrument does not capture. Rather than asking readers to take the exclusion restriction on faith, I run a Monte Carlo exercise to show the instrument recovers the true parameter under realistic data-generating processes.

I simulate data that mimics the key features of my actual dataset: a county-year panel with endogenous CPC placement, correlated unobservables, and realistic effect sizes. I then estimate the IV model on each simulated dataset and examine the distribution of estimates.

{{< figure src="monte_carlo.png" caption="**Monte Carlo validation.** Kernel density of IV estimates across 100 replications. Dashed line marks the true parameter. Dotted line marks the IV mean. Rows vary the true effect size. Columns vary the data-generating process." numbered="true" >}}

The figure shows results across a 3x3 grid. The rows correspond to three true effect sizes (beta = -0.30, -0.20, -0.10). The columns correspond to three data-generating processes of increasing complexity.

**Correct specification** (left column). The DGP matches the assumptions of the estimation model. The IV estimates are centered near the truth with small bias (+0.037, -0.014, +0.032) and moderate variance. This is the baseline sanity check.

**Nonlinear confounding** (middle column). I introduce a quadratic relationship between the confounder and the outcome, which the linear model cannot capture. The IV still performs well. Bias remains small (-0.003 to +0.011), confirming that the instrument is robust to this form of misspecification.

**Heterogeneous effects by age** (right column). The treatment effect varies across age groups, and the instrument recovers a weighted average. For beta = -0.30 and -0.20, the bias is small (-0.067 and +0.004). For beta = -0.10, it's negligible (+0.009). The variance is somewhat larger, which is expected when the instrument captures an average of heterogeneous effects.

Across all nine cells, the IV bias never exceeds 0.07 in absolute value, and the distributions are reasonably well-centered on the truth. This is not a proof that the instrument works in the real data, but it establishes that the approach is sound under plausible conditions.

## What the Monte Carlo does not do

It doesn't address all threats. If CPCs respond to local abortion demand shocks that are also correlated with changes in birth rates through other channels, the instrument could still be invalid. I address these concerns in the paper with additional robustness checks: pre-trend tests, placebo outcomes, and sensitivity to alternative instrument construction.

The value of the Monte Carlo is narrower. It shows that the *statistical machinery* works. Given a valid exclusion restriction, the estimator recovers the right number. That's a useful thing to know before interpreting the point estimates.

## Why show this?

Most applied papers assert instrument validity with a first-stage F-statistic and a plausibility argument. Monte Carlo validation goes further by demonstrating the estimator's performance under controlled conditions. I think the field would benefit from more of this, particularly for simulated instruments where the prediction step introduces additional degrees of freedom.

If you're building a simulated IV in your own work, I'd recommend a similar exercise. It takes a few hours to code and can reveal problems with your instrument that no amount of hand-waving about the exclusion restriction will catch.

---

*For context on the CPC setting and expansion patterns, see [How Crisis Pregnancy Centers Spread Across the Carolinas](/post/cpc-expansion-carolinas/). For the age-specific results this instrument produces, see [Who Do Crisis Pregnancy Centers Actually Affect?](/post/who-cpcs-affect/)*
