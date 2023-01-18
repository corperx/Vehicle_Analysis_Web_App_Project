import streamlit as st
import pandas as pd
import plotly.express as px

#Reading the file
df = pd.read_csv('vehicles_us_processed.csv')
#-----------------------------------------------
#Creating the title

st.title("Building and deploying a web application dashboard to a cloud service")
st.markdown("by Keke Enem")

#--------------------------------------------------------

#creating header with checkbox

st.header('Market of used cars. Original data')
st.write("""
##### Filter the data below to see a sample of the ads by each manufacturer
""")
show_new_cars = st.checkbox('Include new cars from dealers')
if not show_new_cars:
    df = df[df.state!='new']

#----------------------------------------------

#creating options for filter from all manufacturers and different years
manufacturer_choice = df['manufacturer'].unique()
make_choice_man = st.selectbox('Select manufacturer:', manufacturer_choice)

#---------------------------------------------------------------
#next let's create a slider for years, so that users can filter cars by years of produciton
#creating min and max years as limits for sliders
min_year, max_year=int(df['model_year'].min()), int(df['model_year'].max())

#creating slider 
year_range = st.slider(
     "Choose years",
     value=(min_year,max_year),min_value=min_year,max_value=max_year )

#-----------------------------------------------------------------------
#creating actual range  based on slider that will be used to filter in the dataset
actual_range=list(range(year_range[0],year_range[1]+1))

#---------------------------------------------------------------------
#filtering dataset on chosen manufacturer and chosen year range
filtered_type=df[(df.manufacturer==make_choice_man) & (df.model_year.isin(list(actual_range)))]

#showing the final table in streamlit
st.table(filtered_type.head(10))
#------------------------------------------------------------------------

st.header('Price analysis')
st.write("""
###### Let's analyze what influences price the most. We will check how distibution of price varies depending on 
transmission, engine or body type and state
""")

import plotly.express as px

# Will create histograms with the split by parameter of choice: color, transmission, fuel, type, state

#creating list of options to choose from
list_for_hist=['transmission','fuel','type','state']

#creating selectbox
choice_for_hist = st.selectbox('Split for price distribution', list_for_hist)

#plotly histogram, where price is split by the choice made in the selectbox
fig1 = px.histogram(df, x="price", color=choice_for_hist)

#adding title
fig1.update_layout(
title="<b> Split of price by {}</b>".format(choice_for_hist))

#embedding into streamlit
st.plotly_chart(fig1)


#-------------------------------------------------------------------------------------
#Relationship between condition and model_year:
st.header('Histogram of `condition` vs `model_year`')
fig = px.histogram(df, x='model_year', color='condition')
st.write(fig)
#--------------------------------------------------------------------------

#distribution of vehicle types by the manufacturer 
st.header('Vehicle types by manufacturer')
# create a plotly barchart figure
fig = px.bar(df, x='manufacturer', color='type')
# display the figure with streamlit
st.write(fig)

#----------------------------------------------------------------------
# creating age category of cars, cause we want to take it into account when we analyze the price
df['age']=2023-df['model_year']

def age_category(x):
    if x<5: return '<5'
    elif x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'

df['age_category']=  df['age'].apply(age_category) 

#--------------------------------------------------------------------------------
st.write("""
###### Now let's check how price is affected by odometer or fuel type
""")

#Distribution of price depending on odometer,engine capacity and fuel type
list_for_scatter=['odometer','fuel']
choice_for_scatter = st.selectbox('Price dependency on ', list_for_scatter)
fig2 = px.scatter(df, x="price", y=choice_for_scatter, color="age_category",
                  hover_data=['model_year'])

fig2.update_layout(
title="<b> Price vs {}</b>".format(choice_for_scatter))
st.plotly_chart(fig2)

#-----------------------------------------------------------------------------------------
st.header('Compare price distribution between manufacturers')
# get a list of car manufacturers
manufac_list = sorted(df['manufacturer'].unique())
# get user's inputs from a dropdown menu
manufacturer_1 = st.selectbox(
                              label='Select manufacturer 1', # title of the select box
                              options=manufac_list, # options listed in the select box
                              index=manufac_list.index('chevrolet') # default pre-selected option
                              )
# repeat for the second dropdown menu
manufacturer_2 = st.selectbox(
                              label='Select manufacturer 2',
                              options=manufac_list, 
                              index=manufac_list.index('hyundai')
                              )
# filter the dataframe 
mask_filter = (df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2)
df_filtered = df[mask_filter]

# add a checkbox if a user wants to normalize the histogram
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None

# create a plotly histogram figure
fig = px.histogram(df_filtered,
                      x='price',
                      nbins=30,
                      color='manufacturer',
                      histnorm=histnorm,
                      barmode='overlay')
# display the figure with streamlit
st.write(fig)

#------------------------------------------------------------------------------------
