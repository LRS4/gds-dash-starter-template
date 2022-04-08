from dash import dcc
from dash import html
import numpy as np
import pandas as pd
from dash.dependencies import Output, Input
from utils import layout_helpers as lh
from components.mobile_navigation import mobile_navigation_bar
from section import headlines, avocado_sales, map

from app import app
from app import server

app.title = "GDS Dash Starter Template"

app.layout = html.Div(
    children=[
        html.Header(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.A(
                                    children="Dash GDS starter template",
                                    href="/",
                                    className="govuk-header__link govuk-header__link--service-name govuk-!-margin-left-3 govuk-!-margin-bottom-0"
                                )
                            ],
                            className="govuk-header__logo"
                        ),
                        html.Button(
                            children="Menu ▼",
                            id="mobile-menu-btn",
                            className="mobile-menu-button govuk-button"
                        )
                    ],
                    className="govuk-header__container"
                )
            ],
            className="govuk-header govuk-!-padding-top-0",
            role="banner",
            id="global-header",
        ),
        mobile_navigation_bar,
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


@app.callback(Output('mobile-navigation', 'style'), 
              Output('mobile-menu-btn', 'children'),
              Input('mobile-menu-btn', 'n_clicks'))
def show_or_hide_mobile_navigation(click): 
    if click == None:
       return {'display': 'none'}, "Menu ▼"
    if click % 2 != 0:
       return {'display': 'inline-block'}, "Menu ▲"
    else:
        return {'display': 'none'}, "Menu ▼"


if __name__ == "__main__":
    app.run_server(debug=True)
