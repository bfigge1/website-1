---
title: "How We Combined Engineering and Economics"
subtitle: "Estimating the payoff from rooftop solar before anyone decided whether to install it."
summary: "Engineering models can estimate how much a rooftop solar system is worth. Economists can study whether people adopt it. Our project combined both approaches."
authors:
- admin
tags:
- solar
- engineering
- economics
- methods
categories:
- Research
date: "2026-07-29T12:15:00-07:00"
lastmod: "2026-07-29T13:45:00-07:00"
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

4. [Did California's Solar Mandate Increase Solar Adoption?](/post/did-california-solar-mandate-work/)

One of the hardest questions in economics is surprisingly simple:

> *What would have happened if someone had made a different decision?*

Suppose a builder chooses **not** to install rooftop solar on a newly constructed home.

Would installing solar have saved money?

Or was avoiding solar actually the better financial decision?

The problem is that we observe only the choice that was made. We never observe the alternative.

To answer that question, we combined engineering and economics.

## Economics can observe choices—but not necessarily opportunities

Economic data are very good at recording what people do.

We can observe whether a builder installed rooftop solar. We can observe where the building was constructed, when permits were filed, and characteristics of the building itself.

But none of those data tell us something equally important:

> *How profitable would rooftop solar have been for this specific project?*

Without that information, it is difficult to know whether non-adoption reflects a project with poor financial prospects or barriers that prevented an otherwise attractive investment.

Estimating those expected payoffs became the first part of our project.

## Using an engineering model

Rather than building our own engineering model, we used the **System Advisor Model**, or SAM, developed by the U.S. National Renewable Energy Laboratory.

SAM is used by engineers, utilities, consultants, and solar developers to evaluate photovoltaic systems. Given enough information about a building and proposed system, the model estimates electricity production, utility bills, installation and operating costs, financing, incentives, and ultimately the expected **net present value** of installing rooftop solar.

In other words, SAM estimates what a builder or homeowner might expect to gain financially from installing a system.

That made it the ideal starting point.

## But we did not simply run SAM

Many previous engineering studies evaluated only a handful of representative buildings.

Our objective was different.

We wanted to estimate expected private payoffs for **thousands of actual construction projects**. That required assembling a much richer dataset than had previously been used in evaluations of rooftop solar mandates.

For each building project, we combined information from multiple sources:

- municipal building-permit records identifying new residential projects across the San Francisco Bay Area;
- rooftop shading estimates from Google Project Sunroof;
- local weather and solar irradiance from NREL's National Solar Radiation Database;
- hourly electricity-consumption profiles from restricted-access PG&E metering data for nearly 63,000 addresses;
- historical electricity tariffs and net-metering rules;
- changing federal and state incentives; and
- California interconnection records describing installation costs across cities and years.

Together, these datasets allowed us to parameterize the engineering model using characteristics of actual projects rather than hypothetical examples.

{{< figure src="engineering-model.png" caption="**From observed buildings to estimated payoffs.** We combine building permits with rooftop shading, local weather, electricity-use profiles, tariffs, incentives, and installation costs, then use NREL's System Advisor Model to estimate the expected private payoff from rooftop solar for each project." numbered="true" >}}

## Every project receives its own estimate

One detail that often gets overlooked is that rooftop solar systems do not all have the same optimal size.

A building with higher electricity demand benefits from a different system than one with lower demand. Roof size matters. Electricity tariffs matter. Shading matters.

Rather than evaluating one fixed solar system for every project, we optimized system size separately for each building to maximize its expected private payoff, subject to the building's characteristics and rooftop constraints.

That means every project in the dataset receives its own predicted net present value under its own circumstances.

The result is not a single estimate of "the" profitability of rooftop solar. It is a distribution of expected payoffs across thousands of projects.

## Modeling expectations at the time of the decision

The adoption decision occurred when the builder was planning and permitting the project—not years later, when its eventual performance could be observed.

We therefore attempted to parameterize SAM using information that would have been available when each permit was first filed. Historical installation costs, tariffs, net-metering rules, incentives, financing assumptions, and technology characteristics vary by project year.

For electricity demand, our primary model uses city-level mean hourly consumption profiles for recently created PG&E premises. This approach is intended to approximate what a builder could reasonably expect about a future occupant's electricity use. As a robustness check, we also use matched building-level interval data for the subset of projects where those data are available.

This distinction matters. An engineering model can generate a very precise estimate under a given set of inputs, but the decision-maker does not know the future with certainty. Our estimates represent plausible expected payoffs at the time of the decision, not guaranteed realized returns.

## Engineering tells us what appears financially possible

After running the engineering model, we knew something economists rarely observe directly.

For every building, we had an estimate of:

> **What would rooftop solar likely have been worth?**

Under our primary parameterization, expected private payoffs were positive for every project. For single-family homes, they ranged from approximately $2,700 to $17,200, with a median of about $7,900.

Alternative assumptions produced more variation. Higher installation costs, lower electricity consumption, less favorable compensation for exported electricity, or the absence of the federal tax credit reduced estimated payoffs. With project-matched electricity-consumption data, 12 percent of the relevant subsample had negative estimated payoffs, although some of those estimates likely reflected incomplete consumption records or buildings that were not yet occupied.

That heterogeneity is itself an important result.

Earlier engineering studies often concluded that rooftop solar was cost-effective across all representative new-construction cases. Our analysis suggests a more nuanced picture: expected private payoffs were generally positive, but their magnitude—and occasionally their sign—depended on project characteristics and assumptions about future conditions.

## Economics asks a different question

Once we estimated expected payoffs, the project shifted from engineering to economics.

Instead of asking:

> *Would solar appear to pay?*

we could ask:

> *Did builders actually install solar where the expected payoff was highest?*

Those are different questions.

The engineering model estimates the private financial opportunity under specified assumptions. The adoption data reveal behavior.

Comparing the two is what led us to the idea we call the **solar gap**, which I discuss in the next article.

## Why combine disciplines?

Many climate-policy questions require both engineering and economics.

Engineering tells us what technologies are capable of achieving and what they appear likely to cost or save.

Economics helps explain how people respond to those opportunities and whether policies change their behavior.

Neither perspective is sufficient on its own.

A technology can work extremely well and still fail to spread. Likewise, observing slow adoption does not necessarily mean the technology is ineffective or that non-adopters are making mistakes.

Understanding both requires combining the two perspectives—and being clear about what each can and cannot establish.

---

*This post is based on [Solar Adoption by Mandates](/publication/solar_mandates/), joint work with Stefano Carattini, Wade Davis, and Anton Heimerdinger.*

**Previous:** [The Strange Economics of Rooftop Solar](/post/strange-economics-rooftop-solar/)

**Next:** [The Solar Gap](/post/solar-gap/)
