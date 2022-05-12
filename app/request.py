import urllib.request,json

#Get api key
api_key = None

#Get base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']

def get_news():
    get_news_url = base_url.format(api_key)




