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
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Strong(
                                    children="Cases",
                                    className="govuk-caption-m govuk-!-font-weight-regular"
                                ),
                                html.H4(
                                    children="People tested positive",
                                    className="govuk-heading-m title-mobile govuk-!-margin-bottom-0"
                                ),
                                html.Strong(
                                    children="Last 7 days",
                                    className="govuk-body-s float govuk-!-margin-top-3 govuk-!-margin-bottom-0"
                                ),
                                html.Div(
                                    children=[
                                        html.Div(
                                            children=[
                                                "361,774",
                                                html.Span(
                                                    children="Total number of people tested positive reported in the last 7 days (1 April 2022 - 7 April 2022)",
                                                    className="tooltiptext govuk-!-font-size-16"
                                                )
                                            ],
                                            className="tooltip"
                                        )
                                    ],
                                    className="govuk-heading-m govuk-!-margin-bottom-0 govuk-!-padding-top-0"
                                )
                            ],
                            className="card-container"
                        )
                    ],
                    className="govuk-grid-column-one-third"
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Strong(
                                    children="Cases",
                                    className="govuk-caption-m govuk-!-font-weight-regular"
                                ),
                                html.H4(
                                    children="People tested positive",
                                    className="govuk-heading-m title-mobile govuk-!-margin-bottom-0"
                                ),
                                html.Strong(
                                    children="Last 7 days",
                                    className="govuk-body-s float govuk-!-margin-top-3 govuk-!-margin-bottom-0"
                                ),
                                html.Div(
                                    children=[
                                        html.Div(
                                            children=[
                                                "361,774",
                                                html.Span(
                                                    children="Total number of people tested positive reported in the last 7 days (1 April 2022 - 7 April 2022)",
                                                    className="tooltiptext govuk-!-font-size-16"
                                                )
                                            ],
                                            className="tooltip"
                                        )
                                    ],
                                    className="govuk-heading-m govuk-!-margin-bottom-0 govuk-!-padding-top-0"
                                )
                            ],
                            className="card-container"
                        )
                    ],
                    className="govuk-grid-column-one-third",
                ),
                html.Div(
                    children=[
                        "test"
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
                        "test"
                    ],
                    className="govuk-grid-column-one-third"
                ),
                html.Div(
                    children=[
                        "test"
                    ],
                    className="govuk-grid-column-one-third"
                ),
                html.Div(
                    children=[
                        "test"
                    ],
                    className="govuk-grid-column-one-third"
                )
            ],
            className="govuk-grid-row govuk-!-margin-top-5"
        )
    ]
)
