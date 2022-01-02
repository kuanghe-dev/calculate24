from dash import dcc, html
import dash_bootstrap_components as dbc

# def gen_inline_blocks(*args):
#     return html.Div(
#         [
#             html.Div([arg], style={'display': 'inline-block'}) for arg in args
#         ]
#     )

# def add_tooltip(obj, tooltip, id):
#     return gen_inline_blocks(
#         obj,
#         html.Span(
#             u"\U0001F6C8",
#             id=id,
#             style={"cursor": "pointer", "fontSize": "18px"},
#         ),
#         dbc.Tooltip(
#             tooltip,
#             target=id,
#         ),
#     )

calculate24_card = dbc.Card(
    [
        # dbc.CardHeader(
        #     "Calculate 24",
        #     style={"fontWeight": "bold"},
        # ),
        dbc.CardBody(
            [
                html.P(["Please input four integers between 1 and 9:"],
                       style={"fontWeight": "bold"}),
                dbc.Row([
                    dbc.Col(
                        html.Div(
                            [
                                dbc.Input(id="n1-input", type="number", value=6),
                                dbc.FormFeedback("Need a number between 1 and 9.", type="invalid"),
                            ],
                        ),
                        width=3,
                    ),
                    dbc.Col(
                        html.Div(
                            [
                                dbc.Input(id="n2-input", type="number", value=6),
                                dbc.FormFeedback("Need a number between 1 and 9.", type="invalid"),
                            ],
                        ),
                        width=3,
                    ),
                    dbc.Col(
                        html.Div(
                            [
                                dbc.Input(id="n3-input", type="number", value=6),
                                dbc.FormFeedback("Need a number between 1 and 9.", type="invalid"),
                            ],
                        ),
                        width=3,
                    ),
                    dbc.Col(
                        html.Div(
                            [
                                dbc.Input(id="n4-input", type="number", value=6),
                                dbc.FormFeedback("Need a number between 1 and 9.", type="invalid"),
                            ],
                        ),
                        width=3,
                    ),                    
                ], className="pb-4"),                

                dbc.Row([
                    html.P(["Results:"],
                       style={"fontWeight": "bold"}),
                    dbc.Col(
                        html.Div(id="result-output"),
                        width=12,
                    ),
                ]),
            ],
            className="pb-2",
        )
    ],
    className="mb-3",
    color="secondary",
    outline=True,
)

acknowledgments_card = dbc.Card(
    [
        dbc.CardBody([
            dcc.Markdown('''\
#### Source Code

You can find the source code [here](http://github.com/). TODO

#### Acknowledgments

This website's icon is made by [iconmas](https://www.flaticon.com/authors/iconmas)
from [Flaticon](https://www.flaticon.com).
''')
        ], className="mb-1 pb-0"),
    ],
    className="mb-4",
    color="secondary",
    outline=True,
)

layout = dbc.Container(
    [
        html.Div(
            [
                html.H1('24 Game'),
                html.P('Find ways to manipulate four integers to get 24.',
                       className='lead')
            ],
            className="page-header my-2"
        ),

        calculate24_card,
        acknowledgments_card,
    ],
    fluid=True,
    style={"width": "90%"}
)
