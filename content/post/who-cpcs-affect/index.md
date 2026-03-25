---
title: "Who Do Crisis Pregnancy Centers Actually Affect?"
subtitle: "Age-specific effects and the substitution mechanism"
summary: "CPC abortion reductions are pervasive across all age groups, peaking at ages 25-29. Pregnancy rates do not respond at any age, confirming substitution. A marital decomposition reveals that the births concentrate among married women aged 25-34."
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
  caption: "CPC effects by age group on abortion, birth, and pregnancy rates"
  focal_point: ""
  placement: 2
  preview_only: false
---

The headline finding from my [paper](/publication/figge_jmp/) is that one additional CPC per 10,000 women reduces abortion rates by 13 to 14 percent. That number comes from a 2SLS estimate using a simulated instrument for CPC exposure, applied to a 30-year county panel from North and South Carolina.

But the aggregate number hides the more interesting story. When I decompose the estimates by age group and marital status, the pattern tells us something about *how* CPCs work, not just *whether* they work.

## The age decomposition

The figure below shows 2SLS coefficients for three outcomes (log abortion rate, log birth rate, and log pregnancy rate) across five age groups. Each age group is estimated in a separate regression using the same simulated CPC instrument (first-stage F > 127 in all cases).

{{< figure src="age_coefficients.png" caption="**CPC effects by age group.** Circles show abortion effects, triangles show birth effects, diamonds show pregnancy effects. 95% confidence intervals shown." numbered="true" >}}

Three things stand out.

**Abortion reductions are pervasive across all age groups.** Coefficients range from -0.136 (ages 35-44) to -0.212 (ages 25-29). This is not a story about CPCs affecting one particular demographic. The reductions are negative and significant everywhere.

**Birth effects are positive and significant at ages 25 and older.** The magnitudes are small, which is expected: the birth base rate is roughly five times the abortion rate, so even full one-for-one substitution produces only a modest percentage increase in births.

**Pregnancy rates do not respond at any age.** All five pregnancy coefficients are statistically indistinguishable from zero. This is the key mechanistic finding. Under deterrence, where CPCs prevent pregnancies through upstream behavioral change, pregnancy rates should fall. They do not. The data are consistent with substitution at every age: CPCs change how pregnancies are resolved, not whether they occur.

## The marital decomposition

An exploratory marital decomposition reveals where the substituting births land. Abortion reductions are pervasive among unmarried women across all adult ages, while the corresponding birth increases concentrate among married women aged 25 to 34. The substitution ratio at ages 25 to 29 is consistent with one-for-one replacement (ratio = 0.93, with the 95% confidence interval including unity).

The demographic mismatch between where abortions fall (unmarried women broadly) and where births rise (married women at prime childbearing ages) is suggestive but hard to pin down with county-level data. It could reflect within-woman reclassification (women who marry because they carry to term), cross-demographic spillovers (community norms shifting), or simply that married women in this age range are the group where an additional pregnancy is most likely to result in a live birth rather than another outcome. The county-level data cannot distinguish these channels.

## The event study

Event study estimates around first CPC opening show flat pre-trends for abortion, birth, and pregnancy rates. Joint F-tests fail to reject the null of zero pre-trends (p = 0.359 for abortion, p = 0.547 for birth, p = 0.446 for pregnancy). The flat pregnancy pre-trends are particularly useful for the mechanism analysis: they confirm that treated and control counties were on parallel pregnancy trajectories before CPC entry, strengthening the interpretation of the post-treatment pregnancy null as a causal zero.

{{< figure src="event_study.png" caption="**Event study around first CPC opening.** Coefficients relative to the year before CPC opening. County and year fixed effects, population weighted." numbered="true" >}}

## Why this matters

The mechanism evidence has direct policy implications. Because CPCs work through substitution rather than deterrence, the relevant welfare question is about the marginal woman redirected from abortion to birth, not about averted pregnancies. The marital decomposition suggests the substituting births concentrate among married women at prime childbearing ages, a group for whom carrying to term is plausibly close to desired fertility timing. But unmarried teenagers also show a clean substitution cell, and for that group the welfare calculus is less favorable.

States have substantially increased CPC funding since *Dobbs*. The mechanism evidence implies that this funding generates additional births whose welfare consequences depend on wantedness, something the data cannot measure.

---

*For the full identification strategy behind these estimates, see my post on [building the instrument](/post/building-an-instrument/). For context on CPC expansion, see [How Crisis Pregnancy Centers Spread Across the Carolinas](/post/cpc-expansion-carolinas/).*
