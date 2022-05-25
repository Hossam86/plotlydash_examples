
from dash import Dash, html, dcc
#  interface for plotly express
import plotly.express as px
import pandas as pd

# Dash application is composed of two parts. The first part is the application layout,
# and it describes what the application looks like.

# The second part is the application interactivity through callback functions.  Automatic called functions
# by dash app whenever input components' property changes to update some property in another component.

# Dash: class for dash application
# html : HTML components modules provides interface classes for every html tag
# dcc  : Dash Core Components module contains higher-level components that are interactive and are generated
#           with JavaScript, HTML, and CSS through the React.js library.

#  Application instance from Dash class
app = Dash(__name__)

#  sample data source - pandas dataframe
df = pd.DataFrame(
    {"Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
     "Amount": [4, 1, 2, 2, 4, 5],
     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]})

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

#  dash built on react.js and ploty.js , so we can use plolty graph directly through dash core interface
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
