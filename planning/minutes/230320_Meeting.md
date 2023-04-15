# Meeting 20/03/23

## Agenda:

-   Previous Actions

    -   Dave: Set up meeting for 7pm-8pm Wednesday.

        -   Dave: Done

    -   Everyone: Find at least 4 more solar-related articles to review.

    -   Everyone: Find and collate other data.

    -   Everyone: Start data exploration.

        -   Compare factors and consider interpolation.

    -   Everyone: Narrow down the research scope.

-   Data collation and exploration to date

-   Additional research to date

-   Use task board on Todoist?

-   Refine research scope

## Actions

-   Dave: Set up next team meeting.

-   Zoren: Set up this week's meeting w/ lecturer, including agenda in
    > request and calendar invite.

-   Sam: Explore range of (min and max) grid demand on days relative to
    > weather (using rain as proxy?), using a basic linear model
    > (precipitation + temperature).

    -   Also look at how broad solar uptake affects these peaks.

    -   Dave: So we could phrase our research question as "What effect
        > does the uptake of residential solar have on the dynamic range
        > of grid demand?"

-   Dave: Help Sam to merge to main in Github.

-   Dave: Investigate possible duplicates in demand data.

## Notes

-   Sam: I've been working on the Clean Energy Regulator data. I think I
    > might have pulled it into main but I'm not sure.

    -   Sam: This is all NSW data.

-   Sam: There doesn't appear to be much relationship between rain and
    > demand (based on the weather station I got).

    -   Sam: We could aggregate up to get a better view on this.

-   Aaron: I've been looking at the temperature interpolation thing.

-   Dave: ... Talked about what I did.

    -   Exploratory data analysis on given data:
        > [[https://docs.google.com/document/d/17eF7tTns474qM4IhrGRvxNK2KwvxSZvLxjGfULdHxzs/edit#]{.underline}](https://docs.google.com/document/d/17eF7tTns474qM4IhrGRvxNK2KwvxSZvLxjGfULdHxzs/edit#)

    -   Literature review on impacts of solar to energy demand:
        > [[https://docs.google.com/document/d/1HnhMcezWpKxXeXhcycxMCCw2bIcgrokO4nR0oe60LKI/edit?usp=share_link]{.underline}](https://docs.google.com/document/d/1HnhMcezWpKxXeXhcycxMCCw2bIcgrokO4nR0oe60LKI/edit?usp=share_link)

    -   Scraped AEMO price data:
        > [[https://github.com/dmc-au/Team-A\-\--Impacts-of-Household-PV-on-Grid-Demand/blob/main/src/aemo-price-scrape.sh]{.underline}](https://github.com/dmc-au/Team-A---Impacts-of-Household-PV-on-Grid-Demand/blob/main/src/aemo-price-scrape.sh)

-   Team: Agreeing to work with weekly and upwards analysis and
    > modeling.

-   Zoren notes:

    -   Merged PV install data (on Python)

    -   Looking into simple model between demand, temperature and solar
        > PV uptake
