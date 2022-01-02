import os

from app import create_app
from app.layout import layout
from app.callbacks import assign_callbacks

app = create_app()

app.layout = layout
assign_callbacks(app)

if __name__ == '__main__':
    debug = bool(os.environ.get('DEBUG'))
    app.run_server(debug=debug, port=8000)

