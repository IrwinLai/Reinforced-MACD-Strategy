import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import floor

def targetstock(means,data,targetstock,purdic):   #每日目标股票
    if means == '1':
        for i in range(len(data)):
            if (data.iloc[i,[4]][0]>0) & (data.iloc[i,[6]][0]>0) & (data.iloc[i,[7]][0]>0):
                targetstock = targetstock.append(df.iloc[i])
        
    if means == '2':
        for i in range(len(data)):
            if (data.iloc[i,[4]][0]<0) & (data.iloc[i,[6]][0]>0) & (data.iloc[i,[7]][0]>0):
                targetstock = targetstock.append(df.iloc[i])
        
    if means == '3':
        for i in range(len(data)):
            if (data.iloc[i,[4]][0]>0) & (data.iloc[i,[6]][0]<0) & (data.iloc[i,[7]][0]>0):
                targetstock = targetstock.append(df.iloc[i])
        
    if means == '4':
        for i in range(len(data)):
            if (data.iloc[i,[4]][0]>0) & (data.iloc[i,[6]][0]>0) & (data.iloc[i,[7]][0]<0):
                targetstock = targetstock.append(df.iloc[i])
        
    if means == '5':
        for i in range(len(data)):
            if (data.iloc[i,[4]][0]>0) & (data.iloc[i,[6]][0]<0) & (data.iloc[i,[7]][0]<0):
                targetstock = targetstock.append(df.iloc[i])
                
    if means == '6':
        for i in range(len(data)):
            if (data.iloc[i,[4]][0]<0) & (data.iloc[i,[6]][0]>0) & (data.iloc[i,[7]][0]<0):
                targetstock = targetstock.append(df.iloc[i])
    
    if means == '7':
        for i in range(len(data)):
            if (data.iloc[i,[4]][0]<0) & (data.iloc[i,[6]][0]<0) & (data.iloc[i,[7]][0]>0):
                targetstock = targetstock.append(df.iloc[i])
    
    if means == '8':
        for i in range(len(data)):
            if (data.iloc[i,[4]][0]<0) & (data.iloc[i,[6]][0]<0) & (data.iloc[i,[7]][0]<0):
                targetstock = targetstock.append(df.iloc[i])
                
    if means == '9': #5+6
        tem = pd.DateFrame()
        for i in range(len(data)):
            if (data.iloc[i,[4]][0]>0) & (data.iloc[i,[6]][0]<0) & (data.iloc[i,[7]][0]<0):  #5
                tem.append(df.iloc[i])                
            if (data.iloc[i,[4]][0]<0) & (data.iloc[i,[6]][0]>0) & (data.iloc[i,[7]][0]<0):  #6
                targetstock = targetstock.append(df.iloc[i])
        tem.sort_values(by=['dif'],ascending = False)
        
        for i in range(min(len(tem),10)):
            targetstock = targetstock.append(tem.iloc[i])
                
    if means == '0':  #4+6
        tem = pd.DataFrame()
        for i in range(len(data)):
            if (data.iloc[i,[4]][0]>0) & (data.iloc[i,[6]][0]>0) & (data.iloc[i,[7]][0]<0): #4
                tem = tem.append(df.iloc[i])
            if (data.iloc[i,[4]][0]<0) & (data.iloc[i,[6]][0]>0) & (data.iloc[i,[7]][0]<0): #6
                targetstock = targetstock.append(df.iloc[i])
        '''
        if len(targetstock) < 8:
            num = 8 - len(targetstock)
            if len(tem)!=0 :
                tem.sort_values(by = 'dif',ascending = True)
                for i in range(min(len(tem),num)):
                    targetstock = targetstock.append(tem.iloc[i])
        '''
        
        for i in range(len(tem)):
            targetstock = targetstock.append(tem.iloc[i])

    return targetstock

def purchasestock(date,stock,purdic,daily,k,stop,stopw):   #购入股票
    amount = max(len(stock),10)
    weight = (1 - stopw)/amount
    amount = len(stock) if len(stock) < 10 else amount
    tem1 = {}
    tem2 = {}
    for j in range(amount):
        tem1 = {stock.iloc[j,[3]][0]:{"pos":floor(daily[k%5]*weight/stock.iloc[j,[2]][0]/100),"weight":weight}}
        tem2.update(tem1)
    #tem2.update(stop)
    stop = {}
    stopw = 0
    tem2 = {date:tem2}
    purdic.update(tem2)
    
    return purdic,amount

def dailycapital(purdic,time,capital,daily,k):    #计算当日收益
    datelist = list(purdic.keys())  #目前持仓的日期
    purdate = datelist[-1]          #最晚的持仓日是上一个交易日，昨天
    deldate = datelist[0]           #最早的持仓日需要删除，即平仓
    saledate = time[time.index(purdate)+1]       #最晚持仓日的下一个交易日是今天
    allstock1 = data.loc[data.index == saledate] #今天的股票行情
    allstock2 = data.loc[data.index == purdate]  #昨天的股票行情
    day = k
    earning = 0
    stop = {}              #记录停牌情况
    stopw = 0
    for d in datelist:     #遍历5个资金账户
        dailyhold = pd.DataFrame(purdic.get(d)).T
        index = list(dailyhold.index)
        dailyearning = 0
        dailychange = 0
        for i in range(len(dailyhold)):
            change = allstock1.loc[allstock1['code'] == index[i],'change']
            if change.count() == 0 :      #今天无收盘价，昨天有，即今天停牌
                dailyearning += 0
                if d == deldate:     #如果要平仓的股票停牌了，把它计入停牌字典，再次买入
                    stop.update({index[i]:purdic.get(d).get(index[i])})
                    stopw += purdic.get(d).get(index[i])['weight']
            else:
                dailychange += change[0] * purdic.get(d).get(index[i])['weight']
        dailyearning = daily[day%5] * dailychange
        daily[day%5] += dailyearning
        if daily[day%5] <=0:
            daily[day%5] =0
        earning += dailyearning
        day += 1
    earn = {saledate:{'capital':earning}}
    capital.update(earn)
    if(len(datelist)>=5):
        purdic.pop(deldate)
        
    return daily,capital,stop,stopw

data = pd.read_csv('2011-2018hs300macd.csv', index_col = 'date')
data = data.fillna(0)
time = list(data.index.unique())
time.sort()

#初始化
initial = 10000000
totalcapital = pd.DataFrame(index = time)
#遍历策略
for means in '0':
    k = 0
    daily = [initial/5 for i in range(5)]
    purdic = {}
    capital = {}
    stop = {}
    stopw = 0
    l = []
    r = []
    #遍历日期
    for i in time[30:-1]:
        stock = pd.DataFrame()
        df = data.loc[data.index==i]
        stock = targetstock(means,df,stock,purdic)
        prudic,amount = purchasestock(i,stock,purdic,daily,k,stop,stopw)
        daily,capital,stop,stopw = dailycapital(purdic,time,capital,daily,k)
        k+=1
        l.append(amount)
    
    #累计收益
    temcapital = pd.DataFrame(capital).T
    totalcapital[means] = temcapital['capital']
    totalcapital[means] = totalcapital[means].fillna(0).cumsum()
totalcapitael = totalcapital.fillna(0)

#输出结果
plt.subplots(figsize = (16,5.5))
totalcapital.index = pd.to_datetime(totalcapital.index)
#tem['rate'][:].plot(label = 'hs300')
for means in '0':
    totalcapital[means] /= initial 
    totalcapital[means] += 1
    totalcapital[means][:].plot(label = means)
plt.legend(loc='best')
plt.show()



