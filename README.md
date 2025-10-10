# Index

## Press release scraper
A webscraper that I built to monitor a stocks website and email me when a new press release came out. The stock was highly volatile and would jump a lot based on news so it was important to me to be able to monitor it. While I don't trade the stock as much anymore I do still have the script running on my computer.

## Screener
Still a work in progress but I have the basic format laid out. It includes a function to check a list of ickers to see if they have been delisted. It then removes any that throw errors and moves them into a fresh list and saves it as a .txt file. Eventually I want to be using this to find my stocks but I need to lock in my strategy and what I am looking for. As of right now I am having it print as a dataFrame but I think eventually I will export it to excel to have more freedom and readability for the 

### To improve:
1. Speed, it's pretty slow and could be made more efficient, especially when I start screening for specific things. 


## Scraper(Unfinished)
Eventually I want to add a scraper that scrapes a website for tickers. I want it to be one that I have freedom with(possibly nasdaq or yahoo finance) so I can make one scraper but use different urls from the website to scrape different things like sectors. I will have that separate though and save them all as separate files so I don't run it everytime

## Trader(Unfinished)
While I don't think I will ever send it live unless I put a lot of time into it I would like to set up a little algorythmic trader that can buy and sell stocks. Don't know what strategy I will use but I'll start with something simple like the golden cross and maybe one day I put the time in to come up with a strategy.

# The Plan

## Set up a scraper to pull all tickers and make a python list.
Libraries: Beautiful soup, requests

## Set up a screener that loops over a list of tickers and then checks for certain things and returns a data frame with other info as well.
Libraries: yfinance, pandas, numpy
Functionalities: For now add a option for single stocks and lists. I don't want to be running into request limits on the free market data accounts.

## Set up a algotrader that can buy and sell stocks. I don't plan to take it live for a long time until I have backtested it but getting it set up to buy and sell stocks will allow me to then implement strategies later