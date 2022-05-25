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

# The Dash Core Components module (dash.dcc) includes a component called Graph.
# Graph renders interactive data visualizations using the open source plotly.js JavaScript graphing
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

# Dash Core Components (dash.dcc) includes a set of higher-level components like dropdowns, graphs, markdown blocks,
# and more.# Like all Dash components, they are described entirely declaratively. Every option that is configurable
# is available as a keyword argument of the component.

df = pd.read_csv('data_resources/gdp-life-exp-2007.csv')
# plotly figure
figure = fig = px.scatter(df, x="gdp per capita", y="life expectancy", size="population",
                          color="continent", hover_name="country", log_x=True, size_max=60)

layout4 = [html.Div(children=dcc.Graph(figure=figure, id='graph_example'))]

# You can view all of the available components in the Dash Core Components Gallery.
# Dropdown - single
dropdown_single = [html.Label('Dropdown'), dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal')]

# Dropdown - multiselect
dropdown_multi = [html.Br(), html.Label('Multi-Select Dropdown'),
                  dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'],
                               ['Montréal', 'San Francisco'], multi=True)]

radio_button = [html.Br(), html.Label('Radio Items'),
                dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'], 'Montréal'), html.Br()]

# we can wrap all bove in one block  (html.Div) to control the style

column1 = [html.Div(children=dropdown_single + dropdown_multi + radio_button,
                    style={'padding': 10, 'flex': 1})]

# checkbox
checkbox = [html.Br(), html.Label('Checkboxes'),
            dcc.Checklist(['New York City', 'Montréal', 'San Francisco'], ['Montréal', 'San Francisco'])]

#  Text input
text = [html.Br(), html.Label('Text Input'), dcc.Input(value='MTL', type='text')]

slider = [html.Br(), html.Div([html.Label('Slider'),
                               dcc.Slider(min=0, max=9,
                                          marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
                                          value=5)])]

column2 = [html.Div(children=checkbox + text + slider, style={'padding': 10, 'flex': 1})]

layout5 = [html.Div(children=column1 + column2, style={'display': 'flex', 'flex-direction': 'row'})]

layout = layout1 + layout2 + layout3 + layout4 + layout5

app.layout = html.Div(children=layout)
if __name__ == '__main__':
    app.run_server(debug=True)
