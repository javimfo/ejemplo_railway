import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output

# iniciamos app
app = dash.Dash(external_stylesheets=[dbc.themes.LUX])


app.title = 'Visor Estratégico'
server = app.server

# parte superior de la app
navbar = dbc.NavbarSimple(
    children=[
        dbc.Button("Home", outline=True, color="primary", className="mr-1", id="btn_sidebar"),
    ],
    # brand=[html.Div(
    #     [html.H6(["VISOR ESTRATÉGICO DE NIVELES DE SERVICIO"]), html.H6(["Área Big Data de Transporte"]),
    #      html.H6(["Coordinación SIT-MTT"])])],
    brand="VISOR ESTRATÉGICO DE NIVELES DE SERVICIO",
    brand_href="#",
    color="dark",
    dark=True,
    fluid=True,
)

app.layout = html.Div(
    [
        dcc.Store(id='side_click'),
        dcc.Location(id="url"),
        navbar,
    ],
)


lista_pag = ['rve', 'rutas', 'congestiones', 'od']  # , 'rve', 'eda', 'congestiones']



if __name__ == "__main__":
    app.run_server(debug=True, port=8077)
