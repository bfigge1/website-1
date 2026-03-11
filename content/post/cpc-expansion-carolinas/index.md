---
title: "How Crisis Pregnancy Centers Spread Across the Carolinas"
subtitle: "Mapping three decades of expansion and what it means for reproductive access"
summary: "Between 1990 and 2019, crisis pregnancy centers in North and South Carolina grew from 62 to over 150. Here's what that expansion looked like, county by county."
authors:
- admin
tags:
- CPC
- reproductive health
- data visualization
categories:
- Research
date: "2026-02-15T00:00:00Z"
lastmod: "2026-02-15T00:00:00Z"
featured: true
draft: false

image:
  caption: "CPC and abortion provider locations across the Carolinas"
  focal_point: ""
  placement: 2
  preview_only: false
---

In 1990, there were 62 crisis pregnancy centers (CPCs) in North and South Carolina. By the late 2010s, that number had grown to over 150. During the same period, the number of abortion providers barely moved, hovering between 18 and 26.

This post walks through the data behind my [job market paper](/publication/figge_jmp/) on CPCs and fertility decisions, starting with the most basic question: where did these centers open, and why does that geography matter?

## What are CPCs?

Crisis pregnancy centers are nonprofit organizations, typically faith-based, that offer free pregnancy testing, counseling, and material support (diapers, baby clothes, parenting classes) to pregnant women. Their stated goal is to provide alternatives to abortion. They do not perform or refer for abortions. There are now more than 2,500 nationwide, outnumbering abortion clinics roughly three to one.

Despite their prevalence, there was essentially no causal evidence on whether CPCs actually affect abortion rates before this paper. That gap is what motivated the research.

## The expansion, decade by decade

Use the slider below to scrub through time, or hit Play to watch CPCs (pink circles) and abortion providers (blue triangles) appear and disappear across North and South Carolina from 1975 to 2020. Click any marker for details.

{{< include-html "leaflet_map.html" >}}

A few patterns stand out.

First, the growth is not uniform. CPCs expanded along the I-85 corridor (Charlotte to Raleigh) and in the western mountains of North Carolina. The coastal plain and rural southern South Carolina saw much less penetration.

Second, abortion providers barely moved. The blue triangles are almost identical across all four maps. They sit in the same handful of metro areas (Charlotte, Raleigh-Durham, Greensboro, Asheville, Greenville, Charleston, Columbia). This means most of the variation in reproductive access over this period is coming from the CPC side, not from changes in clinic supply.

Third, by the late 2010s, CPCs outnumber abortion providers roughly 7 to 1 in these two states. Many counties have a CPC but no abortion provider within their borders.

## Why geography matters for identification

The key challenge in studying CPCs is endogeneity. CPCs don't open randomly. They may target areas where abortion rates are already high, or where local religious communities are mobilizing. A naive regression of abortion rates on CPC presence would conflate the effect of CPCs with whatever drove them to locate there.

My paper addresses this with a simulated instrumental variables strategy. The basic idea: I use the characteristics of a county at a baseline period (before CPC expansion) to predict how many CPCs it would eventually receive, based on the national expansion pattern. This strips out the local demand-side factors that drive both CPC location and abortion rates.

The maps above give visual intuition for why this works. The expansion followed a predictable spatial pattern tied to population density, highway access, and proximity to existing religious infrastructure. Counties that "looked like" CPC targets in 1990 did in fact get more CPCs, and I can use that predicted exposure as an instrument.

I go deeper into the methodology in a [separate post](/post/building-an-instrument/).

## What did all that expansion do?

The headline result: CPC presence reduces county-level abortion rates by about 18 percent. That's a meaningful effect. It implies that CPCs are succeeding at their core mission of redirecting women away from abortion, at least in the aggregate.

But that aggregate number hides important variation by age. I unpack that in [another post](/post/who-cpcs-affect/).

---

*This post is based on my job market paper, "The Role of Crisis Pregnancy Centers in Fertility Decisions." You can read the full paper [here](/publication/figge_jmp/).*
