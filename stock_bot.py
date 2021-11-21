from bsedata.bse import BSE
import yfinance as yf
import matplotlib.pyplot as pyl

#creating a BSE instance
b=BSE()

#scrip codes of stocks
codes=[
'500180','500209','532540','500247','507685','500325','500112','532281',
]

#getting the securityID of the stock
names=[]
for i in codes:
    names.append(b.getQuote(i)['securityID'])

# Converting in the format of 'securityID.NS' for yahoo-finance to give accurate data
data=[]
for j in names:
    data.append(j+'.NS')

#downloading the data from yahoo-finance from startdate to enddate
frame = yf.download(data,start = "2020-01-01" , end = "2021-01-01")

#to filter the data to get only the prices
closes=frame['Adj Close']
print(closes)

#Plotting the graph using matplotlib pyplot
grph=closes.plot(kind='line',lw=1,title='Stock prices in 2020',figsize=(12,8))
pyl.show(grph)


