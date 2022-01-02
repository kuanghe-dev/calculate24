from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from .calculate24 import Calculate24

INPUT_PARAM_RANGE = {
    'n1-input': [1, 9],
    'n2-input': [1, 9],
    'n3-input': [1, 9],
    'n4-input': [1, 9],
}

def validate_param(param, param_range):
    """Validate input value 'param' against a range 'param_range'

    The range might have one or more np.inf indicating no low-end or high-end
    limit.

    Return: a bool indicating whether validation is successful and a string
    message with possible error.

    Example:

    - input: 'x', [1, 10]
    - output: (False, 'Input needs to be a number')

    - input: '3', [1, 10]
    - output: (True, '')
    """

    try:
        value = int(param)
    except:
        return False

    return param_range[0] <= value <= param_range[1]

def assign_callbacks(app):
    for param in INPUT_PARAM_RANGE:
        @app.callback(
            Output(f'{param}', 'invalid'),
            Input(f'{param}', 'value'),
            State(f'{param}', 'id'),
        )
        def check_param_validity(value, id):
            valid = validate_param(value, INPUT_PARAM_RANGE[id])
            return not valid

    @app.callback(
        Output('result-output', 'children'),
        [
            Input('n1-input', 'value'),
            Input('n2-input', 'value'),
            Input('n3-input', 'value'),
            Input('n4-input', 'value'),
        ]
    )
    def calculate24(n1, n2, n3, n4):
        inputs = [n1, n2, n3, n4]

        for i in range(4):
            id = f'n{i+1}-input'
            if not validate_param(inputs[i], INPUT_PARAM_RANGE[id]):
                return dbc.Alert('Please check input values.', color="danger", className="mb-0")

        results = Calculate24(inputs).run()
        if results:
            text = '\n'.join(results)
        else:
            text = f'No results found for {n1}, {n2}, {n3}, and {n4}.'

        markdown = f"""\
```cpp
{text}
```
"""
        return dcc.Markdown(markdown, className="px-4")



