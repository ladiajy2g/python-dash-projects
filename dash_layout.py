import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

# add dataframe
# Add Dataframe
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "NYC", "MTL", "NYC"]
})

# add a bar graph figure
fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')


app = dash.Dash()
app.layout = html.Div(children = [
    html.H1(
        children = 'Dashboard',
        style = {
            'textAlign' : 'center'
        }
    ),
    #create dropdown graph
    dcc.Dropdown(options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC' # Providing a vallue to dropdown
    ),

    #bar graph
    dcc.Graph(id='example-graph-2', figure=fig)

])


#run application
if __name__ == '__main__' :
    app.run_server()

