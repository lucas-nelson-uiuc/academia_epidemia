import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import spotipy.oauth2 as oauth2
import pandas as pd
import time

class SpotifyUser():

	def __init__(self):
		self.client_id = ''
		self.client_secret = ''

def decipher_playlist(spotify_user, url_list):

	auth_manager = SpotifyClientCredentials(client_id = spotify_user.client_id,
											client_secret = spotify_user.client_secret)
	sp = spotipy.Spotify(auth_manager=auth_manager)

	#playlist_encrypt = url_list
	playlist_encrypt = # enter list of playlists
	
	playlist_names = [sp.playlist(playlist)['name'] for playlist in playlist_encrypt]
	print(playlist_names)

	print('----------------------')

	encrypt_dict = {"4'": 'r', "1_": 'l', "6-": 'g', "4": 'a', "1": 'i', "0": 'o', "5": 's', "3": 'e'}
	
	updated_playlists = []
	for playlist in playlist_names:
		for code in encrypt_dict:
			if code in playlist:
				playlist = playlist.replace(code, encrypt_dict[code])
		updated_playlists.append(playlist)
	
	print(updated_playlists)

if __name__ == '__main__':
	user = SpotifyUser()
	user.client_id = # enter client_id
	user.client_secret = # enter client_secret
	decipher_playlist(user, '')



# print(playlist_decrypt)
