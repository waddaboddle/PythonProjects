from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "4f5d086e6a854091b4ed855a39c7f42d"
CLIENT_SECRET = "34dc6e50baf740db861b114f3ffa6818"
REDIRECT_URI = "http://example.com"

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope))

user = sp.current_user()
user_id = user["id"]
# print(user_id)

travel_date = input("What year would you like to travel to? Type it in this format YYYY-MM-DD: ")
# LINK = "https://www.billboard.com/charts/hot-100/2000-08-12/"
LINK = f"https://www.billboard.com/charts/hot-100/{travel_date}/"
# print(LINK)

response = requests.get(LINK)

top_100_webpage = response.text

soup = BeautifulSoup(top_100_webpage, "html.parser")

songs = [element.get_text().strip() for element in soup.select(selector="li h3", class_="c-title")]

song_uris = []
year = travel_date.split("-")[0]

playlist_name = f"Hot 100: {travel_date}"
response = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
    collaborative=False,
    description='Hot 100 from billboard.com'
)

playlist_id = response["id"]

for song in songs[:100]:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify, skipped.")

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
