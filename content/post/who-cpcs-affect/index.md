---
title: "Who Do Crisis Pregnancy Centers Actually Affect?"
subtitle: "Age-specific effects and the substitution mechanism"
summary: "CPC abortion reductions are pervasive across all age groups, peaking at ages 25-29. Pregnancy rates do not respond at any age, confirming substitution. Welfare concerns concentrate among teenagers, whose marginal births carry higher low-birth-weight rates."
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

The headline finding from my [paper](/publication/figge_jmp/) is that one additional CPC per 10,000 women reduces abortion rates by 7 to 14 percent, depending on the estimator, with the 2SLS specification at the top of that range. That number comes from a simulated instrument for CPC exposure, applied to a 30-year county panel from North and South Carolina.

But the aggregate number hides the more interesting story. When I decompose the estimates by age group and marital status, the pattern tells us something about *how* CPCs work, not just *whether* they work.

## The age decomposition

The figure below shows 2SLS coefficients for three outcomes (log abortion rate, log birth rate, and log pregnancy rate) across five age groups. Each age group is estimated in a separate regression using the same simulated CPC instrument (first-stage F > 193 in all cases).

{{< figure src="age_coefficients.png" caption="**CPC effects by age group.** Circles show abortion effects, triangles show birth effects, diamonds show pregnancy effects. 95% confidence intervals shown." numbered="true" >}}

Three things stand out.

**Abortion reductions are pervasive across all age groups.** Coefficients range from -0.130 (ages 35-44) to -0.197 (ages 25-29). This is not a story about CPCs affecting one particular demographic. The reductions are negative and significant everywhere, and a joint test cannot distinguish them.

**Birth effects are positive and significant at ages 25 and older.** In the log-rate specification the birth coefficient is null at younger ages and turns positive and significant from age 25 up (0.032 at 25-29, 0.040 at 30-34, 0.050 at 35-44). The magnitudes are small, which is expected: the birth base rate is roughly five times the abortion rate, so even full one-for-one substitution produces only a modest percentage increase in births.

**Pregnancy rates do not respond at any age.** All five pregnancy coefficients are statistically indistinguishable from zero. This is the key mechanistic finding. Under deterrence, where CPCs prevent pregnancies through upstream behavioral change, pregnancy rates should fall. They do not. The data are consistent with substitution at every age: CPCs change how pregnancies are resolved, not whether they occur.

## Where the substitution shows up

At ages 25 and older the substitution is clean. Birth coefficients are positive and significant at every age above 25, and the implied substitution ratios bracket unity, so averted abortions reappear as roughly one offsetting birth each. This is the strongest substitution evidence of any age group.

The natural next question is which women carry to term, and here the county-level data turn slippery. It is tempting to read a marital decomposition at ages 25 to 34 as births concentrating among married women, but that reading does not hold up. The married share of women aged 10 to 44 fell from 0.59 in 1990 to 0.35 in 2019, part of the broader decline in shotgun marriage, and the decomposition is sensitive to how you weight for that shift. An unweighted split suggests marriage-during-pregnancy, but a specification that fixes the marital share at its 1990 baseline reverses the result, with birth coefficients positive for both married and unmarried cells at 25 to 34. The marital split at these ages is not interpretable as behavioral redirection.

For teenagers the picture is different and cleaner. The log-rate regression is underpowered at this age because teen birth and abortion rates fell so steeply over the panel, but the count-level instrument shows a clear effect: about 44 additional teen births per unit of CPC exposure, significant at the 1 percent level. A Poisson marital decomposition localizes the offsetting births among unmarried teens (abortion -0.117, birth +0.170). At ages 20 to 24 the channel is genuinely ambiguous; the data reject full one-for-one substitution but cannot rule out zero, bounding the substitution share at 0.60.

## The event study

Event study estimates around first CPC opening show flat pre-trends for abortion, birth, and pregnancy rates. Joint F-tests fail to reject the null of zero pre-trends (p = 0.359 for abortion, p = 0.547 for birth, p = 0.446 for pregnancy). The flat pregnancy pre-trends are particularly useful for the mechanism analysis: they confirm that treated and control counties were on parallel pregnancy trajectories before CPC entry, strengthening the interpretation of the post-treatment pregnancy null as a causal zero.

{{< figure src="event_study.png" caption="**Event study around first CPC opening.** Coefficients relative to the year before CPC opening. County and year fixed effects, population weighted." numbered="true" >}}

## Why this matters

The mechanism evidence has direct policy implications. Because CPCs work through substitution rather than deterrence, the relevant welfare question is about the marginal woman redirected from abortion to birth, not about averted pregnancies. And the answer depends a lot on which woman.

Teenagers are where the welfare concern concentrates, and three pieces of evidence point that way. Substitution operates for teens, shown by the count-level and Poisson results above. The marginal teen births are worse than average: a Wald decomposition of the teen low-birth-weight effect implies a marginal LBW rate of 12.7 percent against a baseline of 9.5 percent, with both pieces significant at the 1 percent level. And the downstream stakes are higher for teen mothers, who complete high school at lower rates with well-documented economic costs. Teens are the only age group where both the substitution and the worse marginal birth quality are individually significant.

The dollar accounting reinforces the point. Public funding works out to about $1,031 per averted abortion at the 2SLS estimate. The private welfare cost per redirected birth, from a structural calibration anchored to the Turnaway Study, runs $418 to $2,554, smaller than headline figures because it prices only the marginal woman near indifference. Across scenarios and estimators the marginal excess burden of public CPC spending ranges from 0.20 to 2.48, straddling break-even.

States have substantially increased CPC funding since *Dobbs*. The mechanism evidence implies that this funding generates additional births whose welfare consequences fall hardest on teens, the group least equipped to absorb them.

---

*For the full identification strategy behind these estimates, see my post on [building the instrument](/post/building-an-instrument/). For context on CPC expansion, see [How Crisis Pregnancy Centers Spread Across the Carolinas](/post/cpc-expansion-carolinas/).*
