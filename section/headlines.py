from dash import dcc
from dash import html
from components.number_card import number_card

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
                            caption="Cases",
                            title="People tested positive",
                            description="Last 7 days",
                            number="361,774",
                            tooltip_text="Total number of people tested positive reported in the last 7 days (1 April 2022 - 7 April 2022)",
                            change_tag_label="-32.4%",
                            change_tag_type="good",
                            change_tag_arrow_direction="decrease",
                            change_tag_tooltip_text="Change from previous return"
                        )
                    ],
                    className="govuk-grid-column-one-third"
                ),
                html.Div(
                    children=[
                        number_card(
                            caption="Test 2",
                            title="People tested positive",
                            description="Last 7 days",
                            number="361,774",
                            tooltip_text="Total number of people tested positive reported in the last 7 days (1 April 2022 - 7 April 2022)",
                            change_tag_label="+32.4%",
                            change_tag_type="bad",
                            change_tag_arrow_direction="increase",
                            change_tag_tooltip_text="Change from previous return"
                        )
                    ],
                    className="govuk-grid-column-one-third",
                ),
                html.Div(
                    children=[
                        number_card(
                            caption="Test 3",
                            title="People tested positive",
                            description="Last 7 days",
                            number="361,774",
                            tooltip_text="Total number of people tested positive reported in the last 7 days (1 April 2022 - 7 April 2022)"
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
                            caption="Test 3",
                            title="People tested positive",
                            description="Last 7 days",
                            number="361,774",
                            tooltip_text="Total number of people tested positive reported in the last 7 days (1 April 2022 - 7 April 2022)"
                        )
                    ],
                    className="govuk-grid-column-one-third"
                ),
                html.Div(
                    children=[
                        number_card(
                            caption="Test 3",
                            title="People tested positive",
                            description="Last 7 days",
                            number="361,774",
                            tooltip_text="Total number of people tested positive reported in the last 7 days (1 April 2022 - 7 April 2022)"
                        )
                    ],
                    className="govuk-grid-column-one-third"
                ),
                html.Div(
                    children=[
                        number_card(
                            caption="Test 3",
                            title="People tested positive",
                            description="Last 7 days",
                            number="361,774",
                            tooltip_text="test"
                        )
                    ],
                    className="govuk-grid-column-one-third"
                )
            ],
            className="govuk-grid-row govuk-!-margin-top-5"
        )
    ]
)
