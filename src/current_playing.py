import time
import spotipy
import threading
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
# Scope required for currently playing
cid = ""
secret = ""
scope = "user-read-currently-playing"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
spotifyObject = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
counter = 1
result = [False]
index = 0

while True:

    print()
    print(">> updating current track [" + str(counter) + "]")
    print()
    counter += 1

    current = spotifyObject.currently_playing()
    current_type = current['currently_playing_type']

    if current_type == "track":

        artist = current['item']['artists'][0]['name']
        title = current['item']['name']
        length_ms = current['item']['duration_ms']
        progress_ms = current['progress_ms']
        time_ms = length_ms - progress_ms
        time_sec = int((time_ms/1000))
        # id = current['item']['id']
        search_query = artist + " " + title
        # thread to track end of song without clogging main thread
        thread = threading.Thread(target="", args=(time_sec, result, index))
        thread.start()

        print(">> going to sleep for " + str(time_sec) + " seconds")
        print()
        print(">> enter 0 to open browser")
        print(">> enter 1 for artist info")
        print(">> enter nothing to continue")
        print(">> ctrl+c to exit")
        print()

        start = time.time()
        while result[index] == False:
            user_input = ""
            if user_input == "0":
                print(">> updating browser with search query: \"{}\"".format(search_query))

            end = time.time()
            time_sec = time_sec - int(abs(start - end))
        # reset
        result[index] = False

    elif current_type == "ad":

        print(">> ad popped up -- sleeping...")
        time.sleep(30)