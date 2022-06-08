import yt_dlp 

ydl_opts = {
    "outtmpl": "%(title)s.%(ext)s",
    "noplaylist": False,
    "default_search": "auto",
    'format' : 'bestaudio/best',
    'postprocessors' : [{
        'key' : 'FFmpegExtractAudio',
        'preferredcodec' : 'mp3',
        'preferredquality' : '192'
    }],
    'postprocessor_args' : [
        '-ar', '16000'
    ],
    'prefer_ffmpeg' : True,
    'keepvideo' : False
}
def download(url):    
    ydl = yt_dlp.YoutubeDL(ydl_opts)   
    ydl.download(url)
    
if __name__ == '__main__':
    url = str(input('Enter URL or search term to download mp3: \n'))
    download(url)
