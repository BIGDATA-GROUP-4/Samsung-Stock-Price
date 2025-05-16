"""
Enhanced Interactive Samsung Electronics Close Price Visualization for Canva

This script creates a highly customized interactive plot of Samsung Electronics stock price data
with hover functionality, animation effects, and additional features for embedding in Canva.
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot
import numpy as np
from datetime import datetime
import plotly.express as px

# Load the data
print("Loading Samsung stock price data...")
data = pd.read_csv('Samsung Electronics Stock Historical Price.csv')
data['Date'] = pd.to_datetime(data['Date'])

# Create a simplified dataframe with just Date and Close
df_simple = data[['Date', 'Close']].copy()

# Calculate moving averages
df_simple['MA50'] = df_simple['Close'].rolling(window=50).mean()
df_simple['MA200'] = df_simple['Close'].rolling(window=200).mean()

# Add percentage change from initial price
first_price = df_simple['Close'].iloc[0]
df_simple['Pct_Change'] = ((df_simple['Close'] - first_price) / first_price) * 100

# Create a custom color scale
colors = px.colors.sequential.Blues

# Create the interactive plot
fig = go.Figure()

# Add main trace with animation
fig.add_trace(
    go.Scatter(
        x=df_simple['Date'],
        y=df_simple['Close'],
        mode='lines',
        name='Close Price',
        line=dict(width=3, color='#0066cc'),
        hovertemplate='<b>Date</b>: %{x|%Y-%m-%d}<br>' +
                      '<b>Close Price</b>: ₩%{y:,.0f}<br>' +
                      '<extra></extra>',
    )
)

# Add 50-day moving average
fig.add_trace(
    go.Scatter(
        x=df_simple['Date'],
        y=df_simple['MA50'],
        mode='lines',
        name='50-Day MA',
        line=dict(width=2, color='#ff9900', dash='dash'),
        hovertemplate='<b>50-Day MA</b>: ₩%{y:,.0f}<br><extra></extra>',
    )
)

# Add 200-day moving average
fig.add_trace(
    go.Scatter(
        x=df_simple['Date'],
        y=df_simple['MA200'],
        mode='lines',
        name='200-Day MA',
        line=dict(width=2, color='#ff0000', dash='dash'),
        hovertemplate='<b>200-Day MA</b>: ₩%{y:,.0f}<br><extra></extra>',
    )
)

# Create animation frames for the main line
frames = []
for i in range(0, len(df_simple) + 1, 20):  # Increase animation smoothness
    end_idx = min(i, len(df_simple))
    
    # Only display MA after we have enough data points
    ma50_data = df_simple['MA50'].iloc[:end_idx]
    ma200_data = df_simple['MA200'].iloc[:end_idx]
    
    frames.append(
        go.Frame(
            data=[
                go.Scatter(
                    x=df_simple['Date'][:end_idx],
                    y=df_simple['Close'][:end_idx],
                    mode='lines',
                    line=dict(width=3, color='#0066cc'),
                ),
                go.Scatter(
                    x=df_simple['Date'][:end_idx],
                    y=ma50_data,
                    mode='lines',
                    line=dict(width=2, color='#ff9900', dash='dash'),
                ),
                go.Scatter(
                    x=df_simple['Date'][:end_idx],
                    y=ma200_data,
                    mode='lines',
                    line=dict(width=2, color='#ff0000', dash='dash'),
                )
            ]
        )
    )

fig.frames = frames

# Add animation controls
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            buttons=[
                dict(
                    label="Play",
                    method="animate",
                    args=[None, {"frame": {"duration": 20, "redraw": True}, "fromcurrent": True}]
                ),
                dict(
                    label="Pause",
                    method="animate",
                    args=[[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate"}]
                ),
                dict(
                    label="Reset",
                    method="animate",
                    args=[
                        [frames[0].name],
                        {
                            "frame": {"duration": 0, "redraw": True},
                            "mode": "immediate"
                        }
                    ]
                )
            ],
            direction="left",
            pad={"r": 10, "t": 10},
            showactive=False,
            x=0.1,
            y=0,
            xanchor="right",
            yanchor="top",
            bgcolor="rgba(255, 255, 255, 0.7)",
            bordercolor="rgba(0, 0, 0, 0.5)",
            borderwidth=1,
            font=dict(size=12)
        )
    ]
)

# Calculate min and max for better y-axis range
y_min = df_simple['Close'].min() * 0.95  # Add 5% padding
y_max = df_simple['Close'].max() * 1.05  # Add 5% padding

# Customize the layout
fig.update_layout(
    title={
        'text': 'Samsung Electronics Stock Price (2019-Present)',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 24, 'color': '#333333', 'family': 'Arial, sans-serif'}
    },
    xaxis=dict(
        title=dict(text='Date', font=dict(size=16, family='Arial, sans-serif')),
        showgrid=True,
        gridcolor='rgba(211, 211, 211, 0.5)',
        gridwidth=0.5,
    ),
    yaxis=dict(
        title=dict(text='Close Price (₩)', font=dict(size=16, family='Arial, sans-serif')),
        showgrid=True,
        gridcolor='rgba(211, 211, 211, 0.5)',
        gridwidth=0.5,
        tickformat=',',
        range=[y_min, y_max]
    ),
    hovermode='x unified',
    plot_bgcolor='rgba(255, 255, 255, 1)',
    paper_bgcolor='rgba(255, 255, 255, 1)',
    hoverlabel=dict(
        bgcolor="white",
        font_size=14,
        font_family="Arial, sans-serif",
        bordercolor="rgba(0, 0, 0, 0.3)",
    ),
    margin=dict(l=80, r=80, t=100, b=80),
    legend=dict(
        x=0.01,
        y=0.99,
        bgcolor='rgba(255, 255, 255, 0.8)',
        bordercolor='rgba(0, 0, 0, 0.3)',
        borderwidth=1,
        font=dict(family='Arial, sans-serif', size=12)
    ),
)

# Add range slider with improved styling
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1M", step="month", stepmode="backward"),
                dict(count=6, label="6M", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1Y", step="year", stepmode="backward"),
                dict(step="all", label="All")
            ]),
            bgcolor='rgba(255, 255, 255, 0.8)',
            bordercolor='rgba(0, 0, 0, 0.3)',
            borderwidth=1,
            font=dict(family='Arial, sans-serif', size=12),
            x=0.01,
            y=1.01,
        ),
        rangeslider=dict(
            visible=True,
            bgcolor='rgba(211, 211, 211, 0.3)',
            bordercolor='rgba(211, 211, 211, 0.8)',
        ),
        type="date"
    )
)

# Add annotations
min_point = df_simple.loc[df_simple['Close'].idxmin()]
max_point = df_simple.loc[df_simple['Close'].idxmax()]

fig.add_annotation(
    x=min_point['Date'],
    y=min_point['Close'],
    text=f"Min: ₩{int(min_point['Close']):,}",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowcolor="#D32F2F",
    arrowwidth=2,
    bgcolor="rgba(255, 255, 255, 0.8)",
    bordercolor="#D32F2F",
    borderwidth=1,
    borderpad=4,
    font=dict(family="Arial, sans-serif", size=12, color="#D32F2F"),
)

fig.add_annotation(
    x=max_point['Date'],
    y=max_point['Close'],
    text=f"Max: ₩{int(max_point['Close']):,}",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowcolor="#388E3C",
    arrowwidth=2,
    bgcolor="rgba(255, 255, 255, 0.8)",
    bordercolor="#388E3C",
    borderwidth=1,
    borderpad=4,
    font=dict(family="Arial, sans-serif", size=12, color="#388E3C"),
)

# Save the figure as an HTML file that can be embedded in Canva
print("Saving enhanced interactive visualization as HTML...")
html_path = 'samsung_interactive_chart_enhanced.html'
plot(fig, filename=html_path, auto_open=False)

# Create a standalone version with improved styling for better embedding
standalone_path = 'samsung_interactive_chart_enhanced_standalone.html'
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
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
        }}
        .chart-container {{
            width: 100%;
            height: 100vh;
            background-color: white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        .header {{
            padding: 10px;
            text-align: center;
            color: #333;
            background-color: white;
            border-bottom: 1px solid #ddd;
        }}
        .footer {{
            position: fixed;
            bottom: 0;
            width: 100%;
            padding: 10px;
            text-align: center;
            color: #666;
            background-color: white;
            border-top: 1px solid #ddd;
            font-size: 12px;
        }}
        @media print {{
            .header, .footer {{
                display: none;
            }}
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

print(f"Enhanced interactive visualization saved to {html_path} and {standalone_path}")
print("You can now embed these HTML files in your Canva presentation.")
print("Instructions for embedding in Canva:")
print("1. Upload the HTML file to a web hosting service like GitHub Pages or Netlify")
print("2. In Canva, add an 'Embed' element and paste the URL to your hosted HTML file")
print("3. Alternatively, use the 'Website' embed option in Canva and enter the URL") 