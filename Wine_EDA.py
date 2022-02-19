#The goal of the below code is to set up standardized functions for exploratory data analysis (EDA)
#While this will be used on a wine dataset, this can be applied generally
#Below are some important libraries for data analytics/science
import numpy as np
from matplotlib.pyplot import *
import pandas as pd
import warnings #This is so we can see all cols of a dataset in a terminal
#To start things off, import the 'CSV' to be worked with
warnings.filterwarnings('ignore')
pd.set_option("display.max_columns", None) #From this point on, all cols will be visible in the terminal
#The dataset will be the only global variable. While not the best practice, this is the most convinient form
wine_dataset = pd.read_csv("H:\Data for DAP\Wine Data Project\Wine Review Data Reformatted CSV.csv")
#This function looks at some general characteristics of the data as well as the first five rows of data
def data_peek_fn(wine_dataset):
    return wine_dataset.info(),wine_dataset.shape,wine_dataset.head()

#After the first look at the data, I want to see how many blanks there are within my data
#This function enumerates nulls and counts them
def null_checker_fn(wine_dataset):
    return wine_dataset.isna().any(), wine_dataset.isna().sum()

#That is a lot of nulls in my dataset. Let's clean that up with the next function and look at the data again
def basic_data_clean_fn(wine_dataset):
    reshaped_wine_dataset = wine_dataset.dropna()
    return reshaped_wine_dataset.info(), reshaped_wine_dataset.shape, reshaped_wine_dataset.head()
#print(basic_data_clean_fn(wine_dataset))
#Let's look at some summary stats for points and price
#Remember if your col names are upper or lowercase (wine data cols are lowercase)
def summary_stats(wine_dataset):
    reshaped_wine_dataset = wine_dataset.dropna()
    wine_points = wine_dataset['points']
    wine_price = wine_dataset['price']
    print("Summary stats of the wine points:", wine_points.describe())
    print("Summary stats of the wine prices:", wine_price.describe())
#print(summary_stats(wine_dataset))