#!/usr/bin/env python

"""Given an iTunes playlist file, print a list of albums:
<album> | <artist/composer> [Performed by <artist>]

Example:

python playlist_viewer.py playlist.txt

Migration | Bonobo [Performed by Bonobo, 2017]


Source:

Name	Artist	Composer	Album	Grouping	Work	Movement Number	Movement Count	Movement Name	Genre	Size	Time	Disc Number	Disc Count	Track Number	Track Count	Year	Date Modified	Date Added	Bit Rate	Sample Rate	Volume Adjustment	Kind	Equalizer	Comments	Plays	Last Played	Skips	Last Skipped	My Rating	Location
Migration	Bonobo		Migration						Electronic	11333649	327	1	1	1	12	2017	2/18/17, 5:31 PM	2/18/17, 11:19 AM	256	44100		Purchased AAC audio file			23	12/13/17, 2:59 PM	1	3/24/17, 8:43 AM		Macintosh HD:Users:paulvosper:Music:iTunes:iTunes Media:Music:Bonobo:Migration:01 Migration.m4a
"""


import csv
import sys


def most_common(lst):
    return max(set(lst), key=lst.count)


def print_playlist(playlist):

    with open(playlist, encoding='utf-16') as f:
        reader = csv.DictReader(f, dialect='excel-tab')

        playlist_dictionary = {}

        # Create new playlist_dictionary from playlist file
        for entry in reader:
            album = entry['Album']
            # Classical differs in Artist/Performer vs Composer
            artist = entry['Composer'] if ('classical' in entry['Genre'].lower()) else entry['Artist']
            performer = entry['Artist']
            year = entry['Year']
            if album in playlist_dictionary:
                playlist_dictionary[album][0].append(artist)
                playlist_dictionary[album][1].append(performer)
                playlist_dictionary[album][2].append(year)
            else:
                playlist_dictionary[album] = [[artist], [performer], [year]]

        # Print playlist dictionary
        for entry in playlist_dictionary:
            album = entry
            artist = most_common(playlist_dictionary[entry][0])
            performer = most_common(playlist_dictionary[entry][1])
            year = most_common(playlist_dictionary[entry][2])
            print('{} | {} [Performed by {}, {}]'.format(album, artist, performer, year))


if __name__ == '__main__':

    print_playlist(sys.argv[1])
