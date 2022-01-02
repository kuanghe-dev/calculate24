import dash
import os

from app import create_app
from app.layout import layout
from app.callbacks import assign_callbacks

app = create_app()

app.layout = layout
assign_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
    #debug = bool(os.environ.get('DEBUG'), port=8000)

