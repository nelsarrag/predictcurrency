import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import math

xlpath = "C:\\Users\\elsar\\OneDrive\\Documents\\Predicting Currency Exchange Rates\\CurrencyExchangeData.xlsx"

pd.options.mode.chained_assignment = None  # default='warn'

harvest_currdata = pd.read_excel(xlpath, "Harvest Currency Exchange")
harvest_alt = harvest_currdata.groupby("Get").get_group("Orb of Alteration")
harvest_alt["Day"] = range(1, len(harvest_alt) + 1)
harvest_exa = harvest_currdata.groupby("Get").get_group("Exalted Orb")
harvest_exa["Day"] = range(1, len(harvest_exa) + 1)

heist_currdata = pd.read_excel(xlpath, "Heist Currency Exchange")
heist_alt = heist_currdata.groupby("Get").get_group("Orb of Alteration")
heist_alt["Day"] = range(1, len(heist_alt) + 1)
heist_exa = heist_currdata.groupby("Get").get_group("Exalted Orb")
heist_exa["Day"] = range(1, len(heist_exa) + 1)

ritual_currdata = pd.read_excel(xlpath, "Ritual Currency Exchange")
ritual_alt = ritual_currdata.groupby("Get").get_group("Orb of Alteration")
ritual_alt["Day"] = range(1, len(ritual_alt) + 1)
ritual_exa = ritual_currdata.groupby("Get").get_group("Exalted Orb")
ritual_exa["Day"] = range(1, len(ritual_exa) + 1)

metamorph_currdata = pd.read_excel(xlpath, "Metamorph Currency Exchange")
metamorph_alt = metamorph_currdata.groupby("Get").get_group("Orb of Alteration")
metamorph_alt["Day"] = range(1, len(metamorph_alt) + 1)
metamorph_exa = metamorph_currdata.groupby("Get").get_group("Exalted Orb")
metamorph_exa["Day"] = range(1, len(metamorph_exa) + 1)

delirium_currdata = pd.read_excel(xlpath, "Delirium Currency Exchange")
delirium_alt = delirium_currdata.groupby("Get").get_group("Orb of Alteration")
delirium_alt["Day"] = range(1, len(delirium_alt) + 1)
delirium_exa = delirium_currdata.groupby("Get").get_group("Exalted Orb")
delirium_exa["Day"] = range(1, len(delirium_exa) + 1)

legion_currdata = pd.read_excel(xlpath, "Legion Currency Exchange")
legion_alt = legion_currdata.groupby("Get").get_group("Orb of Alteration")
legion_alt["Day"] = range(1, len(legion_alt) + 1)
legion_exa = legion_currdata.groupby("Get").get_group("Exalted Orb")
legion_exa["Day"] = range(1, len(legion_exa) + 1)

blight_currdata = pd.read_excel(xlpath, "Blight Currency Exchange")
blight_alt = blight_currdata.groupby("Get").get_group("Orb of Alteration")
blight_alt["Day"] = range(1, len(blight_alt) + 1)
blight_exa = blight_currdata.groupby("Get").get_group("Exalted Orb")
blight_exa["Day"] = range(1, len(blight_exa) + 1)

all_altvals = pd.concat([harvest_alt, heist_alt, ritual_alt, metamorph_alt, delirium_alt, legion_alt, blight_alt])
all_exavals = pd.concat([harvest_exa, heist_exa, ritual_exa, metamorph_exa, delirium_exa, legion_exa, blight_exa])
alt_vals_exc_ritual_heist = pd.concat([harvest_alt, metamorph_alt, delirium_alt, legion_alt, blight_alt])


all_altvals_avg = all_altvals.groupby("Day").agg(mean_values=pd.NamedAgg(column="Value", aggfunc="mean")) #avg of each index
all_altvals_median = all_altvals.groupby("Day").agg(mean_values=pd.NamedAgg(column="Value", aggfunc="median")) #avg of each index

all_exavals_avg = all_exavals.groupby("Day").agg(mean_values=pd.NamedAgg(column="Value", aggfunc="mean"))
all_exavals_median = all_exavals.groupby("Day").agg(mean_values=pd.NamedAgg(column="Value", aggfunc="median"))

f1 = plt.figure(1)
ax = sns.distplot(all_altvals["Value"], hist=True, kde=True,
                  bins=math.ceil(math.sqrt(len(all_altvals))),
                  color='darkblue',
                  hist_kws={"edgecolor": "black"},
                  kde_kws={"linewidth": 4})
ax.set(xlabel="Alteration Orb price in Chaos Orbs", ylabel="Probability Density", title="Probability Density of Alteration Orb Pricing")
plt.close()

f2 = plt.figure(2)
plt.plot(range(1, len(all_altvals_avg[:95]) + 1), all_altvals_avg[:95])
plt.xlabel("Time (days)")
plt.ylabel("Alteration Orb Purchasing Power in Chaos")
plt.title("Average Price of Alteration Orb as Economy Develops")
plt.close()

f3 = plt.figure(3)
bx = sns.distplot(all_exavals["Value"], hist=True, kde=True,
                  bins=math.ceil(math.sqrt(len(all_exavals))),
                  color="red",
                  hist_kws={"edgecolor": "black"},
                  kde_kws={"linewidth": 4})
bx.set(xlabel="Exalted Orb price in Chaos Orbs", ylabel="Probability Density", title="Probability Density of Exalted Orb Pricing")
plt.close()

f4 = plt.figure(4)
plt.plot(range(1, len(all_exavals_avg[:95]) + 1), all_exavals_avg[:95])
plt.xlabel("Time (days)")
plt.ylabel("Exalted Orb Purchasing Power in Chaos")
plt.title("Average Price of Exalted Orb as Economy Develops")
plt.close()
f5 = plt.figure(5)
cx = sns.distplot(alt_vals_exc_ritual_heist["Value"], hist=True, kde=True,
                  bins=math.ceil(math.sqrt(len(alt_vals_exc_ritual_heist))),
                  color="red",
                  hist_kws={"edgecolor": "black"},
                  kde_kws={"linewidth": 4})
cx.set(xlabel="Alteration Orb price in Chaos Orbs", ylabel="Probability Density", title="Probability Density of Alteration Orb Pricing, Pre-Patch")
plt.close()

f5 = plt.figure(5)
plt.plot(range(1, len(blight_alt) + 1), blight_alt["Value"])
plt.xlabel("Time (days)")
plt.ylabel("Alteration Orb Purchasing Power in Chaos")
plt.title("[Blight League] Pricing of Alteration Orb vs. Time")
plt.close()

f6 = plt.figure(6)
plt.plot(range(1, len(harvest_alt) + 1), harvest_alt["Value"])
plt.xlabel("Time (days)")
plt.ylabel("Alteration Orb Purchasing Power in Chaos")
plt.title("[Harvest League] Pricing of Alteration Orb vs. Time")
plt.close()

f7 = plt.figure(7)
plt.plot(range(1, len(all_altvals_median[:95]) + 1), all_altvals_median[:95])
plt.xlabel("Time (days)")
plt.ylabel("Alteration Orb Purchasing Power in Chaos")
plt.title("Median Price of Alteration Orb as Economy Develops")
plt.close()

f8 = plt.figure(8)
plt.plot(range(1, len(legion_alt) + 1), legion_alt["Value"])
plt.xlabel("Time (days)")
plt.ylabel("Alteration Orb Purchasing Power in Chaos")
plt.title("[Legion League] Pricing of Alteration Orb vs. Time")
plt.close()

f9 = plt.figure(9)
plt.plot(range(1, len(ritual_alt) + 1), ritual_alt["Value"])
plt.xlabel("Time (days)")
plt.ylabel("Alteration Orb Purchasing Power in Chaos")
plt.title("[Ritual League] Pricing of Alteration Orb vs. Time")

f10 = plt.figure(10)
plt.plot(range(1, len(all_exavals_median[:95]) + 1), all_exavals_median[:95])
plt.xlabel("Time (days)")
plt.ylabel("Exalted Orb Purchasing Power in Chaos")
plt.title("Median Price of Exalted Orb as Economy Develops")
plt.show()
