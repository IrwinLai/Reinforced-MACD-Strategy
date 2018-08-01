## Reinforced-MACD-Strategy
The stock strategy based on the combination of DIF, MACD and MACD%

### Abstract
The Advanced MACD strategy is based on some MACD indicators. According to these indicators, we can divide the stock into 8 gruops, and then rolling purchase these different groups.


### About the Strategy
- Theroy of MACD

![](https://ws4.sinaimg.cn/large/0069RVTdgy1ftsu3ezc2xj30n605kjre.jpg)

According to the formula, DIF is the diffrence between the short term and long term exponential moving average. Hencec, the DIF refeclts the recent trend. When DIF > 0, the recent trand is rising.  
MACD is the different of short term and long term DIF. Simply speaking, MACD is the change rate of DIF.   
dMACD, actually, should be '(MACDt - MACDt-1) / MACDt-1' the differential coefficience of MACD, but we only need to know whether this indicator is positive or negative. So we just assume the dMACD is 'MACDt - MACDt-1'  
In short, the DIF is the velocity of the price, the MACD is the acceleration of price, and the dMACD is the velocity of acceleration.

Based on these information, we can consider under different condition of the three indicors, if the stock prices have some rule? We'll check it.

||DIF|MACD|dMACD|  
|:--:|:--:|:--:|:--:|
|1|+|+|+|
|2|-|+|+|
|3|+|-|+|
|4|+|+|-|
|5|+|-|-|
|6|-|+|+|
|7|-|-|+|
|8|-|-|-|

- Steps of the Strategy

1. Get the DIF, MACD, dMACD
2. In each trading day, divide the index componential stocks into 8 groups. 
3. Rolling purchase each group one by one in each weight and keep the stock for 5 days.
4. For the suspended stocks we are keeping, we will sell them after 5 trading day, and we will not buy the stock, which is suspending.
5. Consider the trade fee of 0.01% for buying and selling.

### Test Result of HS300 index
1 to 8 is the different group. 9 is the combination of group 5 and 6. 0 is the combination of group 4 and 6.  
![](https://ws3.sinaimg.cn/large/0069RVTdgy1ftuh0bgtzyj30re0fk3zs.jpg)  
According to the photo and form, we can see no group or combination perform better than the hs300 index. However, if we focus on the time before the big plunge in 2015, we can find the group 4 and 5 is suitable for the phase of rising, and the group 6 is good in the stationary moment. That is worthy for thinking deeply.  
However, I once read a similar strategy, which has a little better result. 

### Analysis
We simply analyz the group 1 and 4.

- Group 1  
The group 1 means the DIF, MACD and dMACD are all positive. Hence, these stocks are easily capture the opportunity of quickly accelerated rising.   
- Group 4  
The group 4 means the DIF and MACD are positive, and the dMACD is negative. So the stocks are in the rising trend with increasing velocity. However the acceleration is becoming slow. So that could be a steady increasement.

### Other Test
- ZZ500
![](https://ws3.sinaimg.cn/large/0069RVTdgy1ftujldrsz3j30qg0emmxz.jpg)




 
