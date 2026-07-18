import pandas as pd
from dash import Dash, html, dcc, Input, Output
from plotly.express import line

# Load the data
data = pd.read_csv("output.csv")
data["date"] = pd.to_datetime(data["date"])

# Create the Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div(

    style={
        "backgroundColor": "#F5F5F5",
        "padding": "30px",
        "fontFamily": "Arial"
    },

    children=[

        html.H1(
            "Pink Morsel Visualizer",
            style={
                "textAlign": "center",
                "color": "#E91E63",
                "marginBottom": "30px"
            }
        ),

        dcc.RadioItems(
            id="region",

            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],

            value="all",

            inline=True,

            style={
                "textAlign": "center",
                "marginBottom": "30px"
            }
        ),

        dcc.Graph(id="sales_graph")

    ]
)


@app.callback(
    Output("sales_graph", "figure"),
    Input("region", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        df = data.copy()
    else:
        df = data[data["region"] == selected_region]

    df = (
        df.groupby("date")["sales"]
        .sum()
        .reset_index()
        .sort_values("date")
    )

    fig = line(
        df,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales - {selected_region.title()}"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales ($)"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)