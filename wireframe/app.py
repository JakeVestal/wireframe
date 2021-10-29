import dash
from dash import html

app = dash.Dash(__name__)
app.layout = html.Div([html.Img(src='/assets/rolling_out_loud_banner.PNG')])

if __name__ == '__main__':
    app.run_server(debug=True)
