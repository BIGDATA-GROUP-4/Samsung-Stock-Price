# 📈 Samsung Stock Price Analysis
![image](https://github.com/user-attachments/assets/be4fb4ca-914e-4900-b137-4e374afb6876)

## **Project Summary**
This project analyzes Samsung's stock price data to identify patterns, predict future trends, and provide insights for investment decisions. The system collects historical stock data, applies various statistical and machine learning models for analysis, and visualizes the results through interactive dashboards. Key features include price trend analysis, volatility assessment, correlation with market indices, and predictive modeling for short-term price movements.

---

## 🧠 Project Features

### **🔧 Key Features**
- Preprocessing of stock data using PySpark
- Exploratory Data Analysis with Pandas, Seaborn, and Plotly
- Missing data analysis 
- Time Series Decomposition
- Forecasting using XGBoost
- Evaluation using MAE, RMSE, and R²

### **Stock Analysis**
- Performs a comprehensive analysis on Samsung Electronics' historical stock price data
- Includes:
  - Historical data analysis
  - Trend and seasonality decomposition
  - Technical Analysis
  - Builds an XGBoost model with appropriate seasonality settings
  - Forecasts stock prices for the next 5 years
  - Cross-validation and performance metrics
  - Identifies significant change points in the stock price history
  
---

## 📁 Repository Structure

- `Samsung_stockprice.ipynb` – Jupyter notebook with full analysis and Prophet modeling
- `Samsung Electronics Stock Historical Price.csv` – Historical daily stock prices
- `KOSPI Data.csv` – Additional stock data to compare
- `samsung_xgboost_model.pkl` – Serialized model file (optional advanced use)
- `index.html` – Static webpage from the visualization output
- `requirements.txt` – List of Python dependencies

---

## 🚀 Instructions to Run the Code

### 1. Clone the Repository:
```
git clone https://github.com/BIGDATA-GROUP-4/Samsung-Stock-Price.git
cd Samsung-Stock-Price
```

### 2. Install Prerequisites:
- Ensure you have the following installed:
  - Apache Spark
  - JavaHome (required for PySpark)
  - pip (Python package manager)
  - Python 3.8+ installed. Then install the required packages:
```bash
pip install -r requirements.txt
```
- The main dependencies include:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - tensorflow
  - plotly
  - mplfinance
  - statsmodels
  - xgboost 

### 3. Run the Notebook & Dashboard
- Open Samsung_stockprice.ipynb
- Run cells sequentially
- Make sure the dataset file Samsung Electronics Stock Historical Price.csv is placed in the same directory as the notebook or adjust the file path accordingly.

## 📊 What is Included in the Analysis
- Data Preprocessing:
  - Schema inspection
  - Type conversion and date parsing
  - Handling missing values

- Exploratory Data Analysis:
  - Visualizations of stock trends
  - Volume and price relationship
  - Seasonal decomposition

- Forecasting: 
   - Forecast for the next 90 days
   - Model performance metrics
   - Predicting future stock prices using XGBoost
   - Visual comparison of predictions vs actual

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

## 🧑‍💼Contribution Breakdown

| Team Member         | Contribution (%) |
| ------------------- | ---------------- |
| Nguyễn Châu Anh     | 12.22%           |
| Trần Duy Chiến      | 12.53%           |
| Lê Trung Kiên       | 12.53%           |
| Bùi Tuấn Lâm        | 12.33%           |
| Hoàng Mai Linh      | 11.59%           |
| Lương Thị Hồng Ngọc | 12.52%           |
| Lê Hồng Nhung       | 13.90%           |
| Viên Đình Thông     | 12.38%           |

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
