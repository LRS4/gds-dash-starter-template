from dash import dcc
from dash import html
import numpy as np
import pandas as pd
from dash.dependencies import Output, Input
from utils import layout_helpers as lh
from section import headlines, avocado_sales, map

from app import app
from app import server

app.title = "GDS Dash Starter Template"

app.layout = html.Div(
    children=[
        dcc.Markdown('''
            <header role="banner" id="global-header" class="govuk-header govuk-!-padding-top-0" data-module="govuk-header" style="border-bottom:10px solid #1d70b8; margin-top: 0px;">
                <div class="govuk-header__container">
                    <div class="govuk-header__logo">
                        <a href="/" class="govuk-header__link govuk-header__link--service-name govuk-!-margin-left-3 govuk-!-margin-bottom-0">
                            Dash GDS starter template
                        </a>
                    </div>
                    <button class="mobile-menu-button govuk-button" id="mobile-menu-btn">Menu ▼</button>
                </div>
            </header>
        ''', dangerously_allow_html=True),
        html.P(
            children="Last updated on Wednesday, 30 March 2022 at 4:00pm",
            className="govuk-body-s govuk-!-margin-left-4 govuk-!-margin-top-4 govuk-!-margin-bottom-0"
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.Div(
                                            children=[
                                                html.Ul(
                                                    children=[
                                                        html.Li(
                                                            id="home-nav-item",
                                                            children=[
                                                                dcc.Link(
                                                                    children="Headlines",
                                                                    href="/section/home",
                                                                    className="govuk-link"
                                                                )
                                                            ],
                                                            className="moj-side-navigation__item moj-side-navigation__item--active"
                                                        ),
                                                        html.Li(
                                                            id="avocado_sales-nav-item",
                                                            children=[
                                                                dcc.Link(
                                                                    children="Sales",
                                                                    href="/section/avocado_sales",
                                                                    className="govuk-link"
                                                                )
                                                            ],
                                                            className="moj-side-navigation__item"
                                                        ),
                                                        html.Li(
                                                            id="map-nav-item",
                                                            children=[
                                                                dcc.Link(
                                                                    children="Map",
                                                                    href="/section/map",
                                                                    className="govuk-link"
                                                                )
                                                            ],
                                                            className="moj-side-navigation__item"
                                                        )
                                                    ],
                                                    className="moj-side-navigation__list"
                                                )
                                            ],
                                            className="moj-side-navigation govuk-!-padding-right-4"
                                        )
                                    ],
                                    className="dashboard-menu"
                                )
                            ],
                            className="dashboard-menu"
                        ),
                        dcc.Location(
                            id="url",
                            refresh=False,
                            pathname=""
                        ),
                        html.Div(
                            id="page-content",
                            children=[
                                # Dynamic page content
                            ],
                            className=""
                        )
                    ],
                    className="dashboard-container"
                ),
            ],
            className="govuk-main-wrapper"
        )
    ],
    className="govuk-template__body"
)


@app.callback(Output(component_id="page-content", component_property="children"),
    [
      Input(component_id="url", component_property="pathname")
    ],
)
def display_page(pathname):
    if pathname == "/section/home":
        return headlines.layout

    if pathname == "/section/avocado_sales":
        return avocado_sales.layout

    if pathname == "/section/map":
        return map.layout

    return headlines.layout


@app.callback(Output(component_id="home-nav-item", component_property="className"),
    [
      Input(component_id="url", component_property="pathname")
    ],
)
def update_active_nav_link(pathname):
    if pathname == "/section/home" or pathname == "" or pathname == None:
        return "moj-side-navigation__item moj-side-navigation__item--active"
    else:
        return "moj-side-navigation__item moj-side-navigation"


@app.callback(Output(component_id="avocado_sales-nav-item", component_property="className"),
    [
      Input(component_id="url", component_property="pathname")
    ],
)
def update_active_nav_link(pathname):
    if pathname == "/section/avocado_sales":
        return "moj-side-navigation__item moj-side-navigation__item--active"
    else:
        return "moj-side-navigation__item moj-side-navigation"


@app.callback(Output(component_id="map-nav-item", component_property="className"),
              [
    Input(component_id="url", component_property="pathname")
],
)
def update_active_nav_link(pathname):
    if pathname == "/section/map":
        return "moj-side-navigation__item moj-side-navigation__item--active"
    else:
        return "moj-side-navigation__item moj-side-navigation"


if __name__ == "__main__":
    app.run_server(debug=True)
