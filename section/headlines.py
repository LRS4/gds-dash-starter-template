from dash import dcc
from dash import html

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
        )
    ]
)
