
# coding: utf-8

# In[11]:


import pandas as pd

#poke=pd.read_csv('D:\Data projects\pandas\pokemon_data.csv')
#print(poke.head(10))
#print(poke.tail(10))

#poke_excel=pd.read_excel('D:\Data projects\pandas\pokemon_data.xlsx')
poke_txt=pd.read_csv('D:\Data projects\pandas\pokemon_data.txt', delimiter='\t')


# In[13]:


print(poke.columns)


# In[18]:


#print(poke['Name'][0:8])
#print(poke.Name[0:8])
print(poke[['Name', 'HP', 'Defense']][0:8])


# In[21]:


print(poke.iloc[5])
#print(poke.iloc[5:11])


# In[22]:


print(poke.iloc[2,2])


# In[24]:


for index, row in poke.iterrows():
    print(index, row)


# In[25]:


poke.loc[poke['Type 1']=="Fire"]


# In[26]:


poke.describe()


# In[27]:


poke.sort_values('Name')
poke.sort_values('Name', ascending=False) #descending sort
poke.sort_values('Type 1', 'HP')
poke.sort_values('Type 1', 'HP', ascending=[1,0]) #1-true, 0-false


# In[28]:


poke.head(5)


# In[33]:


poke['Total']=poke['HP']+poke['Attack']+poke['Defense']
poke.head(5)


# In[34]:


poke.drop(columns=['Total'])


# In[42]:


poke2=poke[['Name', 'HP']]
poke3=poke['Name']
poke2.head(5)


# In[45]:


poke['Total']=poke.iloc[:,4:10].sum(axis=1) #axis=1 adds horisontal, axis=0 adds vertical
poke.head(5)


# In[48]:


cols=list(poke.columns.values)
poke=poke[cols[0:4]+[cols[-1]]+cols[4:12]] #paskutines pozicijos neima
poke.head(5)


# In[ ]:


poke.to_csv('pokemon_mod.csv')
poke.to_csv('pokemon_mod.csv', index=False) #save without indexes
poke.to_excel('pokemon_mod.xlsx')
poke.to_csv('pokemon.txt', index=False, sep='\t')


# In[53]:


#poke.loc[(poke['Type 1']=="Fire") & (poke['Type 2']=='Poison') & (poke['HP']>70)] # and
poke.loc[(poke['Type 1']=="Fire") | (poke['Type 2']=='Poison')] # or
poke.head(5)


# In[56]:


new_poke=poke.loc[(poke['Type 1']=="Grass") & (poke['Type 2']=='Poison') & (poke['HP']<70)]
new_poke.head(5)


# In[57]:


new_poke=new_poke.reset_index()
new_poke

new_poke.reset_index(drop=True, inplace=True)


# In[59]:


mega_poke=poke.loc[poke['Name'].str.contains('Mega')]
not_mega_poke=poke.loc[~poke['Name'].str.contains('Mega')]#~ means not
mega_poke.head(5)
poke.loc[poke['Type 1'].str.contains('Fire|Grass'), regex=True]# regex
poke.loc[poke['Type 1'].str.contains('fire|grass'), flags=re.I, regex=True]# flags=re.I - ignore capital letters
poke.loc[poke['Type 1'].str.contains('pi[a-z]*'), flags=re.I, regex=True]# pi[a-z]* contains p and after that it can be any letter from 0 to infinity
poke.loc[poke['Type 1'].str.contains('^pi[a-z]*'), flags=re.I, regex=True]# ^ - starts with pi


# In[62]:


#Conditional changes
poke.loc[poke['Type 1']=='Fire', ['Type 1']]='Flamer' # change if condition is met
poke.head(12)

poke.loc[poke['Type 1']=='Flamer', ['Generation', 'Legendary']]=['Test 1', 'Test 2']  # change 2 columns or more
poke.head(12)
# change if condition is met


# In[76]:


#Aggregate statistics
poke.groupby(['Type 1']).mean()
poke.groupby(['Type 1']).mean().sort_values(['Defense'], ascending=False)
poke.groupby(['Type 1']).count()['#'].sort_values(ascending=False)
poke.groupby(['Type 1', 'Type 2']).count()['#'].sort_values(ascending=False)


# In[77]:


#Loading large datasets in parts
for poke in pd.read_csv('D:\Data projects\pandas\pokemon_data.csv', chunksize=10):
    print(poke)


# In[ ]:


new_df=pd.DataFrame(columns-df.columns)

for df in pd.read_csv('D:\Data projects\pandas\pokemon_data.csv', chunksize=10):
    results=df.groupby(['Type 1']).count()
    
    ned_df=pd.concat([new_df, results])
    
    #concat appends tables

