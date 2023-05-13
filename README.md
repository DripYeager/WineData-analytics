# Wine Dataset Analysis, Model, and API

This repository contains a project that focuses on the analysis of a wine dataset using Pandas and NLP techniques, the development of a machine learning model to predict the wine's rating, and the creation of an API to make predictions based on the model. The following sections describe each part of the project in more detail.




## Analytics

In the Jupyter Notebook WineAnalytics.ipynb, performed a series of analyses on the wine dataset, including data cleaning, feature engineering, and exploratory data analysis. I used Pandas and NLP techniques to extract actionable insights from the data, such as the most common wine varieties and the relationship between wine rating and price. The results of these analyses are summarized in the document Actionable Insights from the Data.pdf, which provides an overview of the main findings and their implications. I also explained step-by-step the process I followed and the reasoning behind it in Jupyter Notebook file.

## Model

In the Jupyter Notebook Wine Variety Model.ipynb, I built a machine learning model to predict the wine's variety based on its various features, such as the country, province, variety, and price. We used a random forest classifier and performed 10-fold cross-validation to achieve an accuracy of 56.27%, which is higher than the previously reported accuracy of 52.12%. I also explained step-by-step the process I followed and the reasoning behind it in Jupyter Notebook file.

## API

I created an API using Flask and HTML/CSS, which allows users to input the wine's features and obtain a predicted wine variety based on the model I developed. To use the API, first, install all the required libraries listed in the requirements.txt file. Next, download the entire api folder and run the Flask file. Finally, visit the link http://localhost:5000/ to access the API and make predictions.

I hope that this project provides valuable insights into the wine dataset and serves as a useful resource for anyone interested in wine or machine learning.
