#Using merge_asof() to study stocks

jpm_wells = pd.merge_asof(jpm,wells,on="date_time",
                        suffixes=("","_wells"),direction="nearest")
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on="date_time",
                            suffixes=("_jpm","_bac"),direction="nearest")
price_diffs = jpm_wells_bac.diff()
price_diffs.plot(y=["close_jpm", "close_wells", "close_bac"])
plt.show()


#Using merge_asof() to create dataset

gdp_recession = pd.merge_asof(gdp,recession, on="date")
is_recession = ['r' if s=='recession' else 'g' for s in gdp_recession['econ_status']]
gdp_recession.plot(kind="bar", y="gdp", x="date", color=is_recession, rot=90)
plt.show()  