###TASK 1

import requests
city = input("Enter City Name")
url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bab9632b78a8d0e267576ac68515ba3f&units=metric")

responce = requests.get(url)

if responce.status_code == 200:
    data = responce.json()
    
    temparature=data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]
    city_name = data["name"]
    description = data["weather"][0]["description"]
    print(f"""Temparature in {city_name} is {temparature} °C
Humidity : {humidity}%
Wind: {wind}
Description for today: {description}

    """)
else:
    print(f"Error! Status code : {responce.status_code}")

###TASK 2
import requests
url = "https://api.themoviedb.org/3/genre/movie/list?api_key=272f7453e40e478db387d0d340898797"

responce = requests.get(url)

if responce.status_code == 200:
    data = responce.json()
    print("There are choices of genres!")
    for genre in data["genres"]:
        print(genre["name"])

    genre_name = input("Enter a name of the movie genre ( Horror, Comedy, Action ): ")
    genre_id = None
    for genre in data["genres"]:
        if genre["name"].lower() == genre_name.lower():
            genre_id = genre["id"]
            break
    if genre_id is None:
        print("No movies found")

    else:
        import random
        discover_url = f"https://api.themoviedb.org/3/discover/movie?api_key=272f7453e40e478db387d0d340898797&with_genres={genre_id}"
        answer = requests.get(discover_url)
        movies_data = answer.json()
        if movies_data["results"]:
            movie = random.choice(movies_data["results"])
            print(f"""Recommended movie : {movie['title']}
Overview : {movie['overview']}
Release Date : {movie["release_date"]}

""")
        else:
            print("No results.")
else:
    print(f"Error! Staus  code = {responce.status_code}")
    