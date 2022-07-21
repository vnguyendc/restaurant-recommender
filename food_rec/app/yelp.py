import requests
import yaml
from urllib.parse import urlencode



class YelpSearcher():
    '''
    Object to make GET requests to Yelp API, and search for businesses/restaurants
    through yelp. 

    USAGE:
        call YelpSearcher()
        call search() method, and enter the following arguments:
            - keywords (list of strings)
            - location (string)
            - distance (int)
            - price (str e.g. 1, 2, 3, 4)
        search method will return list of businesses from the response
    '''    
    def __init__(self):
        self.api_key = self.get_api_key()
        self.endpoint_url = 'https://api.yelp.com/v3/businesses/search'
        self.results = {}
        self.params = {
            'term': '',
            'location': '',
            'radius': '',
            'limit': '',
            'sort_by': 'rating',
            'price': '',
            # 'open_now': 'true'
        }
        self.pricing = {
            '$': '1',
            '$$': '2',
            '$$$': '3',
            '$$$$': '4'
        }

    def get_api_key(self):
        secrets_file = yaml.safe_load(open('auth/secrets.yaml', 'r'))
        return secrets_file['yelp_api_key']

    def search(self, keywords, location, distance, price):
        '''
        makes request
        returns object of restaurant results
        '''

        ## process args into params dict
        self.params['term'] = ' '.join(keywords)
        self.params['location'] = str(location)
        self.params['distance'] = str(self.convert_miles_meters(distance))
        self.params['price'] = str(self.pricing[price])

        ## call make_request and pass in params
        response = self.make_request(self.params)

        ## handle and parse request json
        ## return as list of business
        self.results = self.get_businesses(response)

        return self.results

    def get_businesses(self, response):
        '''
        gets the following attributes from json response:
            - name
            - alias
            - image url
            - url
            - categories
            - rating
            - location: display_address
        
        return list of dictionaries
            key: business name
            value: dictionary of above attributes
        
        '''
        results = {}
        for bus in response['businesses']:
            attributes = {}
            attributes['name'] = bus['name']
            attributes['image_url'] = bus['image_url']
            attributes['url'] = bus['url']
            attributes['categories'] = bus['categories']
            attributes['rating'] = bus['rating']
            attributes['display_address'] = bus['location']['display_address']
            results[bus['alias']] = attributes

        return results

    def convert_miles_meters(self, miles):
        conversion_factor = 0.62137119
        return int(int(miles) / conversion_factor * 1000)

    def make_request(self, query):
        headers = {'Authorization': 'Bearer %s' % self.api_key}

        try:
            response = requests.get(self.endpoint_url, headers=headers, params=query, timeout=5)
            response.raise_for_status()
            
            # Code here will only run if the request is successful
            return response.json()

        except requests.exceptions.HTTPError as errh:
            return errh
        except requests.exceptions.ConnectionError as errc:
            return errc
        except requests.exceptions.Timeout as errt:
            return errt
        except requests.exceptions.RequestException as err:
            return err

    