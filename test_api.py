#!/usr/bin/env python3

import requests
import json


def get_movie_data(movie_name):
    base_url = "http://www.omdbapi.com/"
    params_d = dict()
    params_d['apikey'] = "affe7ef0" #Private API Key
    params_d['t'] = movie_name
    params_d['r'] = "json"
    result = requests.get(base_url, params=params_d)
    if result.status_code == 200:
        json_data = json.loads(result.text)
        #print(json_data)
        json_dict = json.dumps(json_data, indent=4)
        print(json_dict)
        print("***************************************")
        return json_data
    else:
        "There is an error in connecting to the URL"


#get_movie_data("Black Panther")


def get_movie_rating(json_data):
    for item_dict in json_data['Ratings']:
        if item_dict['Source'] == "Rotten Tomatoes":
            print(f"Movie Name: {json_data['Title']}, Rotten Tomatoes Rating: {item_dict['Value']}")


get_movie_rating(get_movie_data("Black Panther"))
print("***************************************")
