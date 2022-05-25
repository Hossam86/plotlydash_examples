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

#  sample datasource -- panndas frame
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# plotly express figure -- you can use any plotly figure check plotly.js docs
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# simple layout as list of html components(H1,p, ) and dash core components(plotly graph)
layout1 = [html.H1(children='Hello Dash'),
           html.Div(children='''Dash: A web application framework for your data.'''),
           dcc.Graph(id='example-graph1', figure=fig)]

# Let's customize the text in our app by modifying the inline styles of the components.
# The style property in HTML is a semicolon-separated string. In Dash, you can just supply a dictionary.
# The keys in the style dictionary are camelCased. So, instead of text-align, it's textAlign.
# The HTML class attribute is className in Dash.

colors = {'background': '#111111', 'text': '#7FDBFF'}

layout2 = [html.H1(children='Hello Dash', style={'textAlign': 'center', 'color': colors['text']}),
           html.Div(children='''Dash: A web application framework for your data.''',
                    style={'textAlign': 'center', 'color': colors['text']}),
           dcc.Graph(id='example-graph2', figure=fig)]


# one of powerful thing in dash is that we writing our html markup in Python ,
# we can create complex reusable components like tables without switching contexts or languages
# wrapping html tags in html dash commponts help us to create complex reusable components
# like tables without switching contexts or languages.

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


df = pd.read_csv('data_resources/usa-agricultural-exports-2011.csv')
layout3 = [html.H4(children='US Agriculture Exports (2011)'), generate_table(df)]

layout = layout1 + layout2 + layout3

app.layout = html.Div(children=layout)
if __name__ == '__main__':
    app.run_server(debug=True)
