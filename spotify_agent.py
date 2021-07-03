import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import spotipy.oauth2 as oauth2
import pandas as pd
import time

class SpotifyUser():

	def __init__(self):
		self.client_id = ''
		self.client_secret = ''

def get_playlist_df(spotify_user, url):

	auth_manager = SpotifyClientCredentials(client_id = spotify_user.client_id,
											client_secret = spotify_user.client_secret)
	sp = spotipy.Spotify(auth_manager=auth_manager)


	# gather track details
	details_labels = ['album', 'artist', 'title', 'url', 'length', 'explicit', 'popularity', 'number']
	track_details = []
	for item in sp.playlist_tracks(url)['items']:
		track_album = item['track']['album']['name']
		track_artist = item['track']['artists'][0]['name']
		track_title = item['track']['name']
		track_url = item['track']['external_urls']['spotify']
		track_length = item['track']['duration_ms']
		track_explicit = item['track']['explicit']
		track_popularity = item['track']['popularity']
		track_number = item['track']['track_number']
		track_details.append([track_album, track_artist, track_title, track_url, track_length,
								track_explicit, track_popularity, track_number])

	# gather track features
	features_labels = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness',
						'liveness', 'valence', 'tempo', 'signature']
	track_features = []
	for track in track_details:
	   audio_features = sp.audio_features(track[3])[0]
	   track_danceability = audio_features['danceability']
	   track_energy = audio_features['energy']
	   track_loudness = audio_features['loudness']
	   track_speechiness = audio_features['speechiness']
	   track_acousticness = audio_features['acousticness']
	   track_instrumentalness = audio_features['instrumentalness']
	   track_liveness = audio_features['liveness']
	   track_valence = audio_features['valence']
	   track_tempo = audio_features['tempo']
	   track_signature = audio_features['time_signature']
	   track_features.append([track_danceability, track_energy, track_loudness, track_speechiness,
                            track_acousticness, track_instrumentalness, track_liveness, track_valence,
                            track_tempo, track_signature])

	# combine details and features per track
	for track, features in zip(track_details, track_features):
		track.extend(features)

	# combine labels
	details_labels.extend(features_labels)

	playlist_df = pd.DataFrame(track_details, columns=details_labels)
	print(playlist_df.head(60))

if __name__ == '__main__':
	user = SpotifyUser()
	user.client_id = # enter client_id
	user.client_secret = # enter client_secret
	get_playlist_df(user, 'URL/URI/id')