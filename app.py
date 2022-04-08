import dash

app = dash.Dash(
    __name__, 
    suppress_callback_exceptions=True,
    update_title=None,
    external_stylesheets=[
        'https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'
    ],
    meta_tags=[{
        "name": "viewport",
        "content": "width=device-width, initial-scale=1.0"
    }]
)

server = app.server