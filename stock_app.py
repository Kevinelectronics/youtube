import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import yfinance as yf
import os

# Load environment variables from .env file

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Interactive Stock Price Dashboard"

# Define the layout of the app
app.layout = html.Div([
    html.H1("Stock Price Dashboard"),
    dcc.Dropdown(
        id='stock-dropdown',
        options=[
            {'label': 'Apple', 'value': 'AAPL'},
            {'label': 'Google', 'value': 'GOOGL'},
            {'label': 'Amazon', 'value': 'AMZN'}
        ],
        value='AAPL'  # Default value
    ),
    dcc.Graph(id='stock-graph')
])

# Define the callback to update the graph
@app.callback(
    Output('stock-graph', 'figure'),
    Input('stock-dropdown', 'value')
)
def update_graph(selected_stock):
    # Download stock data
    df = yf.download(selected_stock, start="2020-01-01", end="2021-01-01")
    
    # Create the figure
    fig = {
        'data': [{'x': df.index, 'y': df['Close'], 'type': 'line', 'name': selected_stock}],
        'layout': {'title': f'Stock Prices of {selected_stock}'}
    }
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
