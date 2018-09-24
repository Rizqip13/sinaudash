import seaborn as sns
import plotly.graph_objs as go  

dfTips = sns.load_dataset('tips')

# def getPlot(xCategory):
#     return {'bar': [go.Bar(
#                         x=dfTips[xCategory],
#                         y=dfTips['tip'],
#                         text=dfTips['day'],
#                         opacity=0.7,
#                         name='Tip',
#                         marker=dict(color='blue'),
#                         legendgroup='Tip'
#                     ),
#                     go.Bar(
#                         x=dfTips[xCategory],
#                         y=dfTips['total_bill'],
#                         text=dfTips['day'],
#                         opacity=0.7,
#                         name='Total Bill',
#                         marker=dict(color='orange'),
#                         legendgroup='TotalBill'
#                     )],
#             'violin':[go.Violin(
#                         x=dfTips[xCategory],
#                         y=dfTips['tip'],
#                         text=dfTips['day'],
#                         opacity=0.7,
#                         name='Tip',
#                         marker=dict(color='blue'),
#                         legendgroup='Tip'
#                     ),
#                     go.Violin(
#                         x=dfTips[xCategory],
#                         y=dfTips['total_bill'],
#                         text=dfTips['day'],
#                         opacity=0.7,
#                         name='Total Bill',
#                         marker=dict(color='orange'),
#                         legendgroup='TotalBill'
#                     )],
#             'box':[go.Box(
#                         x=dfTips[xCategory],
#                         y=dfTips['tip'],
#                         text=dfTips['day'],
#                         opacity=0.7,
#                         name='Tip',
#                         marker=dict(color='blue'),
#                         legendgroup='Tip',
#                     ),
#                     go.Box(
#                         x=dfTips[xCategory],
#                         y=dfTips['total_bill'],
#                         text=dfTips['day'],
#                         opacity=0.7,
#                         name='Total Bill',
#                         marker=dict(color='orange'),
#                         legendgroup='TotalBill',
#                     )]
#             }

#mempersingkat yang diatas
listGOFUNC={
    'bar':go.Bar,
    'violin':go.Violin,
    'box':go.Box
}

def getPlot(jenis,xCategory):
    return [listGOFUNC[jenis](
                x=dfTips[xCategory],
                y=dfTips['tip'],
                text=dfTips['day'],
                opacity=0.7,
                name='Tip',
                marker=dict(color='blue'),
                legendgroup='Tip'
            ),
            listGOFUNC[jenis](
                x=dfTips[xCategory],
                y=dfTips['total_bill'],
                text=dfTips['day'],
                opacity=0.7,
                name='Total Bill',
                marker=dict(color='orange'),
                legendgroup='Tip')
            ]