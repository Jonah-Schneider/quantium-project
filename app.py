from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
#Your task is to create a Dash app to visualise the data you generated in the last task. Lean on the resources linked below to learn more about the basics of working with Dash. Your application must incorporate the following elements:
#A header which appropriately titles the visualiser
#A line chart which visualises the sales data generated in the last task, sorted by date. Be sure to include appropriate axis labels for the chart.

# Load data
df = pd.read_csv("output.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)

