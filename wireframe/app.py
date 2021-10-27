import dash
from dash import html

app = dash.Dash(__name__)
server = app.server
app.config['suppress_callback_exceptions']=True
app.layout = html.Div([html.Img(src='/assets/rolling_out_loud_banner.png')])

if __name__ == '__main__':
    app.run_server(debug=True)
