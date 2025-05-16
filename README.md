# 📈 Samsung Stock Price Forecasting and Visualization

This repository provides tools to analyze, forecast, and visualize the historical stock prices of **Samsung Electronics** using time series models and interactive charts.

---

## 🧠 Project Features


### 1. **Stock Forecasting**
- Performs a comprehensive time series analysis on Samsung Electronics historical stock price data
- Includes:
  - Historical data analysis
  - Trend and seasonality decomposition
  - Technical Analysis
  - Builds a XGBoost model with appropriate seasonality settings
  - Forecasts stock prices for the next 5 years
  - Cross-validation and performance metrics
  - Identifies significant changepoints in the stock price history

### 2. **Interactive Data Visualization**
- Features:
  - Interactive Plot: Hover over any point to see the exact date and closing price
  - Animated Line: Watch the stock price trend develop over time with play/pause controls
  - Date Range Selector: Zoom in on specific time periods (1M, 6M, YTD, 1Y, All)
  - Range Slider: Drag to select custom date ranges
  - Exportable: Creates HTML files that can be embedded in Canva presentations
---

## 📁 Repository Structure

- `Samsung_stockprice.ipynb` – Jupyter notebook with full analysis and Prophet modeling
- `Samsung Electronics Stock Historical Price.csv` – Historical daily stock prices
- `KOSPI Data.csv` – Additional contextual stock data
- `samsung_interactive_visualization.py` – Script for Plotly interactive charts
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
2. The script will install necessary packages and run the visualization
3. Your default web browser will open with the interactive chart

#### Manual Setup

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Run the visualization script:
   ```
   python samsung_interactive_visualization.py
   ```

3. Open the generated HTML file in your web browser:
   - `samsung_interactive_chart_standalone.html`

#### Embedding in Canva

To embed this visualization in a Canva presentation:

1. Upload the HTML file to a web hosting service like GitHub Pages, Netlify, or any web hosting you have access to
2. In Canva, add an 'Embed' element to your slide
3. Paste the URL to your hosted HTML file
4. Alternatively, use the 'Website' embed option in Canva and enter the URL

---

## 📊 Outputs

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
---

## 🔧 Customization

To modify the forecast horizon or model parameters, edit the following variables in the script:
- `future_years`: Number of years to forecast (default: 5)
- Model parameters in the Prophet initialization like `changepoint_prior_scale` and `seasonality_prior_scale`

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