# Vehicle_Analysis_Web_App_Project

## A simple application to explore some properties of a used car dataset.

This web app is built using the Python framework Streamlit and utilizes Plotly-Express for data visualization. The app includes the following:
- A price analysis feature that allows users to view the distribution of prices based on various criteria, such as transmission type, engine type, body type, and state. 
- An analysis of vehicle type (sedan, truck, coupe, etc) feature that allows users to view the distribution of vehicles based on the manufacturer.
- A distribution of the vehicle condition (good, like new, excellent, etc) vs model year
- An analysis of price is affected by odometer, engine capacity and fuel type. 
- finally, a comparison of price distribution between manufacturers 


Using a drop down menu, users can select the name of the manufacturer whose data would be analyzed.

Users can select the range of years they want up till 2019. 

Users can select the criteria they want to use to split the data by using a drop-down menu. Once a criteria is selected, a histogram is generated and displayed, showing the distribution of prices based on the selected criteria.

Users can also click on the legend to change the type of distribution they want. For example users can click on good and fair under the conditon legend to view only the distribution of the 2 conditions.  

The web app is deployed on Render and can be accessed via a web browser using this link: https://vehicle-analysis-web-app.onrender.com/
