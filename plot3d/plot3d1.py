import plotly.graph_objects as go
import numpy as np
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import dash

BODY_COLOR = "#8e44ad"
BODY_OUTLINE_WIDTH = 10
AXIS_ZERO_LINE_COLOR = "#ffa801"
GROUND_COLOR = "rgb(240, 240, 240)"
PAPER_BG_COLOR = "white"
LEGENDS_BG_COLOR = "rgba(255, 255, 255, 0.5)"
LEGEND_FONT_COLOR = "#34495e"

data = [
        {'color': 'rgba(244,22,100,0.6)',
              'opacity': 0.9,
              'type': 'mesh3d',
              'x': [100.0, 100.0, -100.0, -100.0, -100.0, 100.0, 100.0],
              'y': [0.0, 100.0, 100.0, 0.0, -100.0, -100.0, 0.0],
              'z': [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]
        },
        {
        "line": {"color": BODY_COLOR, "opacity": 1, "width": BODY_OUTLINE_WIDTH},
        "name": "body",
        "showlegend": True,
        "type": "scatter3d",
        "uid": "1f821e07-2c02-4a64-8ce3-61ecfe2a91b6",
        "x": [100.0, 100.0, -100.0, -100.0, -100.0, 100.0, 100.0],
        "y": [0.0, 100.0, 100.0, 0.0, -100.0, -100.0, 0.0],
        "z": [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0],
        }      
        ]



HEXAPOD_FIGURE = {
    "data": data,
    "layout": {
        "paper_bgcolor": PAPER_BG_COLOR,
         "hovermode": "closest",
        "legend": {
            "x": 0,
            "y": 0,
            "bgcolor": LEGENDS_BG_COLOR,
            "font": {"family": "courier", "size": 12, "color": LEGEND_FONT_COLOR},
        },
         "margin": {"b": 20, "l": 10, "r": 10, "t": 20},
        "scene": {
            "aspectmode": "manual",
            "aspectratio": {"x": 1, "y": 1, "z": 1},
            "camera": {
                "center": {
                    "x": 0.0348603742736399,
                    "y": 0.16963779995083,
                    "z": -0.394903376555686,
                },
                "eye": {
                    "x": 0.193913968006015,
                    "y": 0.45997575676993,
                    "z": -0.111568465000231,
                },
                "up": {"x": 0, "y": 0, "z": 1},
            },
            "xaxis": {
                "nticks": 1,
                "range": [-600, 600],
                "zerolinecolor": AXIS_ZERO_LINE_COLOR,
                "showbackground": False,
            },
            "yaxis": {
                "nticks": 1,
                "range": [-600, 600],
                "zerolinecolor": AXIS_ZERO_LINE_COLOR,
                "showbackground": False,
            }
         }
    }
}
# HEXAPOD_FIGURE = {
#     "data": data,
#     'layout': {'template': '...'}
# }
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[   
            html.Div(className='eight columns div-for-charts bg-grey',
                    children=[
                    dcc.Graph(id='timeseries', figure=HEXAPOD_FIGURE)
            ])
                            
        ]

)


if __name__ == '__main__':
    app.run_server(debug=True)