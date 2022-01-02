import dash
import dash_bootstrap_components as dbc

def create_app():
    app = dash.Dash(
        __name__,
        title='24 Puzzle',
        meta_tags=[{"name": "viewport", "content": "width=device-width"}],
        update_title=None,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
    )

    return app
