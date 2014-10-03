#web_of_science_categories.py
""" Web of science categories

Source: 

Notes:
	Agricultural Economics & Policy
	Agriculture, Dairy & Animal Science
	Business, Finance

Vars:
	categories (tuple): a tuple of categories 
"""
import pandas as pd 

url = 'D:\My Documents\Desktop\TO IMPLEMENT\web_of_science_categories.xlsx'
df = pd.read_excel(url)
categories = tuple(df['Categories'].values)


