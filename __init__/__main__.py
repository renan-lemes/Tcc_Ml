
# %%
from dash import Dash
from dash_html_components import Div, H1, P, H3, Br
from dash_core_components import Graph, Dropdown, Slider, Checklist
from dash_core_components import Input as DCCInput
from dash.dependencies import Input, Output

from yfinance import download
from datetime import datetime
df = download('PETR4.SA', '2021-01-01', datetime.now(),
              progress=False)
df2 = download('PETR3.SA', '2021-01-01', datetime.now(),
               progress=False)
df3 = download('PBR', '2021-01-01', datetime.now(),
               progress=False)

external_stylesheets = [
    # 'https://unpkg.com/terminal.css@0.7.2/dist/terminal.min.css'
    './assets/style.css',
]

database = {
    'index': df.index,
    'menores': df.Close,
    'maiores': df3.Close,
    'bebes': df2.Close,
}
# elemento main #
app = Dash(__name__, external_stylesheets=external_stylesheets)
# componente do dash #


app.layout = Div(
    children=[
        DCCInput(id='meu_input1', value='Potato'),
        Br(),
        DCCInput(id='meu_input2', value='Dale'),
        P(id='output1',),
        P(id='output2'),
        H1('Olá ',),
        P('Bem vindo ao dash'),
        P('Bora codar'),
        H3('Gráfico de Linha'),

        Dropdown(
            options=[
                {'label': 'Menores', 'value': 'menores'},
                {'label': 'Maiores', 'value': 'maiores'},
                {'label': 'Bebes', 'value': 'bebes'},
            ],
            value='menores'
        ),
        Slider(
            min=0,
            max=10,
            step=1,
            value=5
        ),
        Checklist(
            options=[
                {'label': 'Menores', 'value': 'menores'},
                {'label': 'Maiores', 'value': 'maiores'},
                {'label': 'Bebes', 'value': 'bebes'},
            ],
            value=['bebes'],
        ),
        Graph(
            config={'displayModeBar': False},
            figure={
                'data': [
                    {
                        'x': df.index,
                        'y': df['Close'],
                        'type': 'line',
                        'name':'Close',
                    },
                    {
                        'x': df.index,
                        'y': df['Low'],
                        'type': 'line',
                        'name':'Low',
                    },
                ],
                'layout':
                    {
                        'title': ' Gráfico de linha da PETR4',
                        'paper_bgcolor': '#222225',
                        'titlefont':
                        {
                            'size': 30,
                            'color': '#e8e9ed',
                        }
                },
            },
        )
    ]
)


@app.callback(
    [
        Output('output1', 'children'),
        Output('output2', 'children'),
    ],
    [
        Input('meu_input1', 'value'),
        Input('meu_input2', 'value'),
    ],
)
def meu_callback(meu_input1, meu_input2):
    #print(f'Callback {meu_input}')
    return meu_input1, meu_input2


app.run_server()
#debug=True faz rodar automaticamente#

# %%
