
from statistics import mode
from tokenize import group
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = pd.DataFrame(
    {"Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
     "Amount": [4, 1, 2, 2, 4, 5],
     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]})

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
style = {'background': colors['background'],
         'textAlign': 'center',
         'color': colors['text']}

barplot_graph_c = dcc.Graph(id='exaple_barplot', figure=fig)

barplot_title_c = html.H1(children="Hello Dash!", style=style)
barplot_subtitle_c = html.Div(
    children="Dash: A web application framework for your data.")


app.layout = html.Div(
    children=[barplot_title_c, barplot_subtitle_c, barplot_graph_c], style=style)


def main():
    app.run_server(debug=True)


if __name__ == '__main__':
    main()
