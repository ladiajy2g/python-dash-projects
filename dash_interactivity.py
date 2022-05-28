# first install pandas dash
# pip install pandas dash

#import required libraries
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

#read the arline data in pandas dataframe
airline_data = pd.read_csv('airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# create a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add a html.Div and core input text component
# Finally, add graph component

app.layout = html.Div(children = [
                                html.H1(
                                    'Arline Performance Dashboard',
                                style={'textAlign': 'center', 'color': '##503D36', 'font-size': 40}
                                ),
                                html.Div([
                                    'Input Year: ', dcc.Input(id = 'input-year', value = '2010', type= 'number',
                                style={'height' : '50px', 'font-size': 35}
                                ),],
                                style = {'font-size': 40}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id= 'line-plot')),
                            ])

# add application callback decorator
@app.callback(Output(component_id = 'line-plot', component_property = 'figure'),
            Input(component_id = 'input-year', component_property = 'value'))

#add computation to call back function and return graph
def get_graph(entered_year):
    #select data based on the entered year
    df = airline_data[airline_data['Year'] == int(entered_year)]

    #group the data by Month and compute average over arrival delay time.
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()

    fig = go.Figure(data=go.Scatter(
        x = line_data['Month'], 
        y = line_data['ArrDelay'], 
        mode = 'lines', 
        marker = dict(color='green'))
        )
    fig.update_layout(title = 'Month vs Average Flight Delay Time',
    xaxis_title = 'Month', yaxis_title = 'ArrDelay')
    return fig


#run the app
if __name__ == '__main__':
    app.run_server()