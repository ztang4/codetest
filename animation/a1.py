import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
import json


fig = go.Figure(
    data=[go.Scatter(hoverinfo="x",hovertext="this is: ",x=[0, 1], y=[0, 1] )],
    layout=go.Layout(
        xaxis=dict(range=[0, 5], autorange=False),
        yaxis=dict(range=[0, 5], autorange=False),
        title="Start Title"
    ),
    frames=[go.Frame(data=[go.Scatter(x=[1, 2], y=[1, 2])]),
            go.Frame(data=[go.Scatter(x=[1, 4], y=[1, 4])]),
            go.Frame(data=[go.Scatter(x=[3, 4], y=[3, 4])]),
            go.Frame(data=[go.Scatter(x=[0, 5], y=[0, 5])],layout=go.Layout(title_text="End Title"))]
)

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[   
            html.Div(
                    children=[
                    dcc.Graph(figure=fig)
            ])
                            
        ]

)

if __name__ == '__main__':
    app.run_server(debug=True)