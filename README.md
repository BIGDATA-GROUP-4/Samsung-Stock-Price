# 📈 Samsung Stock Price Forecasting and Visualization

This repository provides tools to analyze, forecast, and visualize the historical stock prices of **Samsung Electronics** using time series models and interactive charts.

---

## 🧠 Project Features

### 1. **Stock Forecasting**
- Performs a comprehensive time series analysis on Samsung Electronics' historical stock price data
- Includes:
  - Historical data analysis
  - Trend and seasonality decomposition
  - Technical Analysis
  - Builds an XGBoost model with appropriate seasonality settings
  - Forecasts stock prices for the next 5 years
  - Cross-validation and performance metrics
  - Identifies significant change points in the stock price history

### 2. **Interactive Data Visualization**
- Features:
  - Interactive Plot: Hover over any point to see the exact date and closing price
  - Animated Line: Watch the stock price trend develop over time with play/pause controls
  - Date Range Selector: Zoom in on specific periods (1M, 6M, YTD, 1Y, All)
  - Range Slider: Drag to select custom date ranges
  - Exportable: Creates HTML files that can be embedded in Canva presentations
---

## 📁 Repository Structure

- `Samsung_stockprice.ipynb` – Jupyter notebook with full analysis and Prophet modeling
- `Samsung Electronics Stock Historical Price.csv` – Historical daily stock prices
- `KOSPI Data.csv` – Additional contextual stock data
- `run_visualization.bat` – Batch file to run visualization on Windows
- `samsung_xgboost_model.pkl` – Serialized model file (optional advanced use)
- `index.html` – Static webpage from the visualization output
- `requirements.txt` – List of Python dependencies

---

## 🚀 Getting Started

### Setup Environment

```bash
pip install -r requirements.txt
```

### Run Forecasting (Prophet)

```bash
python samsung_xgboost_model.py
```

### Run Visualization (Interactive)

#### Windows

1. Double-click the `run_visualization.bat` file
2. The script will install the necessary packages and run the visualization
3. Your default web browser will open with the interactive chart

#### Manual Setup

Install the required packages:
   ```
   pip install -r requirements.txt
   ```
---

## 📊 Outputs

The script generates: 
   - Data summary statistics
   - Forecast for the next 30 days
   - Model performance metrics (MAPE and RMSE)
   - Cross-validation results
---

## 👥 Contributors

- [@BIGDATA-GROUP-4](https://github.com/BIGDATA-GROUP-4) – Team Collaboration
<a href="https://github.com/immaFrogUwU">
  <img src="https://avatars.githubusercontent.com/u/130581573?v=4" width="50" height="50" alt="immaFrogUwU"/>
</a>
<a href="https://github.com/chientd29">
  <img src="https://avatars.githubusercontent.com/u/137612901?v=4" width="50" height="50" alt="chientd29"/>
</a>
<a href="https://github.com/lamyeucoding">
  <img src="https://avatars.githubusercontent.com/u/203073838?v=4" width="50" height="50" alt="lamyeucoding"/>
</a>
<a href="https://github.com/bbbunny03">
  <img src="https://avatars.githubusercontent.com/u/207357130?v=4" width="50" height="50" alt="bbbunny03"/>
</a>
<a href="https://github.com/chauanh14">
  <img src="https://avatars.githubusercontent.com/u/207451086?v=4" width="50" height="50" alt="chauanh14"/>
</a>
<a href="https://github.com/troc02244">
  <img src="https://avatars.githubusercontent.com/u/192955263?v=4" width="50" height="50" alt="troc02244"/>
</a>
<a href="https://github.com/letrungkien2004">
  <img src="https://avatars.githubusercontent.com/u/207433917?v=4" width="50" height="50" alt="letrungkien2004"/>
</a>
<a href="https://github.com/theycallmevong">
  <img src="https://avatars.githubusercontent.com/u/207429199?v=4" width="50" height="50" alt="theycallmevong"/>
</a>

---

## 📄 License

This project is licensed under the **MIT License**.
