# SkillCraft Technology Software Development Intern batch 15Th May TO 15TH June 
# Task 4
# Create a program that extracts product information such as names prices and ratings from an online e commerce websites and stores the data in a structured format like a csv.

import requests
import pandas

url = "https://real-time-amazon-data.p.rapidapi.com/search"

query_input=input("Enter the Product")

querystring = {"query":query_input,"page":"1","country":"US","sort_by":"RELEVANCE","product_condition":"ALL","is_prime":"false","deals_and_discounts":"NONE"}

headers = {
	"x-rapidapi-key": "52d63e724dmsh53a73fd83d1d7a9p1e7eedjsn6511910fcbc6",
	"x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data=response.json()



product_dataframe=pandas.DataFrame(data["data"]["products"])




df_filtered = product_dataframe[['asin',
                                  'product_title',
                                  'currency',
                                  'product_price' ,
                                  'product_original_price',
                                  'product_star_rating',
                                  'product_num_ratings',
                                  'product_num_offers',
                                  'product_minimum_offer_price',
                                  'has_variations',
                                  'is_amazon_choice'
                                  ]]


df_filtered.to_csv('./Downloads/Product_Detailed_List.csv')
print("CSV EXPORT SUCCESSFULL")



