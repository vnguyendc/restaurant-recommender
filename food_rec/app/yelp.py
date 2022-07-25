import requests
import yaml
from urllib.parse import urlencode

ENDPOINT_URL = 'https://api.yelp.com/v3/'
BUSINESS_SEARCH = 'businesses/search'
BUSINESS_DETAIL = 'businesses/'

class YelpSearcher():
    '''
    Object to make GET requests to Yelp API, and search for businesses/restaurants
    through yelp. 

    - Search and get list of businesses 
    - Get individual business details
    - Get reviews

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
        secrets_file = yaml.safe_load(open('app/auth/secrets.yaml', 'r'))
        return secrets_file['yelp_api_key']

    def search(self, keywords, location, distance, price, limit=None):
        '''
        makes request
        returns object of restaurant results
        '''

        ## process args into params dict
        self.params['term'] = keywords
        self.params['location'] = str(location)
        self.params['distance'] = str(self.convert_miles_meters(distance))
        self.params['price'] = str(self.pricing[price])
        if limit:
            if limit > 20:
                print('Max number of restaurants allowed to be returned is 20.')
                limit = 20
            self.params['limit'] = str(limit)
            

        ## call make_request and pass in params
        endpoint_url = ENDPOINT_URL + BUSINESS_SEARCH
        response = self.make_request(endpoint_url, self.params)

        ## handle and parse request json
        ## return as list of business
        if response is not None:
            self.results = self.get_businesses(response)
            return self.results
        else:
            return None


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
        results = []
        for bus in response['businesses']:
            attributes = {}
            attributes['id'] = bus['id']
            attributes['name'] = bus['name']
            attributes['image_url'] = bus['image_url']
            attributes['url'] = bus['url']
            attributes['categories'] = [item['title'] for item in bus['categories']]
            attributes['rating'] = bus['rating']
            attributes['display_address'] = bus['location']['display_address']
            results.append(attributes)
        return results

    def get_business_ids(self, response):
        '''
        returns list of business ids from response 
        '''
        results = [bus['id'] for bus in response['businesses']]
        return results

    def get_business_details(self, id):
        '''
        gets specific business details based on id
            - display phone
            - photos
            - pricing
        '''
        endpoint_url = ENDPOINT_URL + BUSINESS_DETAIL + str(id)
        response = self.make_request(endpoint_url)

    def convert_miles_meters(self, miles):
        conversion_factor = 0.62137119
        return int(int(miles) / conversion_factor * 1000)

    def make_request(self, url, query=None):
        headers = {'Authorization': 'Bearer %s' % self.api_key}

        try:
            response = requests.get(url, headers=headers, params=query, timeout=5)
            response.raise_for_status()
            
            # Code here will only run if the request is successful
            return response.json()

        except requests.exceptions.HTTPError as errh:
            print(errh)
            return None
        except requests.exceptions.ConnectionError as errc:
            print(errc)
            return None
        except requests.exceptions.Timeout as errt:
            print(errt)
            return None
        except requests.exceptions.RequestException as err:
            print(err)
            return None

    