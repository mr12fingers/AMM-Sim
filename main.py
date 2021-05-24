from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import streamlit as st
import math

st.set_page_config(page_title='AMM sim', page_icon=':chart_with_upwards_trend:')

st.write("""
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

""" )

st.write('# Parameters')

st.write('## Initial liquidity parameters')
b0 = eval(st.text_input("Enter initial number of BNB in liquidity", '10') )
s0 = eval(st.text_input("Enter initial number of SHIRO in liquidity ", '0.45*10**15') )

st.write("""
### Enter current  SHIRO per BNB  ( the ratio b/s )
""")

price = eval(st.text_input("Enter current price ", '1/4699570000000') )

xes = eval(st.text_input("Enter X'es to calculate for ", '5') )


st.write("""
# Calculated outputs
""")


st.write("""
##  Final expected BNB and SHIROs in the pool:
""")

k = b0*s0
bnbdash = math.sqrt(xes*price*k)
sdash = k/bnbdash
st.text_input("Nuber of BNB : ", bnbdash) 
st.text_input("Nuber of SHIRO : ", sdash) 

st.write("""<p style="text-align: center;"><a href="https://www.shiroinu.online/"><img src="https://rawcdn.githack.com/mr12fingers/AMM-Sim/50333521a6adfdf6ba146d16037d0cd8cf6a4255/ShiroFinal.svg"
          alt="ShiroInuToken" title="Shiro Inu Token"></a></p>
    <p style="text-align: center;">
      <meta http-equiv="content-type" content="text/html; charset=utf-8">
    </p>
    <h4 style="box-sizing: border-box; font-weight: 600; font-size: 16px; margin: 0px; padding: 0.5em 0px 0.25em; line-height: 1; color: #262730; font-family: &quot;IBM Plex Sans&quot;,sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: white; text-decoration-style: initial; text-decoration-color: initial; text-align: center;"><a
        href="https://www.shiroinu.online/" target="_blank" rel="noopener noreferrer"
        style="box-sizing: border-box; color: rgb(0, 104, 201); text-decoration: underline;">SHIRO
        Inu Token</a></h4>""", unsafe_allow_html=True)
#st.write(""" #### [SHIRO Inu Token](https://www.shiroinu.online/) """)
