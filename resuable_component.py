from unicodedata import name
from dash import Dash, html, dcc
import pandas as pd

df = pd.read_csv('data_resources/usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=10):
    # table head
    head = html.Tr([html.Th(col) for col in dataframe.columns])
    table_head = html.Thead(head)

    # table body - matrix
    body = [html.Tr([html.Td(dataframe.iloc[i][col]) for col in dataframe.columns])
            for i in range(min(len(dataframe), max_rows))]
    table_body = html.Tbody(body)

    table = html.Table(children=[table_head, table_body])
    return table


app = Dash(__name__)
table = generate_table(df)
app.layout = html.Div(
    children=[html.H4('US Agriculture Exports (2011)'), table])


def main():
    app.run_server(debug=True)


if __name__ == '__main__':
    main()
