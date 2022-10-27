from dash import dcc
from dash import html

def number_card(caption: str, 
    title: str, 
    description: str, 
    number: str, 
    tooltip_text: str,
    change_tag_label: str = None,
    change_tag_type: str = None,
    change_tag_arrow_direction: str = None,
    change_tag_tooltip_text:str = None) -> html.Div:
    """
    Generates a GOV.UK number card

    Args:   
        title: The title of the card i.e. Cases
        description: The description of the card i.e. People tested positive
        number: The metric to display i.e. 361,774
        tooltip_text: The text to appear in the tooltip i.e. Total number of people tested positive
        change_tag_label: The text to display in the change tags (optional)
        change_tag_type: "good" for a positive change green tag and "bad" for negative change red tag (optional)
        change_tag_arrow_direction: "increase" or "decrease" (optional)
    """
    return html.Div(
        children=[
            html.Strong(
                children=caption,
                className="govuk-caption-m govuk-!-font-weight-regular"
            ),
            html.H4(
                children=title,
                className="govuk-heading-m title-mobile govuk-!-margin-bottom-2 govuk-!-margin-top-2"
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
                                children=tooltip_text,
                                className="tooltiptext govuk-!-font-size-16"
                            )
                        ],
                        className="tooltip tooltip-dashed"
                    )
                ],
                className="govuk-heading-m govuk-!-margin-bottom-0 govuk-!-padding-top-0"
            ),
            change_tag(
                change_tag_label,
                change_tag_type,
                change_tag_arrow_direction,
                change_tag_tooltip_text
            )
        ],
        className="card-container"
    )


def change_tag(change_tag_label: str,
               change_tag_type: str,
               change_tag_arrow_direction: str,
               change_tag_tooltip_text: str) -> html.Div:
    """
    Generates a GOV.UK tag to represent a increase or decrease change.
    
    Returns:
        Blank label for spacing if no values given
        Html.Div with a change tag if values given
    """
    if change_tag_label is None:
        return html.Div(
            children=[
                html.B(
                    children=[
                        html.Span(
                            children=("label")
                        )
                    ],
                    className="govuk-tag number govuk-!-margin-top-4 change-box"
                )
            ],
            style={"visibility": "hidden"}
        )

    return html.Div(
        children=[
            html.B(
                children=[
                    html.Span(
                        children=("▼ " if change_tag_arrow_direction == "decrease" else "▲ ") +
                        change_tag_label
                    )
                ],
                className="govuk-tag number govuk-!-margin-top-4 change-box" +
                (" good" if change_tag_type == "good" else " bad")
            ),
            html.Span(
                children=change_tag_tooltip_text,
                className="tooltiptext govuk-!-font-size-16"
            )
        ],
        className = "tooltip"
    )

