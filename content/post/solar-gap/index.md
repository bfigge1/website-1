---
title: "The Solar Gap"
subtitle: "When estimated profitability only weakly predicts adoption."
summary: "Our analysis suggests that expected private payoffs explain surprisingly little of the variation in rooftop solar adoption."
authors:
- admin
tags:
- solar
- climate policy
- behavioral economics
categories:
- Research
date: "2026-07-29T12:20:00-07:00"
lastmod: "2026-07-29T13:45:00-07:00"
featured: true
draft: false

image:
  caption: "Estimated solar payoffs and observed adoption"
  focal_point: ""
  placement: 2
  preview_only: true
---

---

**California solar mandate series**

1. [The Strange Economics of Rooftop Solar](/post/strange-economics-rooftop-solar/)

2. [How We Combined Engineering and Economics](/post/engineering-economics-rooftop-solar/)

3. **The Solar Gap** *(current)*

4. [Did California's Solar Mandate Increase Solar Adoption?](/post/did-california-solar-mandate-work/)

If you ask a simple question—

> **Should a profitable investment be adopted?**

—the obvious answer is usually yes.

Not because people are assumed to be perfect, but because expected profitability should generally make adoption **more likely**, even when other considerations matter.

Our study asked whether that relationship holds for rooftop solar on newly constructed homes.

The answer was:

**Only weakly.**

That finding became one of the central results of the paper.

## Measuring expected profitability

In the previous article, I described how we estimated the expected private payoff from rooftop solar for thousands of new-construction projects using NREL's System Advisor Model.

Each building received an estimated net present value based on local weather, rooftop characteristics, electricity prices, expected electricity consumption, financing, incentives, installation costs, and other project characteristics.

The result was an estimate of what rooftop solar was expected to be worth financially for each individual project.

The next step was straightforward.

We compared those estimated payoffs with what builders actually did.

## What would we expect to see?

Imagine ordering every building from least profitable to most profitable.

If expected profitability strongly determined adoption, we would expect a simple pattern.

The least profitable projects would rarely install solar.

The most profitable projects would install it much more frequently.

Reality looked different.

{{< figure src="solar-gap-web.svg" caption="**Estimated payoffs and observed adoption.** Green distributions show projects that installed solar; blue distributions show those that did not. The lowest-payoff projects are less likely to adopt, but across most of the distribution adopter and non-adopter payoffs overlap substantially." numbered="true" >}}

The projects with the very lowest estimated payoffs were indeed less likely to install solar.

Beyond that lower tail, however, builders chose **not** to install solar across the full range of positive estimated payoffs.

Some projects with relatively modest estimated returns adopted solar. Others with substantially higher estimated returns did not.

The relationship between expected profitability and adoption existed, but it was much weaker than a simple investment model would predict.

## Quantifying the relationship

Visual patterns can be misleading, so we also estimated statistical models relating observed adoption to estimated net present value.

The relationship remained modest.

Across model specifications and alternative engineering parameterizations, a $1,000 increase in estimated net present value was associated with a relatively small increase in adoption probability. In the primary specification with city and year fixed effects, a one-standard-deviation increase in payoff within a city-year corresponded to an increase in adoption probability of only about 1.2 percentage points.

Estimated net present value by itself explained less than 8 percent of the variation in adoption decisions. Specifications adding location, time, and income controls explained more overall variation, but the payoff-adoption relationship remained limited.

That does **not** mean profitability is irrelevant.

It means that many other factors appear to influence adoption.

{{< figure src="npv-explains-less-than-eight.svg" caption="**Estimated profitability explains little of adoption.** Across the paper’s linear probability models, NPV explains less than eight percent of observed variation in solar adoption." numbered="true" >}}

## What is the solar gap?

We use the term **solar gap** for the evidence that builders sometimes forgo rooftop solar despite positive estimated private payoffs—and, in particular, for the weak relationship between the size of those estimated payoffs and observed adoption.

Notice what this definition does **not** say.

It does not claim that every builder who skipped rooftop solar made a mistake.

Nor does it imply that our engineering model perfectly measures the true profitability of every project.

Instead, it points to something more modest.

If estimated profitability were the dominant driver of adoption, we would expect projects with higher estimated payoffs to adopt much more frequently.

That is not what we observe.

## Why might this happen?

The paper discusses several possible explanations.

### 1. The engineering model may miss some costs

Administrative effort, permitting, contractor coordination, grid interconnection, and design revisions can all create real costs.

These "hassle costs" are difficult to observe and quantify. The paper estimates that, across most parameterizations, unobserved costs or model misspecification would need to exceed roughly $4,000 per project to rationalize even half of the observed non-adoption decisions.

That is possible, but it is not trivial relative to the modeled payoffs.

### 2. Builders and future occupants may face different incentives

The builder typically pays for installing the solar system.

The future homeowner or tenant receives much of the electricity savings.

If builders cannot fully recover that value in the building's sale price or rent, they may rationally install less solar than would be optimal for the eventual occupant. This type of split incentive is familiar from research on energy efficiency.

### 3. Builders may have different expectations

Our engineering model uses information that would have been available when builders made their decisions.

Nevertheless, builders may have formed different expectations about future electricity prices, net-metering rules, installation costs, equipment performance, or tax incentives.

Reasonable decision-makers can disagree about the future.

### 4. Solar payoffs may be relatively small and easy to overlook

This explanation is easy to miss when the payoff is reported in dollars.

The median estimated payoff in our primary analysis is roughly **$7,900**. That sounds substantial.

But the median construction cost among projects with cost data is approximately **$500,000**. For most of those projects, the estimated solar payoff is less than 2 percent of total project cost; for almost all projects, it is below 5 percent.

Builders manage financing, permits, inspections, subcontractors, and dozens of other decisions simultaneously.

In that context, a benefit equal to one or two percent of project cost may simply receive relatively little attention—especially when it is uncertain or primarily benefits a future occupant.

{{< figure src="solar-gap-mechanisms.svg" caption="**Possible mechanisms, not definitive conclusions.** The analysis is consistent with several explanations for the weak payoff–adoption relationship." numbered="true" >}}

## What the paper does—and does not—show

The paper does not identify a single reason builders often declined rooftop solar.

Instead, it documents several related empirical facts:

- estimated private payoffs were positive for most projects under a wide range of assumptions;
- adoption remained low before mandates;
- the very lowest-payoff projects were less likely to adopt; and
- above that lower tail, the size of the estimated payoff only weakly predicted adoption.

These findings support the existence of a solar gap, while leaving room for unobserved costs, differing expectations, split incentives, and other rational explanations.

The extent of the gap is therefore bounded by the assumptions in the engineering model. The most optimistic net-present-value calculations provide an upper bound on what builders could be said to forgo.

## Why this matters beyond rooftop solar

The broader lesson extends beyond California.

Climate policy increasingly depends on technologies that appear economically attractive: heat pumps, electric vehicles, home batteries, building retrofits, and distributed solar.

For each technology, policymakers often ask:

> **How much money does it save?**

That is an important question.

But this research suggests a second question may be equally important:

> **How strongly does expected profitability actually predict adoption?**

Those are not the same thing.

A technology can appear financially attractive while still spreading more slowly than expected. Understanding that difference is essential before deciding whether additional information, financing, incentives, standards, or mandates are warranted.

---

*This post is based on [Solar Adoption by Mandates](/publication/solar_mandates/), joint work with Stefano Carattini, Wade Davis, and Anton Heimerdinger.*

**Previous:** [How We Combined Engineering and Economics](/post/engineering-economics-rooftop-solar/)

**Next:** [Did California's Solar Mandate Increase Solar Adoption?](/post/did-california-solar-mandate-work/)
