# The Plan

## Set up a scraper to pull all tickers and make a python list.
Libraries: Beautiful soup, requests

## Set up a screener that loops over a list of tickers and then checks for certain things and returns a data frame with other info as well.
Libraries: Alpha Vantage?, pandas, numpy
Functionalities: For now add a option for single stocks and lists. I don't want to be running into request limits on the free market data accounts. 

## Set up a algotrader that can buy and sell stocks. I don't plan to take it live for a long time until I have backtested it but getting it set up to buy and sell stocks will allow me to then implement strategies later