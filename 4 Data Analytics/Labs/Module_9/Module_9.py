# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 09:14:25 2024

@author: ntcrw
"""

import pandas as pd
import plotly.express as px


# Read in the data into the frame
alcohol_df = pd.read_csv('alcohol.csv')
print(alcohol_df.head())

#print("Location: ", len(alcohol_df.location.unique()))

#print("\nDuplicates: \n", alcohol_df[alcohol_df['location'].duplicated()])



"""
#Question 1
# Which country has the highest alcohol consumption?

highest_mask = alcohol_df['alcohol'].values == alcohol_df['alcohol'].max()

high_res = alcohol_df.loc[highest_mask]

print("\nQuestion 1: ", high_res)


# Question 2 
# What is the smallest alcohol consumption value in dataset alcohol.csv? 
lowest_mask = alcohol_df['alcohol'].values == alcohol_df['alcohol'].min()
low_res = alcohol_df.loc[lowest_mask]

print("\nQuestion 2:",low_res)


# Question #3
# What is the average alcohol consumption value of all the countries?

avg_alc = alcohol_df.alcohol.mean()
print("\nQuestion 3:",  avg_alc)


# Question #4
# If we group countries by the first letter of the country names, which 
# letter-group has most alcohol consumption in total?

q4_df = alcohol_df.copy()
print(q4_df.head())


location_value = q4_df['location'].values
print(type(location_value))


first_letter = []
for loc in location_value:
    #print("*",loc,"*")
   # print(type(loc))
    first = loc.strip()[0]
   # print('*', first,"*")
    first_letter.append(first)
  
    
  
# add the list to the dataframe
q4_df["First"] = first_letter
print(q4_df)


letter_group = q4_df.groupby('First').sum()

sorted_group = letter_group.sort_values(by='alcohol', ascending=False)
print("\nQuestion 4: ", sorted_group.index[0])

"""


# Question 5 
# Generate a Choropleth map to show each country’s alcohol consumption 
# using the two datasets provided.

iso_names = pd.read_csv('country_iso.csv', encoding='latin-1')


country_names = list(iso_names['Country'])
country_names_clean = []


for name in country_names:
    #print("*",name,"*")
    #cleaned_name = name.strip()
    #print("*",cleaned_name,"*")
    country_names_clean.append(name.strip())
    
    

country_iso = list(iso_names['iso_3'])

#print(country_names_clean)

#print(country_iso)

# Match the names with the alcohol data.

country_iso_matched = []
country_names_matched = []
country_alcohol_matched = []


for index in range(len(alcohol_df)):
    
    country = alcohol_df.iloc[index, 0]
    
    for index2 in range(len(country_names_clean)):
        
        if country == country_names_clean[index2]:
            #print(country, " ---> ",country_iso[index2] )
           # print('\n')
           country_names_matched.append(country)
           country_iso_matched.append(country_iso[index2].strip())
           country_alcohol_matched.append(alcohol_df.iloc[index, 1])
    

alcohol_dict = {'Country': country_names_matched, 'ISO': country_iso_matched
                ,'Alcohol':country_alcohol_matched}

#print(alcohol_dict)

# Create the dataframe
choro_df = pd.DataFrame(alcohol_dict)

#print(choro_df)

# Draw the choropleth map
fig = px.choropleth(choro_df, locations='ISO', color='Alcohol'
                    , hover_name='Country'
                    , color_continuous_scale=px.colors.sequential.Plasma)

fig.show()

fig.write_image('choro.png')



































