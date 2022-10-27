import math
from dash import dcc
from dash import html
import numpy as np
import pandas as pd
import pathlib
from components.number_card import number_card

path = pathlib.Path(__file__).parent
data_path = path.joinpath("../data").resolve()
data = pd.read_csv(data_path.joinpath("avocado.csv"))
data["Date"] = pd.to_datetime(data["Date"])

end_price = data["AveragePrice"].head(1).values[0]
start_price = data["AveragePrice"].tail(1).values[0]

data_excluding_big_regions = \
    data[~data["region"].isin(
        ["TotalUS", "West", "Southeast", "Northeast", "SouthCentral"])]

top_sales_region = data_excluding_big_regions[["region", "Total Volume"]] \
    .groupby("region") \
    .sum() \
    .sort_values(by="Total Volume") \
    .tail(1)

bottom_sales_region = data_excluding_big_regions[["region", "Total Volume"]] \
    .groupby("region") \
    .sum() \
    .sort_values(by="Total Volume") \
    .head(1)

top_sales_type = data_excluding_big_regions[["type", "Total Volume"]] \
    .groupby("type") \
    .sum() \
    .sort_values(by="Total Volume") \
    .tail(1)

bottom_sales_type = data_excluding_big_regions[["type", "Total Volume"]] \
    .groupby("type") \
    .sum() \
    .sort_values(by="Total Volume") \
    .head(1)

headlines = {
    "average_price": round(data["AveragePrice"].mean(), 2),
    "average_price_change": round(((end_price - start_price) / start_price) * 100, 2),
    "total_avocados_sold": f'{math.floor(data["Total Volume"].sum()):,}',
    "region_with_highest_sales": top_sales_region,
    "type_with_highest_sales": top_sales_type,
    "region_with_lowest_sales": bottom_sales_region,
    "type_with_lowest_sales": bottom_sales_type
}

layout = html.Div(
    children=[
        html.H1(
            children="Headlines",
            className="govuk-heading-l"
        ),
        html.P(
            children="View headline figures for"
            " number of avocados sold in the US"
            " between 2015 and 2018.",
            className="govuk-body"
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        number_card(
                            caption="Price",
                            title="Average price",
                            description="All time",
                            number="$" + str(headlines["average_price"]),
                            tooltip_text="Total number of people tested positive reported in the last 7 days (1 April 2022 - 7 April 2022)",
                            change_tag_label=str(headlines["average_price_change"]) + "%",
                            change_tag_type="bad",
                            change_tag_arrow_direction="decrease",
                            change_tag_tooltip_text="Change in price from 2015 to now"
                        )
                    ],
                    className="govuk-grid-column-one-third"
                ),
                html.Div(
                    children=[
                        number_card(
                            caption="Volume",
                            title="Total sold",
                            description="All time",
                            number=headlines["total_avocados_sold"],
                            tooltip_text="Total sales made between 2015 and 2018",
                            change_tag_label="+32.4%",
                            change_tag_type="bad",
                            change_tag_arrow_direction="increase",
                            change_tag_tooltip_text="Change from previous year (dummy figure)"
                        )
                    ],
                    className="govuk-grid-column-one-third",
                ),
                html.Div(
                    children=[
                        number_card(
                            caption="Region",
                            title="Top sales region",
                            description=headlines["region_with_highest_sales"].index,
                            number=f'{int(headlines["region_with_highest_sales"].values[0][0]):,}',
                            tooltip_text="Total sales made in the top sales region",
                            change_tag_label="+32.4%",
                            change_tag_type="good",
                            change_tag_arrow_direction="increase",
                            change_tag_tooltip_text="Change from previous year (dummy figure)"
                        )
                    ],
                    className="govuk-grid-column-one-third"
                )
            ],
            className="govuk-grid-row"
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        number_card(
                            caption="Type",
                            title="Top sales type",
                            description=headlines["type_with_highest_sales"].index,
                            number=f'{int(headlines["type_with_highest_sales"].values[0][0]):,}',
                            tooltip_text="Total sales made by the top sales type"
                        )
                    ],
                    className="govuk-grid-column-one-third"
                ),
                html.Div(
                    children=[
                        number_card(
                            caption="Region",
                            title="Bottom sales region",
                            description=headlines["region_with_lowest_sales"].index,
                            number=f'{int(headlines["region_with_lowest_sales"].values[0][0]):,}',
                            tooltip_text="Total sales made by the bottom sales region"
                        )
                    ],
                    className="govuk-grid-column-one-third"
                ),
                html.Div(
                    children=[
                        number_card(
                            caption="Type",
                            title="Bottom sales type",
                            description=headlines["type_with_lowest_sales"].index,
                            number=f'{int(headlines["type_with_lowest_sales"].values[0][0]):,}',
                            tooltip_text="Total sales made by the bottom sales type"
                        )
                    ],
                    className="govuk-grid-column-one-third"
                )
            ],
            className="govuk-grid-row govuk-!-margin-top-5"
        )
    ]
)
