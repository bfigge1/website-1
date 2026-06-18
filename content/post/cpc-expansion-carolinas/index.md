---
title: "How Crisis Pregnancy Centers Spread Across the Carolinas"
subtitle: "Mapping three decades of expansion and what it means for reproductive access"
summary: "Between 1990 and 2019, crisis pregnancy centers in North and South Carolina grew from roughly 60 to 146, while the number of abortion providers held flat around 35. Here's what that expansion looked like, county by county."
authors:
- admin
tags:
- CPC
- reproductive health
- data visualization
categories:
- Research
date: "2026-03-10T00:00:00Z"
lastmod: "2026-03-10T00:00:00Z"
featured: true
draft: false

image:
  caption: "CPC and abortion provider locations across the Carolinas"
  focal_point: ""
  placement: 2
  preview_only: true
---

{{< include-html "leaflet_map.html" >}}

In 1990, there were roughly 60 crisis pregnancy centers (CPCs) in North and South Carolina. By 2019, that number had grown to 146. The number of abortion providers held flat over the same period, 36 in 1990 and 35 in 2019, though with substantial churn within each state as clinics opened and closed.

This post walks through the data behind my [job market paper](/publication/figge_jmp/) on CPCs and fertility decisions, starting with the most basic question: where did these centers open, and why does that geography matter?

## What are CPCs?

Crisis pregnancy centers are nonprofit organizations, typically faith-based, that offer free pregnancy testing, counseling, and material support (diapers, baby clothes, parenting classes) to pregnant women. Their stated goal is to provide alternatives to abortion. They do not perform or refer for abortions. There are now more than 2,500 nationwide, outnumbering abortion clinics roughly three to one.

Despite their prevalence, there was essentially no causal evidence on whether CPCs actually affect abortion rates before this paper. That gap is what motivated the research.

## The expansion, decade by decade

Use the slider below to scrub through time, or hit Play to watch CPCs (pink circles) and abortion providers (blue triangles) appear and disappear across North and South Carolina from 1975 to 2020. Click any marker for details.

A few patterns stand out.

First, the growth is not uniform. CPCs expanded along the I-85 corridor (Charlotte to Raleigh) and in the western mountains of North Carolina. The coastal plain and rural southern South Carolina saw much less penetration.

Second, the abortion provider total stayed flat even though individual clinics came and went. The blue triangles cluster in the same handful of metro areas across all four maps (Charlotte, Raleigh-Durham, Greensboro, Asheville, Greenville, Charleston, Columbia), but there is churn underneath the stable count as providers open and close. Net, the count barely moved, so most of the variation in reproductive access over this period comes from the CPC side, not from changes in clinic supply.

Third, by the late 2010s, CPCs outnumber abortion providers roughly 4 to 1 across the two states, and about 6 to 1 in North Carolina alone, well above the national ratio of 3.4 to 1. Many counties have a CPC but no abortion provider within their borders.

## Why geography matters for identification

The key challenge in studying CPCs is endogeneity. CPCs don't open randomly. They may target areas where abortion rates are already high, or where local religious communities are mobilizing. A naive regression of abortion rates on CPC presence would conflate the effect of CPCs with whatever drove them to locate there.

My paper addresses this with a simulated instrumental variables strategy. I estimate a discrete-time hazard model of CPC entry from predetermined county characteristics, then forward-simulate 1,000 counterfactual expansion paths. Averaging across draws yields a predicted CPC count that converges to the conditional expectation of CPC presence given observable county history. The identifying assumption is predetermination: conditional on rich historical observables and two-way fixed effects, the residual timing of CPC openings is orthogonal to contemporaneous fertility shocks.

The maps above give visual intuition for why the instrument has power. The expansion followed a predictable spatial pattern tied to population density, existing CPC stock, distance to the nearest center, and proximity to evangelical institutional infrastructure. The hazard model captures this path-dependent process, and the forward simulation compounds it over 30 years into cross-county variation that no linear function of the same covariates can replicate (first-stage F = 196).

I go deeper into the methodology in a [separate post](/post/building-an-instrument/).

## What did all that expansion do?

The headline result: one additional CPC per 10,000 women reduces abortion rates by 7 to 14 percent, depending on the estimator, with the 2SLS specification at the top of that range (14 percent). Over the sample period this implies roughly 480 to 970 averted abortions per year across the two states. Pregnancy rates do not respond to CPC presence, ruling out deterrence (upstream behavioral change that prevents pregnancies) as the primary channel. The accounting is consistent with substitution: CPCs change how pregnancies are resolved, not whether they occur.

But the aggregate number hides important variation by age and marital status. I unpack that in [another post](/post/who-cpcs-affect/).

---

*This post is based on my job market paper, "The Role of Crisis Pregnancy Centers in Fertility Decisions." You can read the full paper [here](/publication/figge_jmp/).*
