from alpha_vantage.timeseries import TimeSeries  # importing Time series modules from alpha vintage
import matplotlib.pyplot as plt  # importing module for display graph from matplotlib.

# Defining stockchart function
def stockchart(symbol):
    ts = TimeSeries(key='DDEBX79IAIBRTYI7', output_format='pandas')  # Activation key generated from alphavintage.co
    # pandas one dimensional array to hold data.
    data, meta_data = ts.get_intraday(symbol=symbol, outputsize='compact')  # symbol output name,output compact/full
    print(data)  # print data
    data['4. close'].plot()  # plot close chart
    plt.title('STOCK GRAPH')  # title name
    plt.show()  # plot graph


symbol = input("Enter stock name:")  # output display
stockchart(symbol)  # function calling
