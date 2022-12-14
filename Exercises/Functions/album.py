# Write a function make_album() to build a dictionary describing a musical album. 
# The function should accept the artist name and the title and return a dictionary 
# with these two information. The function should create 3 different albums.
def make_album(artist_name, album_name):
    album_info = {
        'artist':artist_name,'album':album_name,}
    return album_info

album1 = make_album('the beatles','abbey road')
album2 = make_album('pink floyd','the darkside of the moon')
album3 = make_album('back sabbath','heaven and hell')

for key,value in album1.items():
    print(key.title() + ': '+ value.title())

for key,value in album2.items():
    print(key.title() + ': '+ value.title())

for key,value in album3.items():
    print(key.title() + ': '+ value.title())
