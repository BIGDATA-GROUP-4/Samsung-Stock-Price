![Auto Assign](https://github.com/BIGDATA-GROUP-4/demo-repository/actions/workflows/auto-assign.yml/badge.svg)

![Proof HTML](https://github.com/BIGDATA-GROUP-4/demo-repository/actions/workflows/proof-html.yml/badge.svg)

# Welcome to your organization's demo respository
This code repository (or "repo") is designed to demonstrate the best GitHub has to offer with the least amount of noise.

The repo includes an `index.html` file (so it can render a web page), two GitHub Actions workflows, and a CSS stylesheet dependency.

# Samsung Stock Price Forecasting with Prophet

This repository contains a complete implementation of Facebook's Prophet model for forecasting Samsung Electronics stock prices.

## Overview

The `samsung_prophet_model.py` script performs a comprehensive time series analysis on Samsung Electronics historical stock price data:

- Loads and analyzes historical stock data
- Builds a Prophet model with appropriate seasonality settings
- Forecasts stock prices for the next 5 years
- Provides visualizations for trends, seasonality, and forecast components
- Calculates accuracy metrics and performs cross-validation
- Identifies significant changepoints in the stock price history

## Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

## Data

The script expects a CSV file named `Samsung Electronics Stock Historical Price.csv` in the same directory, with at least the following columns:
- `Date`: The trading date
- `Close`: The closing price for each trading day

## Usage

Run the script with:

```bash
python samsung_prophet_model.py
```

## Output

The script generates:

1. Static visualizations saved as PNG files:
   - `samsung_historical.png`: Historical stock price chart
   - `samsung_forecast.png`: Forecasted prices for the next 5 years
   - `samsung_components.png`: Decomposition of the forecast into trend, weekly, and yearly seasonality
   - `samsung_cv_results.png`: Cross-validation results
   - `samsung_changepoints.png`: Stock price chart with identified changepoints

2. Interactive Plotly visualizations saved as HTML files:
   - `samsung_forecast_interactive.html`: Interactive forecast visualization
   - `samsung_components_interactive.html`: Interactive components visualization

3. Console output with:
   - Data summary statistics
   - Forecast for the next 30 days
   - Model performance metrics (MAPE and RMSE)
   - Cross-validation results

## Interpreting Results

- **Trend**: The overall trend of Samsung stock prices
- **Weekly Seasonality**: How prices vary by day of the week
- **Yearly Seasonality**: Annual patterns in the stock price
- **Changepoints**: Significant shifts in the trend
- **Forecast Uncertainty**: Upper and lower bounds for predictions

## Customization

To modify the forecast horizon or model parameters, edit the following variables in the script:
- `future_years`: Number of years to forecast (default: 5)
- Model parameters in the Prophet initialization like `changepoint_prior_scale` and `seasonality_prior_scale`
