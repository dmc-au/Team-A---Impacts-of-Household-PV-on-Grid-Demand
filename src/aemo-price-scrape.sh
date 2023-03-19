#!/bin/bash

# Scrapes all of the AEMO price and demand CSV files
# from 2010 to 2022. The important metric is RRP:
# Region Region Reference Price. Spot price at the regional
# reference node.
# https://aemo.com.au/en/learn/industry-terminology

# Run this script from within the /data/raw folder:
# > source ../../src/aemo-price-scrape.sh

base_url="https://aemo.com.au/aemo/data/nem/priceanddemand/PRICE_AND_DEMAND_"
for (( year=2010; year<=2022; year++ ))
do
    for (( month=1; month<=12; month++ ))
    do
        if (( month < 10 ));
        then
            full_url="${base_url}${year}0${month}_NSW1.csv"
            file_path="${full_url}"
            curl "${full_url}" -O
        else
            full_url="${base_url}${year}${month}_NSW1.csv"
            file_path="${full_url}"
            curl "${full_url}" -O 
        fi
    done
done
cat *csv > aemo-total-demand-and-price.csv
rm *PRICE_AND_DEMAND*