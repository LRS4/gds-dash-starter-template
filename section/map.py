from dash import dcc
from dash import html
from app import app
from dash.dependencies import Output, Input
import plotly.express as px

df = px.data.election()  # replace with your own data source
geojson = px.data.election_geojson()

fig = px.choropleth_mapbox(
    df,
    geojson=geojson,
    color="Coderre",
    locations="district",
    featureidkey="properties.district",
    center={"lat": 45.5517, "lon": -73.7073},
    zoom=10,
    range_color=[0, 6500],
    height=700
)

fig.update_layout(
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    mapbox_style="carto-positron"
)

layout = html.Div(
    children=[
        html.H1(
            children="Avocado headlines",
            className="govuk-heading-l"
        ),
        html.P(
            children="View headline figures for"
            " number of avocados sold in the US"
            " between 2015 and 2018",
            className="govuk-body"
        ),
        dcc.RadioItems(
            id='candidate',
            options=["Joly", "Coderre", "Bergeron"],
            value="Coderre",
            inline=True
        ),
        dcc.Graph(id="map", figure=fig)
    ]
)


@app.callback(
    Output("map", "figure"),
    Input("candidate", "value"))
def display_choropleth(candidate):
    df = px.data.election()  # replace with your own data source
    geojson = px.data.election_geojson()

    fig = px.choropleth_mapbox(
        df, 
        geojson=geojson, 
        color=candidate,
        locations="district", 
        featureidkey="properties.district",
        center={"lat": 45.5517, "lon": -73.7073}, 
        zoom=10,
        range_color=[0, 6500],
        height=700
    )

    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        mapbox_style="carto-positron"
    )

    return fig
