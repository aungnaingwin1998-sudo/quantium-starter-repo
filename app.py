import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load processed data
df = pd.read_csv("output.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sum sales by date
sales_by_date = (
    df.groupby("date", as_index=False)["sales"]
      .sum()
      .sort_values("date")
)

# Create line chart
fig = px.line(
    sales_by_date,
    x="date",
    y="sales",
    title="Pink Morsels Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales ($)"
)

# Optional: mark the price increase date
fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    line_color="red",
    annotation_text="Price Increase"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsels Sales Before and After Price Increase"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)