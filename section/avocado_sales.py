from dash import dcc
from dash import html
from app import app
import numpy as np
import pandas as pd
from dash.dependencies import Output, Input
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from utils import layout_helpers as lh
import pathlib

path = pathlib.Path(__file__).parent
data_path = path.joinpath("../data").resolve()
data = pd.read_csv(data_path.joinpath("avocado.csv"))

data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)
data.set_index("Date", inplace=True)
data["YearRollingAveragePrice"] = data["AveragePrice"].rolling(window=365, min_periods=1).mean()

filtered_data = data.loc[((data.region == "Albany") & (data.type == "organic")), :]

layout = html.Div(
    children=[
        html.H1(
            children="Sales summary",
            className="govuk-heading-l"
        ),
        html.P(
            children="Analyze the behavior of avocado prices"
            " and the number of avocados sold in the US"
            " between 2015 and 2018.",
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
                                    persistence=True,
                                    persistence_type="session"
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
                                    className="dropdown",
                                    persistence=True,
                                    persistence_type="session"
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
                                    min_date_allowed=data.index.min().date(),
                                    max_date_allowed=data.index.max().date(),
                                    start_date=data.index.min().date(),
                                    end_date=data.index.max().date(),
                                    show_outside_days=False,
                                    persistence=True,
                                    persistence_type="session"
                                )
                            ],
                            className="govuk-grid-column-one-half"
                        ),
                    ],
                    className="govuk-grid-row"
                )
            ]
        ),
        dcc.Loading(
            id="loading-spinner-1",
            children=[
                dcc.Graph(
                    id="price-chart",
                    figure={
                        "data": [
                            {
                                "x": filtered_data.index,
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
                )
            ],
            type="circle",
        ),
        dcc.Loading(
            id="loading-spinner-2",
            children=[
                dcc.Graph(
                    id="volume-chart",
                    figure={
                        "data": [
                            {
                                "x": filtered_data.index,
                                "y": filtered_data["Total Volume"],
                                "type": "lines",
                            }
                        ],
                        "layout": lh.get_chart_layout({
                            "title": "Avocados Sold",
                            "colorway": ["#104F75"],
                        })
                    }
                )
            ],
            type="circle"
        )
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
        & (data.index >= start_date)
        & (data.index <= end_date)
    )
    filtered_data = data.loc[mask, :]

    price_chart_figure = make_subplots(specs=[[{"secondary_y": True}]])

    price_chart_figure.add_trace(
        go.Scatter(
            x=filtered_data.index, 
            y=filtered_data["AveragePrice"], 
            name="Price"
        ), 
        secondary_y=False,
    )

    price_chart_figure.add_trace(
        go.Scatter(
            x=filtered_data.index, 
            y=filtered_data["YearRollingAveragePrice"], 
            name="Year Rolling Average",
            line={
                "dash": "solid"
            }
        ), 
        secondary_y=False,
    )

    price_chart_figure.layout = lh.get_chart_layout({
        "title": "Average Price of Avocados",
        "title_x": 0.5,
        "yaxis": {
            "tickprefix": "$"
        },
        "colorway": ["#104F75", "#e87d1e"],
        "legend": {
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "right",
            "x": 1
        }
    })

    volume_chart_figure = {
        "data": [
            {
                "x": filtered_data.index,
                "y": filtered_data["Total Volume"],
                "type": "lines",
            },
        ],
        "layout": lh.get_chart_layout({
            "title": "Avocados Sold",
            "colorway": ["#104F75"]
        })
    }

    return price_chart_figure, volume_chart_figure
