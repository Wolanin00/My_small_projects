from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "REMOVED"
CLIENT_SECRET = "REMOVED"

sp_mati = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:3000",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="../x-folder/day_46_token_MS.txt"
    )
)
user_id = sp_mati.current_user()["id"]

date = input("Type date of Billboard Hot 100 in format YYYY-MM-DD: ")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
soup = BeautifulSoup(response.text, 'html.parser')
all_titles = soup.select(selector="li ul li h3")
song_list = [title.get_text().strip() for title in all_titles]
song_uris = []
year = date.split("-")[0]
for song in song_list:
    result = sp_mati.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

created_playlist = sp_mati.user_playlist_create(user=user_id, name=f"{date} Billboard 100 MS", public=False)
sp_mati.playlist_add_items(playlist_id=created_playlist["id"], items=song_uris)
