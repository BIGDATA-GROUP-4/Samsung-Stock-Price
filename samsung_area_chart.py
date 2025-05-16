"""
Samsung Electronics Stock Performance (2019-2025)
Area Chart Visualization with Forecast

This script creates an interactive area chart visualization of Samsung stock prices
with quarterly formatting and forecast extension.
"""

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
from datetime import datetime, timedelta
import plotly.express as px

# Load the data
print("Loading Samsung stock price data...")
data = pd.read_csv('Samsung Electronics Stock Historical Price.csv')
data['Date'] = pd.to_datetime(data['Date'])

# Create quarterly resampled data
data = data.set_index('Date')
quarterly_data = data['Close'].resample('Q').last().reset_index()
quarterly_data['Quarter'] = quarterly_data['Date'].dt.year.astype(str) + ' Q' + quarterly_data['Date'].dt.quarter.astype(str)

# Generate future forecast data
# Get the last date in our dataset
last_date = quarterly_data['Date'].max()
start_forecast = last_date + pd.Timedelta(days=1)

# Create future dates (quarterly until 2025 Q4)
future_quarters = pd.date_range(start=start_forecast, end='2025-12-31', freq='Q')
future_data = pd.DataFrame({'Date': future_quarters})
future_data['Quarter'] = future_data['Date'].dt.year.astype(str) + ' Q' + future_data['Date'].dt.quarter.astype(str)

# Generate synthetic forecast values (simple model for visualization purposes)
# Using last values and adding slight variability and trend
last_value = quarterly_data['Close'].iloc[-1]
forecast_length = len(future_data)
# Creating a somewhat realistic forecast pattern
trend = np.concatenate([
    np.linspace(0, 5000, 5),    # Small rise
    np.linspace(5000, -8000, 8), # Peak and fall
    np.linspace(-8000, 0, 3)    # Recovery
])[:forecast_length]
noise = np.random.normal(0, 1000, forecast_length)  # Add some randomness
future_data['Close'] = last_value + trend + noise

# Combine historical and forecast data
combined_data = pd.concat([quarterly_data, future_data], ignore_index=True)

# Create the interactive plot with custom styling to match the image
fig = go.Figure()

# Add area chart for historical data
fig.add_trace(
    go.Scatter(
        x=combined_data['Quarter'],
        y=combined_data['Close'],
        fill='tozeroy',
        mode='lines',
        line=dict(color='rgb(100, 100, 220)', width=3),
        fillcolor='rgba(100, 100, 220, 0.2)',
        name='Stock Price (KRW)',
        hovertemplate='%{x}<br>Price (KRW): ₩%{y:,.0f}<extra></extra>'
    )
)

# Mark the transition point between historical and forecast data
historical_len = len(quarterly_data)
fig.add_vline(
    x=historical_len - 0.5,  # Position between last historical and first forecast
    line=dict(color="rgba(150, 150, 150, 0.5)", width=1, dash="dash")
)

# Add forecast annotation
fig.add_annotation(
    x=historical_len + forecast_length/4,
    y=combined_data['Close'].min() + (combined_data['Close'].max() - combined_data['Close'].min())*0.1,
    text="Forecast Start",
    showarrow=False,
    font=dict(size=14, color="rgba(150, 150, 150, 0.8)")
)

# Customize the layout to match the image
fig.update_layout(
    title={
        'text': 'Stock Performance (2019-2025)',
        'y': 0.95,
        'x': 0.05,
        'xanchor': 'left',
        'yanchor': 'top',
        'font': {'size': 24, 'color': '#0A2A52', 'family': 'Arial, sans-serif'}
    },
    xaxis=dict(
        title=None,
        showgrid=True,
        gridcolor='rgba(211, 211, 211, 0.5)',
        gridwidth=0.5,
        zeroline=False,
        tickmode='array',
        tickvals=combined_data['Quarter'][::4],  # Show every year's Q1
        ticktext=combined_data['Quarter'][::4],
        tickangle=0,
        tickfont=dict(size=12)
    ),
    yaxis=dict(
        title=None,
        showgrid=True,
        gridcolor='rgba(211, 211, 211, 0.5)',
        gridwidth=0.5,
        zeroline=False,
        tickformat=',',
        tickprefix='₩',
        range=[combined_data['Close'].min() * 0.9, combined_data['Close'].max() * 1.1]
    ),
    plot_bgcolor='white',
    paper_bgcolor='white',
    margin=dict(l=50, r=50, t=80, b=50),
    hoverlabel=dict(
        bgcolor="white",
        font_size=14,
        font_family="Arial, sans-serif",
        bordercolor="rgba(0, 0, 0, 0.3)"
    ),
    showlegend=True,
    legend=dict(
        x=0.01,
        y=0.99,
        orientation='h',
        bgcolor='rgba(255, 255, 255, 0)'
    )
)

# Add a custom hover template with the quarter info
fig.update_traces(
    hovertemplate='<b>%{x}</b><br>Price (KRW): ₩%{y:,.0f}<extra></extra>'
)

# Save the figure as an HTML file
print("Saving area chart visualization as HTML...")
html_path = 'samsung_area_chart.html'
plot(fig, filename=html_path, auto_open=False)

# Create a standalone version for better embedding
standalone_path = 'samsung_area_chart_standalone.html'
with open(html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()
    
standalone_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Samsung Electronics Stock Performance (2019-2025)</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }}
        .chart-container {{
            width: 100%;
            height: 100vh;
            background-color: white;
        }}
    </style>
</head>
<body>
    <div class="chart-container">
        {html_content}
    </div>
</body>
</html>
"""

with open(standalone_path, 'w', encoding='utf-8') as file:
    file.write(standalone_html)

print(f"Area chart visualization saved to {html_path} and {standalone_path}")
print("You can now embed these HTML files in your Canva presentation.") 