---
title: "The Strange Economics of Rooftop Solar"
subtitle: "Why financially attractive climate technologies do not always get adopted."
summary: "Earlier engineering studies suggested rooftop solar would pay off on nearly all new California homes. Our project-level analysis found a more complicated story."
authors:
- admin
tags:
- solar
- climate policy
- California
categories:
- Research
date: "2026-07-29T12:10:00-07:00"
lastmod: "2026-07-29T13:45:00-07:00"
featured: true
draft: false

image:
  caption: "Estimated private payoffs from rooftop solar"
  focal_point: ""
  placement: 2
  preview_only: true
---

---

**California solar mandate series**

1. **The Strange Economics of Rooftop Solar** *(current)*

2. [How We Combined Engineering and Economics](/post/engineering-economics-rooftop-solar/)

3. [The Solar Gap](/post/solar-gap/)

4. [Did California's Solar Mandate Increase Solar Adoption?](/post/did-california-solar-mandate-work/)

For years, engineering studies supporting California's rooftop solar policies suggested that installing solar would be cost-effective on essentially all new homes.

If that were true, however, a puzzle remained.

Before solar became mandatory, most newly constructed homes in the San Francisco Bay Area did not install it.

Why would builders pass up an investment that appeared to pay for itself?

That question motivated our paper, [Solar Adoption by Mandates](/publication/solar_mandates/). We examine the economics of rooftop solar requirements in California, beginning with San Francisco's 2017 Better Roofs ordinance and then the statewide requirement that took effect in January 2020.

The paper asks three related questions:

1. How profitable was rooftop solar on actual new construction projects before the mandates?
2. Did builders adopt solar on the projects where its estimated payoff was highest?
3. Did the mandates increase adoption relative to what would otherwise have happened?

The answers are more nuanced than either "solar obviously pays" or "builders were irrational."

## Looking beyond the typical house

The engineering studies used to support early solar mandates generally evaluated a small number of hypothetical buildings with stylized characteristics.

We took a different approach.

We assembled detailed data on thousands of actual residential construction projects across the San Francisco Bay Area. We then used the National Renewable Energy Laboratory's System Advisor Model to estimate the expected private payoff from installing rooftop solar on each project.

The calculations account for differences in local sunlight, rooftop shading, electricity consumption, utility tariffs, installation costs, incentives, financing, and system size. Rather than assuming one representative house, we estimated payoffs across the range of buildings that developers were actually constructing.

That produced much more variation than earlier policy studies suggested.

Under our primary assumptions, estimated net present values were positive for every project in the sample. For single-family homes, they ranged from approximately $2,700 to $17,200, with a median of about $7,900. Under alternative assumptions—including higher installation costs, less favorable electricity compensation, and different electricity-use profiles—a minority of projects had negative or very small estimated payoffs.

{{< figure src="solar-payoffs.png" caption="**Estimated private payoffs from rooftop solar.** The primary model produces positive but heterogeneous net present values. Alternative assumptions reduce the estimated payoff for some projects and reveal greater variation than studies based on a small number of representative buildings." numbered="true" >}}

The first lesson, then, is not that rooftop solar was equally profitable everywhere.

It was that solar appeared financially attractive for most projects, but the size and even the sign of the payoff depended on project characteristics and assumptions about future costs, electricity use, incentives, and utility policy.

## Profitable does not necessarily mean important

A median estimated payoff of roughly $8,000 sounds substantial on its own.

But the median construction cost among projects for which we observe costs was approximately $500,000. For most projects, the estimated solar payoff was less than 2 percent of total construction cost, and for almost all projects it was below 5 percent.

That relative scale matters.

A builder manages financing, architectural plans, contractors, inspections, permitting, and a long construction schedule. Even when rooftop solar has a positive estimated return, that return may be small relative to the rest of the project. Additional design work, administrative effort, interconnection delays, or other costs not captured in the engineering model could further reduce its importance.

The expected benefit may also accrue primarily to the future homeowner through lower electricity bills, while the builder bears the installation cost and implementation burden. Whether the builder can fully recover that value in the sale price is uncertain.

So the relevant question is not simply:

> Does solar have a positive estimated net present value?

It is also:

> Is that payoff large, certain, and salient enough to affect the builder's decision?

## Profitability only weakly predicted adoption

Once we had estimated payoffs for individual projects, we compared them with actual solar adoption.

There was a modest positive relationship: projects with the very lowest estimated payoffs were less likely to install solar.

Beyond that lower tail, however, builders declined to install solar across the full range of estimated positive payoffs. Projects with comparatively high expected returns often remained without solar, while some lower-payoff projects adopted it.

Estimated net present value explained less than 8 percent of the variation in adoption decisions.

We refer to this weak connection between estimated private payoffs and observed adoption as the **solar gap**.

The finding does not prove that builders behaved irrationally. Our payoff estimates may omit project-specific constraints or costs that builders understood. Expectations about future tax credits, electricity rates, or net-metering policies may also have differed from the assumptions in the model.

Still, the results suggest that estimated profitability was not the dominant factor in many adoption decisions.

## What could explain the gap?

Several mechanisms are plausible.

Builders may not capture the future electricity savings enjoyed by occupants. Financing or liquidity constraints may make upfront costs more important than long-run returns. Information may be incomplete. Developers may be uncertain about future electricity tariffs or incentive policies. Solar installation may also involve permitting, contractor coordination, interconnection, and other "hassle costs" not fully represented in an engineering model.

Another possibility is simple scale and attention. An expected solar payoff equal to one or two percent of total project cost may receive little attention amid the larger demands of constructing a building.

Our analysis does not isolate one definitive explanation. Instead, it shows that a simple model in which builders adopt whenever estimated net present value is positive does a poor job of describing the observed data.

## What the mandates changed

California's policies allow us to ask what happened when rooftop solar was no longer left entirely to voluntary adoption.

San Francisco's 2017 Better Roofs ordinance applied to new residential, commercial, and municipal buildings, although it included exemptions and allowed solar thermal systems or living roofs as alternative compliance pathways.

Using synthetic-control methods, we estimate that the San Francisco policy increased the share of new residential buildings with solar photovoltaics by 33 percentage points—more than doubling the pre-policy adoption rate. A complementary synthetic difference-in-differences analysis produces a similar estimate of 31 percentage points.

California's statewide mandate took effect in January 2020 for newly constructed low-rise residential buildings. At the state level, we cannot directly observe the solar share among new homes, so we use total residential solar capacity additions per new residential building permit as a proxy outcome.

Depending on the estimator and time aggregation, we find an increase of approximately 5.4 to 8.5 kilowatts of residential solar capacity per new building permit, equivalent to an increase of roughly 38 to 60 percent relative to the counterfactual.

These results indicate that both mandates substantially increased solar adoption.

That does not mean they produced universal rooftop solar. San Francisco's ordinance contained exemptions and alternative compliance pathways, while California's code also included exemptions and options such as community solar. Policy design and implementation therefore matter when interpreting post-mandate adoption.

## Increasing adoption is not the same as proving a policy is efficient

It is tempting to move directly from "the mandate increased rooftop solar" to "the mandate was good policy."

Our paper is more cautious.

The engineering model estimates **private payoffs** to adopters, not the full social costs and benefits of the mandate. A substantial share of those private payoffs came from the federal Investment Tax Credit and California's net-metering policies. Removing the tax credit reduces the median estimated payoff by 41 percent; replacing net metering with a less valuable compensation policy reduces it by 58 percent; removing both reduces it by 75 percent.

Those policies transfer value to rooftop solar adopters, but transfers are not themselves net social benefits.

A complete policy assessment would also compare distributed rooftop solar with alternatives such as utility-scale renewable generation, which can often produce electricity at lower capital cost. Rooftop solar may provide other benefits, including distributed generation and potential grid-management value, but those benefits must be weighed against its higher cost.

Our results therefore support a narrower and more defensible conclusion:

> Solar mandates substantially increased rooftop solar adoption, and many of the projects induced to adopt likely received positive private payoffs under the policies in place.

That is different from showing that rooftop mandates are the least-cost way to increase renewable electricity generation. The paper ultimately finds limited support for preferring mandates for rooftop solar over larger utility-scale projects on efficiency grounds.

## The broader lesson

The most interesting part of this project is the gap between technological possibility and observed behavior.

Engineering models can estimate whether a technology is likely to generate electricity and produce a positive financial return. They are less well suited to predicting whether builders, households, or firms will actually adopt it.

That second question depends on incentives, information, uncertainty, financing, transaction costs, institutional design, and who bears the cost relative to who receives the benefit.

The same issue arises with heat pumps, insulation, electric vehicles, batteries, and climate-adaptation measures. Lower costs and better technology are essential, but they do not guarantee adoption.

Understanding how technologies perform is an engineering question.

Understanding whether they spread—and whether policy should compel them to spread—is also an economic and institutional one.

---

*This post is based on [Solar Adoption by Mandates](/publication/solar_mandates/), joint work with Stefano Carattini, Wade Davis, and Anton Heimerdinger. The [full working paper](/publication/solar_mandates/Carattini_Davis_Figge_and_Heimerdinger_2025.pdf) contains the technical details, robustness analyses, and complete results.*

**Next:** [How We Combined Engineering and Economics](/post/engineering-economics-rooftop-solar/)
