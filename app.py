import dash
import dash_core_components as dcc 
import dash_html_components as html  
import pandas as pd  
import plotly.graph_objs as go  
from dash.dependencies import Input, Output
from categoryplot import dfTips, getPlot
from histogramplot import gethist


# # the layout/content
# app.layout=html.Div(children=[
#     html.H1(children='Welcome To Purwadhika!'),
#     html.H2(children='Hello'),
#     html.H3(children='hehehe'),
#     html.P(children='Welcome To Purwadhika woi')
# ])


app = dash.Dash() # make python obj with dash() method
#obj = obj.method
color_set = ['#ff3fd8','#4290ff']

app.title='Purwadhika Dash Plotly' # set web title


#function to generate HTML Table
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col,className='table_dataset') for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col],className='table_dataset') for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))], # membutuhkan min agar tidak out of index ketika max_rows > panjang data frame
        className='table_dataset' # agar menggunakan style di assets sesuai dengan class nya
    )

# the layout/content
app.layout = html.Div(children=[
    dcc.Tabs(id="tabs", value='tab-1',children=[ #value pada tabs artinya default tab yang terbuka saat pertama loading
        dcc.Tab(label='Tips Data Set', value='tab-1', children=[
            html.Div([
                html.H1('Tips Data Set'),
                generate_table(dfTips)
            ])
        ]),
        dcc.Tab(label='Scatter plot', value='tab-2', children=[
            html.Div([
                html.H1(
                    children='Scater Plot Tips Data Set'
                ),
                dcc.Graph(
                    id='scatterplot',
                    figure={
                        'data': [
                            go.Scatter(
                                x=dfTips[dfTips['sex'] == col]['total_bill'], 
                                y=dfTips[dfTips['sex'] == col]['tip'], 
                                mode='markers', 
                                # line=dict(color=color_set[i], width=1, dash='dash'), 
                                marker=dict(color=color_set[i], size=10, line={'width': 0.5, 'color': 'white'}), name=col) #line untuk kasih border tiap markernya agar ketika numpuk akan terlihat bedanya
                            for col,i in zip(dfTips['sex'].unique(),range(len(color_set))) #karena di plotly tidak bisa pakai hue loop pertama hanya go.scatter yang female saja, lalu baru go.scatter yang malenya
                        ],
                        'layout': go.Layout(
                            xaxis={'title': 'Total Bill'},
                            yaxis={'title': 'Tip'},
                            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                            hovermode='closest'
                        )
                    }
                )     
            ])
        ]),
        dcc.Tab(label='Categorical plot', value='tab-3', children=[
            html.Div([
                html.H1(
                    children='Categorical Plot Tips Data Set'
                ),
                html.Table([
                    html.Tr([
                        html.Td([
                            html.P('Jenis :'),
                            dcc.Dropdown(
                            id='ddl-jenis-plot-categorical',
                            options=[{'label': 'Bar', 'value': 'bar'},
                            {'label': 'Violin', 'value': 'violin'},
                            {'label': 'Box', 'value': 'box'}],
                            value='bar'
                             )
                        ]),
                        html.Td([
                            html.P('X Axis :'),
                            dcc.Dropdown(
                            id='ddl-x-plot-categorical',
                            options=[{'label': 'Smoker', 'value': 'smoker'},
                                    {'label': 'Sex', 'value': 'sex'},
                                    {'label': 'Day', 'value': 'day'},
                                    {'label': 'Time', 'value': 'time'}],
                            value='sex'
                             )
                        ])
                    ])
                ],style={'width':'700px','margin':'0 auto'}), 
                dcc.Graph(
                    id='categoricalPlot',
                    figure={}
                )     
            ])
        ]),
        dcc.Tab(label='Histogram Plot',value = 'tab-4',children=[
            html.Div([
                html.H1('Histogram Plot Tips Data Set'),
                html.Table([
                    html.Tr([
                        html.Td([
                            html.P('X axis :'),
                            dcc.Dropdown(
                                id='ddl-x-plot-histogram',
                                options=[{'label': 'Total Bill', 'value': 'total_bill'},
                                    {'label': 'Tip', 'value': 'tip'}],
                                    value='tip'
                            )
                        ]),
                        html.Td([
                            html.P('Sub Plot :'),
                            dcc.Dropdown(
                                id='ddl-sub-plot-histogram',
                                options=[{'label': 'Smoker', 'value': 'smoker'},
                                    {'label': 'Sex', 'value': 'sex'},
                                    {'label': 'Day', 'value': 'day'},
                                    {'label': 'Time', 'value': 'time'}],
                                    value='day'
                            )
                        ])
                    ])
                ], style={'width':'700px','margin':'0 auto'}),
                html.Div('',id='divH4hist'),
                dcc.Graph(
                    id='histogramPlot',
                    figure={}
                )
            ])
        ])
    ],
    style={
        'fontFamily':'system-ui'
    },
    content_style={
        'fontFamily':'Arial',
        'borderLeft':'1px solid #d6d6d6',
        'borderRight':'1px solid #d6d6d6',
        'borderBottom':'1px solid #d6d6d6',
        'padding':'44px'
    })
],
style={
    'maxWidth':'1000px',
    'margin':'0 auto'
}
)
@app.callback(
    Output(component_id='categoricalPlot', component_property='figure'),
    [Input(component_id='ddl-jenis-plot-categorical', component_property='value'),
    Input('ddl-x-plot-categorical','value')]
    )
def update_categorical_graph(ddljeniscategory,ddlxcategory):
    return {
        'data': getPlot(ddljeniscategory,ddlxcategory),
        'layout': go.Layout(
                    xaxis={'title': ddlxcategory.capitalize()}, yaxis={'title': 'US$'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    # legend={'x': 0, 'y': 1}, 
                    hovermode='closest',
                    boxmode='group',violinmode='group'
                    # plot_bgcolor= 'black', paper_bgcolor= 'black',
                )
    }

# SEBERNERNYA KALAU TRIGGERNYA SAMA LEBIH BAIK DI JADIKAN SATU CALLBACK SAJA UNTUK MEMPERCEPAT
@app.callback(
    Output('histogramPlot','figure'),
    [Input('ddl-x-plot-histogram','value')]
)
def update_histogram_plot(ddlxhistogram):
    return{
        'data': gethist(dfTips[ddlxhistogram]),
        'layout': go.Layout(
            xaxis=dict(title=ddlxhistogram.capitalize()),
            yaxis=dict(title='Jumlah Transaksi')
        )
    }

@app.callback(
    Output('divH4hist','children'),
    [Input('ddl-x-plot-histogram','value')]
)
def batashits(ddlxhistogram):
    return [html.H4('Batas Min : '+str(dfTips[ddlxhistogram].mean()-dfTips[ddlxhistogram].std())),
            html.H4('Batas Max : '+str(dfTips[ddlxhistogram].mean()+dfTips[ddlxhistogram].std()))]

if __name__ == '__main__': # karena coding bisa di panggil di code yang lain, if akan True jika program dijalankan langsung, bukan dipanggil oleh code/module lain nanti ada contohnya one.py dan two.py
    #run server on port 1997
    #debug=True for auto restart if code edited
    app.run_server(debug=True, port=1997)

