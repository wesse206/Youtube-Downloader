import youtube_dl

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

def initiate():
    url = input('Enter your url to song here: ')
    Download(url)

if __name__ == '__main__':
    initiate()
