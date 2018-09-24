# import seaborn as sns
import plotly.graph_objs as go  

# dfTips = sns.load_dataset('tips')

def gethist(xHist):
    atas=xHist.mean()+xHist.std()
    bawah=xHist.mean()-xHist.std()
    return [go.Histogram(x=xHist[(xHist<=atas)&(xHist>=bawah)],name='Normal'),
            go.Histogram(x=xHist[(xHist>atas)|(xHist<bawah)],name='Not Normal')]