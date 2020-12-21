from __future__ import unicode_literals
import youtube_dl
import os
from mutagen.easyid3 import EasyID3
from tk import *

def main():
    root = Tk()
    root.title('YouTube Downloader')
    root.geometry('400x500')

    root.mainloop()

class Download(object):
    def __init__(self, url):
        self.url = url
        self.save_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        self.song()

    def song(self):
        opts = {
            'verbose': True,
            'fixup': 'detect_or_warn',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '1411',
                }],
            'extractaudio': True,
            'outtmpl': self.save_path + '/%(title)s.%(ext)s',\
            'noplaylist': True,
            'duration': True,
            'description': True,
            'embed_thumbnail': True,

            }
        ydl = youtube_dl.YoutubeDL(opts)
        ydl.download([self.url])
#        metatag = EasyID3(self.save_path + str(opts.get('title')) + '.mp3')
#        metatag['title'] = "Song Title"
#        metatag['artist'] = "Song Artist"
#        metatag.RegisterTextKey("track", "TRCK")
#        metatag['track'] = 7
#        metatag.save()

if initiate():
    url = input('Enter your url to song here: ')
    Download(url)

if __name__ == '__main__':
    main()