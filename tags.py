#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import json
import pathlib
from mutagen import easyid3

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("working")


def main():
    """ Main code block """

    json_file = "tags.json"
    with open(json_file,'r') as fd:
        data = fd.read()

    data = json.loads(data)
    for line in data:
        path = pathlib.Path("{filename}".format(**line))
        title = line['title']
        artist = line['artist']
        print("{} - {}".format(title, artist))
        album = 'YouTube'
        if path.exists:
            mp3 = easyid3.EasyID3(str(path))
            mp3["album"] = album
            mp3["artist"] = artist
            mp3["title"] = title
            mp3.save()



if __name__ == "__main__":
    main()

