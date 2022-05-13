import urllib.request,json

#Get api key
api_key = None

#Get base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']

def get_movies():
    get_movies_url = base_url.format(api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.data()
        get_movies_respone = json.loads(get_movies_data)

        movies_results = None
        if get_movies_respone['category']:
            get_movies_list = get_movies_respone['category']
            movies_results = process(get_movies_list)
    return movies_results

def process(movies_list):
    movies_results = []
    for movies_item in movies_list:
        id = movies_item.get('id')
        title = movies_item.get('original_title')
        overview = movies_item.get('overview')
        poster = movies_item.get('poster_path')
        vote_average = movies_item.get('vote_average')
        vote_count = movies_item.get('vote_count')

        movies_object = (id,title,overview,poster,vote_average,vote_count)
        movies_results.append(movies_object)
    return movies_results
        








