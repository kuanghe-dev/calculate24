from dash import html, dcc
import dash_bootstrap_components as dbc

calculate24_card = dbc.Card(
    [
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
    className="mb-4 pb-2",
    color="secondary",
    outline=True,
)

acknowledgments_card = dbc.Card(
    [
        dbc.CardBody([
            dcc.Markdown('''\
#### Source Code

You can find the source code [here](https://github.com/kuanghe-dev/calculate24.git).

#### Acknowledgments

The web app's icon is made by [iconmas](https://www.flaticon.com/authors/iconmas)
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
                html.H1('24 Puzzle'),
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
