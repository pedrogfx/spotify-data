import sys
import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth

#don't hardcode your secrets in open projects
cid = ""
secret = ""


#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#Test if the connection is working well:
URI_TEST = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=77d8f5cd51cd478d&nd=1"

results = sp.search(q='Metallica', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])

playlist_URI = URI_TEST.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

birdy_uri = 'spotify:artist:77SW9BnxLY8rJ0RciFqkHh' #the neighbourhood
results = sp.artist_albums(birdy_uri, album_type='single')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])