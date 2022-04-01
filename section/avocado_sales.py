from dash import dcc
from dash import html
from app import app
import numpy as np
import pandas as pd
from dash.dependencies import Output, Input
from utils import layout_helpers as lh
import pathlib

path = pathlib.Path(__file__).parent
data_path = path.joinpath("../data").resolve()
data = pd.read_csv(data_path.joinpath("avocado.csv"))

data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

app.title = "test"

layout = html.Div(
    children=[
        html.H1(
            children="Avocado sales summary",
            className="govuk-heading-l"
        ),
        html.P(
            children="Analyze the behavior of avocado prices"
            " and the number of avocados sold in the US"
            " between 2015 and 2018",
            className="govuk-body"
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Label(
                                    children="Region",
                                    className="govuk-label"
                                ),
                                dcc.Dropdown(
                                    id="region-filter",
                                    options=[
                                        {"label": region,
                                         "value": region}
                                        for region in np.sort(data.region.unique())
                                    ],
                                    value="Albany",
                                    searchable=True,
                                    clearable=False,
                                    className="dropdown",
                                ),
                            ],
                            className="govuk-grid-column-one-quarter"
                        ),
                        html.Div(
                            children=[
                                html.Label(
                                    children="Type",
                                    className="govuk-label"
                                ),
                                dcc.Dropdown(
                                    id="type-filter",
                                    options=[
                                        {"label": avocado_type,
                                         "value": avocado_type}
                                        for avocado_type in data.type.unique()
                                    ],
                                    value="organic",
                                    clearable=False,
                                    searchable=False,
                                    className="dropdown"
                                ),
                            ],
                            className="govuk-grid-column-one-quarter"
                        ),
                        html.Div(
                            children=[
                                html.Label(
                                    children="Date Range",
                                    className="govuk-label"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data.Date.min().date(),
                                    max_date_allowed=data.Date.max().date(),
                                    start_date=data.Date.min().date(),
                                    end_date=data.Date.max().date(),
                                    show_outside_days=False
                                )
                            ],
                            className="govuk-grid-column-one-half"
                        ),
                    ],
                    className="govuk-grid-row"
                )
            ]
        ),
        dcc.Graph(
            id="price-chart",
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                        "type": "lines",
                    },
                ],
                "layout": lh.get_chart_layout({
                    "title": "Average Price of Avocados"
                })
            }
        ),
        dcc.Graph(
            id="volume-chart",
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "lines",
                    },
                ],
                "layout": lh.get_chart_layout({
                    "title": "Avocados Sold"
                }),
            }
        ),
    ]
)

@app.callback(
    [Output("price-chart", "figure"), Output("volume-chart", "figure")],
    [
        Input("region-filter", "value"),
        Input("type-filter", "value"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
    ],
)
def update_charts(region, avocado_type, start_date, end_date):
    mask = (
        (data.region == region)
        & (data.type == avocado_type)
        & (data.Date >= start_date)
        & (data.Date <= end_date)
    )
    filtered_data = data.loc[mask, :]
    price_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["AveragePrice"],
                "type": "lines",
                "hovertemplate": "$%{y:.2f}<extra></extra>",
            },
        ],
        "layout": lh.get_chart_layout({
            "title": "Average Price of Avocados",
            "yaxis": {
                "tickprefix": "$"
            },
            "colorway": ["#104F75"]
        })
    }

    volume_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["Total Volume"],
                "type": "lines",
            },
        ],
        "layout": lh.get_chart_layout({
            "title": "Avocados Sold",
            "colorway": ["#104F75"],
        })
    }

    return price_chart_figure, volume_chart_figure