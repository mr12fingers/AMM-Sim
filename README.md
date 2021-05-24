# A simple automatic market maker simulator
An automated market maker (AMM) is a type of decentralized exchange (DEX) protocol
that relies on a mathematical formula to price assets.
Instead of using an order book like a traditional exchange, 
assets are priced according to a pricing algorithm.
Lets assume that the two tokens used in this case are SHIRO and BNB

Uniswap uses the following formula:
$b \quad \mathrm{x} s = k$;
Where 
* $b$ = Number of BNB in the pool at the time of the calculation
* $s$ = Number of SHIRO in the pool at the time of the calculation
* $k$ = A constant value which is determined when initial liquidity is provided ( k remains the same at all times)

This calculator can help you calculate the number of BNB and SHIRO in the pool when the 
price of SHIRO reaches a particular value.
In this case the current market price ($b/s$) and the expected returns (in Xes) 

* After choosing each parameter press enter.
* you can use scientific notation like 10**15 for $10^{15}$
* or you can also do math like 1/4699570000000



# Parameters

## Initial liquidity parameters

Enter initial number of BNB in liquidity 

*10*

Enter initial number of SHIRO in liquidity

*0.45*10**15*

### Enter current SHIRO per BNB ( the ratio b/s )

Enter current price

*1/4699570000000*

Enter X'es to calculate for

*5*

# Calculated outputs

## Final expected BNB and SHIROs in the pool:

Number of BNB :

*69.1930058865369*

Number of SHIRO :

*65035474934838.45*

[![ShiroInuToken](https://rawcdn.githack.com/mr12fingers/AMM-Sim/50333521a6adfdf6ba146d16037d0cd8cf6a4255/ShiroFinal.svg)](https://www.shiroinu.online/)



#### [SHIRO Inu Token](https://www.shiroinu.online/)