-   Factors affecting demand

    -   Temperature

    -   Time of the day

        -   Previously (10 -- 20 years ago), peak demand was during the
            day when really hot. Now, a lot of roof solar, now from grid
            perspective, it is reduced demand from the grid.

        -   One distinguish is between real power demand (how much power
            NSW requires) to operational demand (how much the power
            stations actually need to generate, after taking away roof
            solar)

        -   Hence wrangle data to look at time of the day

-   Retraining models

    -   Can be as frequent as you want

    -   But Jack does it twice a month or so, but project dependent

-   Time scale resolution

    -   Typically 30 minute out, and outlook next day and next week

    -   Again, project dependent

-   Clients

    -   Governments (state and federal), longer term planning, want to
        avoid blackouts

        -   E.g. if Queensland builds a large pump hydro, how does that
            affect NSW

        -   Economics/market design

        -   If we shut down these coal power stations, which provided a
            lot of grid stabilisation services, but we don't get these
            services from newer inverter-based services (e.g.
            wind/solar)

        -   So does the government have to pay to provide these
            services? Or we have to build new infrastructure/services in
            these areas

        -   Because we deal with such long horizons, dataset and
            modelling are more interesting

            -   Will need to simplify

            -   A 1% better answer results in huge savings/gains

    -   Transmission/distribution companies

        -   Those we build/maintain the poles/wires

    -   European company interested in buying power stations in NSW

-   Prefer newer data (2 \~ 4 years)

    -   Older data not as good

        -   E.g. demand profiles have changed

            -   E.g. 10/20 years ago peak demand was midday, now in
                evening

    -   Everything is changing, hence need recent data for better
        prediction

-   Roof solar impact

    -   Look up "duck curve"

    -   Over past 15 years, look at demand by the hour, how that has
        changed

    -   They have been a number of power stations that been shut down
        (e.g. 2016) that has changed how the industry works

-   Acceptable model accuracy

    -   Jack reckons within a few hundred MW, should be alright

    -   Depend on the horizon

    -   E.g. shorter term (next dispatch interval), e.g. 30min
        intervals?

    -   But ofc, unforeseen events can dramatically change things

        -   E.g. cloud covering city and hence solar, that was
            equivalent to losing a power station

    -   Look at overall predictive power of model, but also look at what
        time of day or what things that makes the model worse

-   Near-future impacts to power industry

    -   Roof top solar affect power industry and power demand prediction

    -   Some areas has so much roof solar, creates "negative demand"
        e.g. in SA

        -   So much solar in mid of the day, more power pushed into grid
            than demand itself

        -   This causes problems and breaks things

        -   Too much power in

    -   Coal power stations on schedule to be retired over next few
        years

        -   There are plans to build more station/renewables to replace
            it

        -   But when announcement happens, e.g. within 5/10 years, but
            after announcement they like to announce to close it faster,
            but it creates a race to rebuild grid in shorter time to
            keep it stable

-   Types of models forecasting demand

    -   5 min

        -   20 year old NN, 3 layers (1 hidden), 9 inputs

            -   Change in demand interval proceeding next interval

            -   Change in demand over 5 min basis, 30 min basis, up to
                dispatch interval

            -   Change in demand previously

            -   NOT GOOD MODEL

        -   Used in real time

    -   1 to 2 days

    -   A week

        -   Bayesian deep belief network?

        -   For longer term

    -   A collection of models depending on horizon

-   Sometimes students have outperforms AMOS, why don't they update
    their models

    -   

-   Next disruptor

    -   Not in dataset yet

    -   EVs and batteries

        -   Fast charging grid for EVs

    -   Household batteries

    -   Storage technology

    -   There are companies called VPPs (virtual power plants) which are
        software companies

        -   If you can sign up10k household batteries, now you have
            control to a power station

        -   Now you can bid in

    -   But a lot of uncertainty

    -   Before, cost of battery tech was getting cheaper, but last 2
        years it was getting expensive due to raw materials, how will
        the price of raw materials change

-   Ideas

    -   Impact of EV

    -   Impact of power stations closing

    -   Impact of solar

        -   Sales of solar

        -   Install of solar

    -   Impact of wind

    -   Impact of cash rates

    -   Impact of natural weather/disaster

-   Is it possible to
