#!/usr/bin/env python

"""Notes:
- Ran into utf-8 error as file is utf-16
- Song meta-data not consistent with album
- Classical meta-data uses different attribution

'album': [['artist'], ['performer'], ['year']]
"""


import csv
import sys


# max(arg1, ar2, *args[, key])
# Return the largest item in an iterable
def most_common(lst):
    return max(set(lst), key=lst.count)


# with open(sys.argv[1], 'rt') as f:
with open(sys.argv[1], encoding='utf-16') as f:
    # reader = csv.reader(f)
    reader = csv.DictReader(f, dialect='excel-tab')

    d = {}

    for entry in reader:
        album = entry['Album']
        artist = entry['Artist']
        performer = entry['Artist']
        year = entry['Year']
        # Classical differs in Artist/Performer vs Composer
        if 'classical' in entry['Genre'].lower():
            artist = entry['Composer']
        if album in d:
            d[album][0].append(artist)
            d[album][1].append(performer)
            d[album][2].append(year)
        else:
            d[album] = [[artist], [performer], [year]]

    for entry in d:
        album = entry
        artist = most_common(d[entry][0])
        performer = most_common(d[entry][1])
        year = most_common(d[entry][2])
        print('{} | {} [Performed by {}, {}]'.format(album, artist, performer, year))
