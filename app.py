from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
#Your task is to create a Dash app to visualise the data you generated in the last task. Lean on the resources linked below to learn more about the basics of working with Dash. Your application must incorporate the following elements:
#A header which appropriately titles the visualiser
#A line chart which visualises the sales data generated in the last task, sorted by date. Be sure to include appropriate axis labels for the chart.

# Load data
df = pd.read_csv("output.csv")
#Convert Sales into float
df["sales"] = df["sales"].replace('[\$,]', '', regex=True).astype(float)
# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")
daily_sales = df.groupby("date")["sales"].sum().reset_index()
# Create line chart
fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Sales",
    template="plotly_white"
)
fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    line_color="red",
    annotation_text="Price Increase",
    annotation_position="top right"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1(
            "Pink Morsel Sales Dashboard",
            style={"textAlign": "center"}
        ),

        dcc.Graph(
            figure=fig,
            style={"width": "90%", "margin": "auto"}
        ),
    ]
)

#Run app
if __name__ == "__main__":
      #No longer uses app run server now just uses run  
    app.run(debug=True)

