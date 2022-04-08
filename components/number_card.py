from dash import dcc
from dash import html

def number_card(caption: str, title: str, description: str, number: str) -> html.Div:
    """
    Generates a GOV.UK number card
    """
    return html.Div(
        children=[
            html.Strong(
                children=caption,
                className="govuk-caption-m govuk-!-font-weight-regular"
            ),
            html.H4(
                children=title,
                className="govuk-heading-m title-mobile govuk-!-margin-bottom-0"
            ),
            html.Strong(
                children=description,
                className="govuk-body-s float govuk-!-margin-top-3 govuk-!-margin-bottom-0"
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            number,
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
