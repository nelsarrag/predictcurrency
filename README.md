# Forecasting Currency Exchange Values in Path of Exile
This is older code I wrote in 2021 when I began learning Python.

Why is historical data highly predictive of price in this economy?
* Unlike the real world market, the PoE economy is reset every “league,” or 90 day period, and new in-game content is added.
* In other words, all previously attained wealth is deleted, giving every player the same opportunity to interact in a fresh economy and game state.
* While all players start from 0, not all players progress at the same rate.
* There always exists more experienced players who generate wealth at a more rapid rate.
* Thus, their demand for certain commodities will increase predictively.

Price modeling with a probability density function:
* Probability density functions for some currencies can indicate whether a certain price will likely adjust to a mean value or not.
* Given a current currency exchange rate, a trader can input a small interval including the value and calculate the area under the curve to estimate the probability of the currency being said value.
* For currencies with strong bimodal distributions (such as the Alteration Orb), this can help inform likely market directions for the currency.
* This analysis, coupled with in-game knowledge of how the economy generally develops, is a strong indicator of future currency pricing.

