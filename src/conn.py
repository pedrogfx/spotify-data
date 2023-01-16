import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='your_client_id',
                                                client_secret='your_client_secret',
                                                redirect_uri='your_redirect_uri',
                                                scope=['user-library-read', 'user-library-modify']))

search_result = sp.search(q='track:Hey Jude', type='track')
tracks = search_result['tracks']['items']
for track in tracks:
    print(track['name'], track['artists'][0]['name'], track['album']['name'])

tracks_data = []
for track in tracks:
    tracks_data.append({'name': track['name'], 'artist': track['artists'][0]['name'], 'album': track['album']['name']})
    
df = pd.DataFrame(tracks_data)
print(df)

df.to_csv('tracks.csv')