import pandas as pd

df_reader = pd.read_csv('ind_pop.csv', chunksize=10)

print(next(df_reader))
print(next(df_reader))

###

urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
print(df_urb_pop.head())
df_pop_ceb = df_urb_pop[df_urb_pop["CountryCode"] == 'CEB']

pops = zip(df_pop_ceb['Total Population'], 
           df_pop_ceb['Urban population (% of total)'])

pops_list = list(pops)
print(pops_list)

###

urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
pops = zip(df_pop_ceb['Total Population'], 
           df_pop_ceb['Urban population (% of total)'])
pops_list = list(pops)


df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]

df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()

###

urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

data = pd.DataFrame()

for df_urb_pop in urb_pop_reader:
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
    pops = zip(df_pop_ceb['Total Population'],
                df_pop_ceb['Urban population (% of total)'])
    pops_list = list(pops)   
    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
     data = pd.concat([data, df_pop_ceb])

data.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()

###

def plot_pop(filename, country_code):
  
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    data = pd.DataFrame()
    
    for df_urb_pop in urb_pop_reader:
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]
        pops = zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Urban population (% of total)'])
        pops_list = list(pops)
        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
        data = pd.concat([data, df_pop_ceb])

    data.plot(kind='scatter', x='Year', y='Total Urban Population')
    plt.show()

fn = 'ind_pop_data.csv'
plot_pop('ind_pop_data.csv', 'CEB')
plot_pop('ind_pop_data.csv', 'ARB')