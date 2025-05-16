"""
Interactive Samsung Electronics Close Price Visualization

This script creates an interactive plot of Samsung Electronics stock price data
with hover functionality and animation effects that can be embedded in Canva.
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot
import numpy as np
from datetime import datetime

# Load the data
print("Loading Samsung stock price data...")
data = pd.read_csv('Samsung Electronics Stock Historical Price.csv')
data['Date'] = pd.to_datetime(data['Date'])

# Create a simplified dataframe with just Date and Close
df_simple = data[['Date', 'Close']].copy()

# Create the interactive plot
fig = go.Figure()

# Add trace with animation
fig.add_trace(
    go.Scatter(
        x=df_simple['Date'],
        y=df_simple['Close'],
        mode='lines',
        name='Close Price',
        line=dict(width=2, color='#0066cc'),
        hovertemplate='<b>Date</b>: %{x|%Y-%m-%d}<br>' +
                      '<b>Close Price</b>: ₩%{y:,.0f}<br>',
    )
)

# Set up frames for animation
frames = []
for i in range(0, len(df_simple) + 1, 30):  # Animate in monthly chunks for smoothness
    end_idx = min(i, len(df_simple))
    frames.append(
        go.Frame(
            data=[
                go.Scatter(
                    x=df_simple['Date'][:end_idx],
                    y=df_simple['Close'][:end_idx],
                    mode='lines',
                    line=dict(width=2, color='#0066cc'),
                )
            ]
        )
    )

fig.frames = frames

# Add animation buttons
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            buttons=[
                dict(
                    label="Play",
                    method="animate",
                    args=[None, {"frame": {"duration": 30, "redraw": True}, "fromcurrent": True}]
                ),
                dict(
                    label="Pause",
                    method="animate",
                    args=[[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate"}]
                ),
            ],
            direction="left",
            pad={"r": 10, "t": 10},
            showactive=False,
            x=0.1,
            y=0,
            xanchor="right",
            yanchor="top"
        )
    ]
)

# Customize the layout
fig.update_layout(
    title={
        'text': 'Samsung Electronics Close Price (2019-Present)',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 24, 'color': '#333333'}
    },
    xaxis=dict(
        title=dict(text='Date', font=dict(size=16)),
        showgrid=True,
        gridcolor='#E5E5E5',
    ),
    yaxis=dict(
        title=dict(text='Close Price (₩)', font=dict(size=16)),
        showgrid=True,
        gridcolor='#E5E5E5',
        tickformat=',',
    ),
    hovermode='x unified',
    plot_bgcolor='white',
    hoverlabel=dict(
        bgcolor="white",
        font_size=14,
        font_family="Arial"
    ),
    margin=dict(l=80, r=80, t=100, b=80),
)

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1M", step="month", stepmode="backward"),
                dict(count=6, label="6M", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1Y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(visible=True),
        type="date"
    )
)

# Save the figure as an HTML file that can be embedded in Canva
print("Saving interactive visualization as HTML...")
html_path = 'samsung_interactive_chart.html'
plot(fig, filename=html_path, auto_open=False)

# Also save a standalone version for easier viewing
standalone_path = 'samsung_interactive_chart_standalone.html'
with open(html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()
    
# Create a standalone version with improved styling for better embedding
standalone_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Samsung Electronics Stock Price Interactive Visualization</title>
    <style>
        body {{ margin: 0; padding: 0; font-family: Arial, sans-serif; }}
        .chart-container {{ width: 100%; height: 100vh; }}
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

print(f"Interactive visualization saved to {html_path} and {standalone_path}")
print("You can now embed these HTML files in your Canva presentation.")
print("Instructions for embedding in Canva:")
print("1. Upload the HTML file to a web hosting service like GitHub Pages or Netlify")
print("2. In Canva, add an 'Embed' element and paste the URL to your hosted HTML file")
print("3. Alternatively, use the 'Website' embed option in Canva and enter the URL") 