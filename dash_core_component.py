from dash import Dash, dcc, html
from numpy import true_divide
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('data_resources/gdp-life-exp-2007.csv')
# plotly figure
figure = fig = px.scatter(df, x="gdp per capita", y="life expectancy", size="population",
                          color="continent", hover_name="country", log_x=True, size_max=60)

app.layout = html.Div(children=dcc.Graph(figure=figure, id='graph_example'))


def main():
    app.run_server(debug=True)


if __name__ == '__main__':
    main()
