from dash import dcc
from dash import html
import dash_leaflet as dl
import dash_leaflet.express as dlx
from app import app
from dash.dependencies import Output, Input
from dash_extensions.javascript import arrow_function, assign

basemap_url = 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png'
attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'

def get_info(feature=None):
    header = [html.H4("Avocado Sales Volumes")]
    if not feature:
        return header + [html.P("Hover over a Local Authority District")]
    return header + [
        html.B(feature["properties"]["LAD21NM"]), 
        html.Br(),
        "{:.3f} avocados sold".format(feature["properties"]["density"])
    ]

classes = [0, 10000, 20000, 30000, 40000, 50000]
colorscale = ['#cfdce3', '#9fb9c8', '#7095ac', '#407291', '#104f75']
style = dict(
    weight=2, 
    opacity=1, 
    color='white', 
    dashArray='3', 
    fillOpacity=0.7
)

# Create colorbar.
categories = ["{}+".format(
    cls, 
    classes[i + 1]) for i, cls in enumerate(classes[:-1])] + \
    ["{}+".format(classes[-1]
)]

colorbar = dlx.categorical_colorbar(
    categories=categories, 
    colorscale=colorscale, 
    width=350, 
    height=30, 
    position="bottomleft"
)

# GeoJSON rendering logic, must be JavaScript as it is executed in clientside.
style_handle = assign("""function(feature, context){
    const {classes, colorscale, style, colorProp} = context.props.hideout;  // get props from hideout
    const value = feature.properties[colorProp];  // get value the determines the color
    for (let i = 0; i < classes.length; ++i) {
        if (value > classes[i]) {
            style.fillColor = colorscale[i];  // set the fill color according to the class
        }
    }
    return style;
}""")

geojson = dl.GeoJSON(
    url="../assets/json/LAD_DEC_2021_GB_BFC.json",  # url to geojson file
    options=dict(style=style_handle),  # how to style each polygon
    zoomToBounds=True,  # when true, zooms to bounds when data changes (e.g. on load)
    zoomToBoundsOnClick=True,  # when true, zooms to bounds of feature (e.g. polygon) on click
    hoverStyle=arrow_function(dict(weight=5, color='#666', dashArray='')),  # style applied on hover
    hideout=dict(colorscale=colorscale, classes=classes, style=style, colorProp="density"),
    id="geojson"
)

info = html.Div(
    children=get_info(), 
    id="info", 
    className="info",
    style={"position": "absolute", "top": "10px", "right": "10px", "zIndex": "1000"}
)

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
            children=[
                dl.TileLayer(
                    url=basemap_url,
                    attribution=attribution,
                    maxZoom=10,
                    minZoom=6
                ), 
                geojson, 
                colorbar, 
                info
            ],
            zoom=6,
            center=[54.509865, -5.118092],
            style={'width': '99%', 'height': '82vh'}
        )
    ],
    id="map"
)

@app.callback(Output("info", "children"), [Input("geojson", "hover_feature")])
def info_hover(feature):
    return get_info(feature)
