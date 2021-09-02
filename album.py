def make_album(artist ,title ,tracks = ' '):
	#make dictionary of info
	album_info = {'Title': title, 'Artist': artist}
	if tracks:
		album_info['No. of Tracks'] = tracks
	return album_info

while True:
	print("What's your faveourite Album?")
	print("type 'q' to quit")

	a_title = input("Name the album: ")
	if a_title == 'q':
		break

	a_artist = input("Name the artist: ")
	if a_artist == 'q':
		break

	a_tracks = input("how many tracks: ")
	if a_tracks == 'q':
		break

	user_album = make_album(a_artist, a_tracks, a_tracks)
	print(user_album)

