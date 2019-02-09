#!/usr/bin/env python 

import requests
from bs4 import BeautifulSoup

url = "https://www.humblebundle.com/books/programming-cookbooks"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
tier_dict = {}

##BUNDLE TIERS
tiers = soup.select('.dd-game-row')

for tier in tiers:
	# Only for sections that have a headline
	if tier.select('.dd-header-headline'):
		# Grab tier name and price
		tiername = tier.select('.dd-header-headline')[0].text.strip()
		# Grab tier product names
		product_names = tier.select(".dd-image-box-caption")
		product_names = [prodname.text.strip() for prodname in product_names]
		# Add one product tier to our data structure
		tier_dict[tiername] = { "product": product_names }



# OLD TIERS
#tiers_headlines = soup.select('.dd-header-headline')
# for tier in tiers_headlines:
# print(tier.text.strip()) 
##BELOW IS A ONE-LINER LIST COMPREHENSIONS
# tiers_headlines = soup.select('.dd-header-headline')
# stripped_tiernames = [tier.text.strip() for tier in tiers_headlines]

# ## PRODUCT NAMES dd-image-box-caption
# product_names = soup.select(".dd-image-box-caption")
# stripped_product_names = [prodname.text.strip() for prodname in product_names]

## ACCESSING DATA PATTERN
for tiername, tierinfo in tier_dict.items():
	print(tiername)
	print("################################")
	print("Products:")
	print("\n".join(tierinfo['product']))
	print("\n\n")

## DATA STRUCTURE 
# # - for each tier name and price
# # 	- product list
# tiers = {
# 	"tier1": {
# 		"price": 500,
# 		"products": [
# 			'bookname1',
# 			'bookname2'
# 		]
# 	},

# 	"tier2": {
# 		"price": 500,
# 		"products": [
# 			'bookname1',
# 			'bookname2'
# 		]
# 	}	
# }
