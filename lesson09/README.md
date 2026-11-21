**Date**: Nov 27, 2026

**Time series forecasting**: naive baselines, decomposition, classical models (ETS, ARIMA, TBATS, Prophet), machine learning via reduction, time series foundation models (TimesFM, Chronos-2, TiRex-2, Timestral), ensembles and backtesting, all with [sktime](https://www.sktime.net).

## Notebook

* [01_sktime.ipynb](01_sktime.ipynb): forecasting Wikipedia traffic with sktime (CPU is enough, a GPU makes the foundation models faster)

## Data

Daily visits of 352 popular Wikipedia pages from the Kaggle competition [Web Traffic Time Series Forecasting](https://www.kaggle.com/competitions/web-traffic-time-series-forecasting) (2017):

* [wiki_train.csv.gz](wiki_train.csv.gz): Jul 1, 2015 – Sep 10, 2017 (803 days)
* [wiki_test.csv.gz](wiki_test.csv.gz): Sep 13 – Nov 13, 2017 (62 days)

The original has 145,063 pages, most of them with almost no traffic. We kept the pages with a median above 10,000 visits a day (desktop + mobile, people + bots), without special pages and adult sites, and added the Halloween and Oktoberfest pages. For 119 pages, the last training day was 0 because of missing data; it was replaced by the value from one week earlier. The notebook can optionally keep only the 44 busiest pages, to run faster.

## Links

* sktime [forecasting tutorial](https://www.sktime.net/en/stable/examples/01_forecasting.html) and [list of forecasters](https://www.sktime.net/en/stable/api_reference/forecasting.html)
* Rob J Hyndman and George Athanasopoulos: [Forecasting: Principles and Practice](https://otexts.com/fpp3/) (free book, examples in R)
* Leaderboards of time series foundation models: [GIFT-Eval](https://huggingface.co/spaces/Salesforce/GIFT-Eval), [fev-bench](https://huggingface.co/spaces/autogluon/fev-leaderboard)
