---
title: "Who Do Crisis Pregnancy Centers Actually Affect?"
subtitle: "The age-specific effects of CPCs on abortion and birth rates"
summary: "CPCs reduce abortion rates most among women in their early 20s, but increase birth rates most among teenagers. The age patterns reveal something about how these centers work."
authors:
- admin
tags:
- CPC
- reproductive health
- data visualization
- causal inference
categories:
- Research
date: "2026-02-20T00:00:00Z"
lastmod: "2026-02-20T00:00:00Z"
featured: true
draft: false

image:
  caption: "CPC effects vary substantially by age group"
  focal_point: ""
  placement: 2
  preview_only: false
---

The headline finding from my [job market paper](/publication/figge_jmp/) is that crisis pregnancy centers reduce abortion rates by about 18 percent. That number comes from a 2SLS estimate using a simulated instrument for CPC exposure, applied to a 30-year county panel from North and South Carolina.

But aggregate effects hide the more interesting story. When I estimate the model separately by age group, the pattern that emerges tells us something about *how* CPCs work, not just *whether* they work.

## The coefficient plot

The figure below shows 2SLS coefficients for two outcomes (log abortion rate and log birth rate) across five age groups. Each age group is estimated in a separate regression using the same simulated CPC instrument.

{{< figure src="age_coefficients.png" caption="**CPC effects by age group.** Blue circles show the effect on log abortion rates. Red triangles show the effect on log birth rates. 95% confidence intervals shown." numbered="true" >}}

Three things jump out.

**Abortion effects are largest for women aged 20-29.** The point estimates for the 20-24 and 25-29 age groups are around -0.17 to -0.18 in log points, roughly a 16-18 percent reduction in the abortion rate. The effect for teenagers (10-19) is smaller at about -0.11, and for women 35-44 it's about -0.08.

**Birth rate effects are positive across all age groups.** CPC presence increases birth rates by 5-10 percent, depending on age. This is the mirror image of the abortion reduction: women who would have obtained abortions are instead carrying pregnancies to term.

**The abortion-birth tradeoff is not one-to-one.** For teenagers, the birth rate effect (about +5%) is large relative to the abortion effect (about -11%). For women 25-34, the birth effect is proportionally larger (+10%) compared to their abortion reduction. This suggests CPCs are not simply substituting abortions for births; they may also be affecting pregnancy incidence or other margins (miscarriage timing, out-of-state travel).

## What explains the age pattern?

The fact that 20-somethings show the largest abortion reductions makes sense for several reasons. Women in their early 20s have the highest baseline abortion rates, so there is more margin to move. They are also the demographic most likely to face an unplanned pregnancy during a period of economic instability (still in school, early career, less likely to have a stable partner). CPC services like free ultrasounds, parenting classes, and material goods may have the highest marginal value for this group.

Teenagers show a smaller abortion effect but a notable birth effect. One interpretation: teens who interact with CPCs may be less likely to travel to obtain an out-of-county abortion (they have fewer resources, less transportation autonomy), so the local presence of a CPC matters more on the birth margin.

Women over 35 show the weakest effects overall. This is consistent with older women having more established preferences and resources, making them less susceptible to CPC counseling at the margin.

## The event study

To check that these effects reflect CPC openings rather than pre-existing trends, the figure below shows an event study. I plot coefficients for years before and after the first CPC opens in a county, separately by age group.

{{< figure src="event_study.png" caption="**Event study for birth rates by age group.** Coefficients are relative to the year before CPC opening (dashed line). County and year fixed effects, population weighted." numbered="true" >}}

The pre-trends are flat for all age groups, which supports the identifying assumption. After CPC entry, birth rates drift upward, with the effect building gradually over several years. This is consistent with the mechanism: CPCs take time to establish community presence and build a client base.

## Why this matters

The age heterogeneity is policy-relevant for two reasons.

First, it tells us CPCs are most effective among economically vulnerable women. This raises questions about long-term outcomes. Are these additional births occurring among women who have the resources to support them? My paper cannot answer that, but the age pattern suggests the answer may often be no.

Second, it constrains the mechanism. CPCs are not simply making abortion harder to access (that would affect all ages roughly equally, conditional on baseline rates). They appear to be changing individual-level decisions through counseling and support services, with effects that vary by how much a woman stands to gain from those services.

---

*For the full identification strategy behind these estimates, see my post on [building the instrument](/post/building-an-instrument/). For context on CPC expansion, see [How Crisis Pregnancy Centers Spread Across the Carolinas](/post/cpc-expansion-carolinas/).*
