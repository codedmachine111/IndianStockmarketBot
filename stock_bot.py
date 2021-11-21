from bsedata.bse import BSE
import yfinance as yf
import matplotlib.pyplot as pyl
from config import codes, start_date

#creating a BSE instance
b=BSE()

#getting scrip codes of stocks
sc_codes=codes
print(sc_codes)

#start date
strt_dt=start_date
#getting the securityID of the stock
names=[]
for i in sc_codes:
    names.append(b.getQuote(i)['securityID'])

# Converting in the format of 'securityID.NS' for yahoo-finance to give accurate data
data=[]
for j in names:
    data.append(j+'.NS')

#downloading the data from yahoo-finance from startdate to enddate
frame = yf.download(data,start = strt_dt)

#to filter the data to get only the prices
closes=frame['Adj Close']
print(closes)

#Plotting the graph using matplotlib pyplot
grph=closes.plot(kind='line',lw=1,title='Stock prices in 2020',figsize=(12,8))
pyl.show(grph)


