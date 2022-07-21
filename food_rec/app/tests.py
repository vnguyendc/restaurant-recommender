from django.test import TestCase

# Create your tests here.
from yelp import YelpSearcher

searcher = YelpSearcher()
keywords = ['korean']
location = 'murray hill, NY'
distance = 3
price = '$$$'

response = searcher.search(keywords=keywords, location=location,
                distance=distance, price=price)

print(response)


import json
json.dump(response, open('test_results.json', 'w'))
# json.dump(response['businesses'][-1], open('test_results.json', 'w'))