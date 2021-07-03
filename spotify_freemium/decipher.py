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
	playlist_encrypt = ['https://open.spotify.com/playlist/2peFCkryOU68kcEueeBmcw',
						'https://open.spotify.com/playlist/4gRAQPeK0VBqua9EVCk83i',
						'https://open.spotify.com/playlist/24fobBkjvpmwUL6M55Ls41',
						'https://open.spotify.com/playlist/4ruz6qz9UaJi0Uh9aXWd4e',
						'https://open.spotify.com/playlist/0BRBifP99IZYqtXClXSu4b',
						'https://open.spotify.com/playlist/1EffEt6r2PZiNoqJPBa53S',
						'https://open.spotify.com/playlist/3PFpKt44V2PP5IvNqCn1ly',
						'https://open.spotify.com/playlist/2dijCoBx6ktdHC7OjERJHD',
						'https://open.spotify.com/playlist/4r3lbgLtB6OflmHdNAeFWt',
						'https://open.spotify.com/playlist/55mC6DTHx1jWpHUfXpUaUC',
						'https://open.spotify.com/playlist/4I9peD1SiBDaBhKsDNa4yg',
						'https://open.spotify.com/playlist/3Whz31feyEWBBJ1bgubprI',
						'https://open.spotify.com/playlist/0QPTp6QO7mt3icX7NiFax6',
						'https://open.spotify.com/playlist/57Q4NLC64QOuJcqzzvAioi',
						'https://open.spotify.com/playlist/2CcSamqgDw8BzN0RJp7qGA',
						'https://open.spotify.com/playlist/45ZeJcyQ9oEIf4Eo9aJ4Bt',
						'https://open.spotify.com/playlist/2JUdrxncd30zv3VRJkLaZS',
						'https://open.spotify.com/playlist/5mNmEqtjAnqjXaVFkNZ5ET',
						'https://open.spotify.com/playlist/3DInsqW7PC1gDisXkIV22x']
	
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
