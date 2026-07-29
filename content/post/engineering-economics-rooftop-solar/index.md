---
title: "How We Combined Engineering and Economics"
subtitle: "Using NREL’s System Advisor Model, administrative data, and causal inference to study rooftop solar."
summary: "Using NREL’s System Advisor Model, administrative data, and causal inference to study rooftop solar."
authors:
- admin
tags:
- solar
- climate policy
- California
categories:
- Research
date: "2026-07-29T12:15:00-07:00"
lastmod: "2026-07-29T12:15:00-07:00"
featured: true
draft: false

image:
  caption: "Engineering estimates of rooftop solar payoffs"
  focal_point: ""
  placement: 2
  preview_only: true
---

---



**California solar mandate series**

1. [The Strange Economics of Rooftop Solar](/post/strange-economics-rooftop-solar/)

2. **How We Combined Engineering and Economics** *(current)*

3. [The Solar Gap](/post/solar-gap/)

4. [Did California’s Solar Mandate Work?](/post/did-california-solar-mandate-work/)

5. [Why Climate Policy Is About Adoption](/post/climate-policy-is-about-adoption/)

Economic data usually show what people chose. They rarely show what would have happened had they made a different choice.

That limitation is especially important for rooftop solar. Observing that one builder installed solar and another did not tells us little unless we know whether the investment made financial sense for each project. A house in sunny Fairfield differs from one in foggier San Francisco. Roof area, shading, electricity consumption, utility rates, installation costs, financing, and tax incentives all affect the return.

To study adoption, we first needed to model the technology.

## Building a project-level engineering model

We used the National Renewable Energy Laboratory's open-source [System Advisor Model](https://sam.nrel.gov/), or SAM. The model estimates electricity production and financial performance for renewable-energy projects. We parameterized it for thousands of actual new-construction projects in the San Francisco Bay Area.

The inputs came from several sources:

- municipal building permits identifying new residential projects;
- fine-scale solar irradiance and weather data;
- rooftop area and shading estimates from Google Project Sunroof;
- California interconnection records for system costs;
- utility tariffs, net-metering rules, and federal incentives; and
- hourly electricity-consumption profiles, including restricted-access data for newly built premises.

For each project, we allowed the model to choose the solar system size that maximized estimated private payoff, subject to rooftop constraints. The resulting net present value represented discounted electricity-bill savings and incentives minus installation, financing, replacement, and operating costs.

## Why project-level variation matters

Policy cost-effectiveness studies often evaluate a handful of stylized buildings. That is useful for rulemaking, but it can hide substantial variation. In our data, identical policy rules produced different estimated returns across locations and building types.

Sunlight matters, but so do electricity consumption and the timing of that consumption. Under time-of-use rates, a kilowatt-hour generated at one hour can be worth more than a kilowatt-hour generated at another. Larger multifamily buildings can offset consumption across multiple units, while roof area limits the system size. Installation costs also vary across cities and years.

By running the engineering model separately for observed projects, we could estimate a distribution of payoffs rather than one representative number.

## Connecting modeled payoffs to actual behavior

The engineering model gave us a counterfactual for each building: what rooftop solar was expected to be worth. Building-permit records then showed whether the builder actually installed it.

This allowed us to compare two concepts that are often conflated:

1. **Economic potential:** where rooftop solar appears privately cost-effective.
2. **Observed adoption:** where builders actually install rooftop solar.

That comparison revealed the solar gap. Projects with higher estimated returns were not consistently more likely to adopt. Builders passed on solar throughout the payoff distribution, including among projects with some of the largest modeled returns.

## Estimating the effects of mandates

The second part of the paper evaluated San Francisco's 2017 mandate and California's 2020 statewide mandate. A simple before-and-after comparison would be misleading because solar adoption was already evolving and many other factors changed over time.

We therefore used synthetic control methods. For San Francisco, a weighted combination of other Bay Area cities reproduced the city's pre-policy adoption pattern. The main synthetic San Francisco was composed of Oakland and San Jose. After the mandate, actual San Francisco diverged sharply from that counterfactual.

For the statewide analysis, we constructed a synthetic California from other jurisdictions and measured photovoltaic capacity per new residential building permit. We also tested alternative specifications, including synthetic difference-in-differences.

The methods complement one another. Engineering tells us where solar appears worthwhile. Administrative data tell us what builders did. Causal inference estimates what the mandates changed. Together, they answer a richer question than any one discipline could answer alone.

## Open tools, public evidence

One reason I value this design is that its core engineering tool is publicly available. SAM can be inspected, rerun, and challenged. The building, climate, tariff, and policy inputs make assumptions visible rather than burying the result inside a proprietary risk or analytics platform.

That transparency does not make the estimates unquestionable. It makes disagreement productive: readers can ask whether financing costs are too low, whether future tariffs are uncertain, or whether administrative costs are missing, and then see how the answer changes.

---



*This post is based on [Solar Adoption by Mandates](/publication/solar_mandates/). Read the [paper](/publication/solar_mandates/Carattini_Davis_Figge_and_Heimerdinger_2025.pdf).*

**Previous:** [The Strange Economics of Rooftop Solar](/post/strange-economics-rooftop-solar/)

**Next:** [The Solar Gap](/post/solar-gap/)
