from dash import dcc
from dash import html
import dash_leaflet as dl
from app import app
from dash.dependencies import Output, Input

url = 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png'
attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'

layout = html.Div(
    children=[
        html.H1(
            children="Map",
            className="govuk-heading-l"
        ),
        html.P(
            children="View regional disparities for"
            " number of avocados sold in the UK"
            " between 2015 and 2018.",
            className="govuk-body"
        ),
        dl.Map(
            dl.TileLayer(
                url=url,
                attribution=attribution,
                maxZoom=10,
                minZoom=6
            ), 
            zoom=6,
            center=[54.509865, -5.118092],
            style={'width': '99%', 'height': '80vh'}
        )
    ]
)
