#Using .melt() to reshape government data

ur_tall = ur_wide.melt(id_vars= ["year"],var_name="month",
                        value_name="unempl_rate")
ur_tall['date'] = pd.to_datetime(ur_tall['month'] + '-' + ur_tall["year"])
ur_sorted = ur_tall.sort_values("date", ascending= True)

ur_sorted.plot(x="date",y="unempl_rate")
plt.show()       


#Using .melt() for stocks vs bond performance

bond_perc = ten_yr.melt(id_vars=["metric"],var_name="date",
                        value_name="close")
bond_perc_close = bond_perc.query('metric == "close"')  
dow_bond = pd.merge_ordered(dji,bond_perc_close,on="date",
                        suffixes=("_dow","_bond"),how="inner")  
dow_bond.plot(y = ["close_dow","close_bond"], x='date', rot=90)
plt.show()                                            