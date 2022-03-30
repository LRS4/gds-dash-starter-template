import dash
from dash import dcc
from dash import html
import pandas as pd

data = pd.read_csv("avocado.csv")
data = data.query("type == 'conventional' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

app = dash.Dash(__name__)
app.title = "GDS Dash Starter Template"

app.layout = html.Div(
    children=[
        html.Div(
            html.H1(
                children="Avocado Analytics",
                className="govuk-heading-l"
            ),
            className="govuk-grid-column-one-third"
        ),
        html.Div(
            children=[
                html.H1(
                    children="Avocado Analytics",
                    className="govuk-heading-l"
                ),
                html.P(
                    children="Analyze the behavior of avocado prices"
                    " and the number of avocados sold in the US"
                    " between 2015 and 2018",
                    className="govuk-body"
                ),
                dcc.Graph(
                    figure={
                        "data": [
                            {
                                "x": data["Date"],
                                "y": data["AveragePrice"],
                                "type": "lines",
                            },
                        ],
                        "layout": {"title": "Average Price of Avocados"},
                    },
                ),
                dcc.Graph(
                    figure={
                        "data": [
                            {
                                "x": data["Date"],
                                "y": data["Total Volume"],
                                "type": "lines",
                            },
                        ],
                        "layout": {"title": "Avocados Sold"},
                    },
                ),
            ],
            className="govuk-grid-column-two-thirds"
        )
    ],
    className="govuk-grid-row"
)

if __name__ == "__main__":
    app.run_server(debug=True)
