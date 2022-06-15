
# pip install pytube
from pytube import YouTube

inputYoutubeUrl = input("The Youtube video you want to download: ")
inputOutPath = input("Output path, leave empty if you want it in the same folder: ")

def downloader(url: str, outpath: str = "./"):
    yt = YouTube(url)
    yt.streams.filter(file_extension="mp4").get_highest_resolution().download(outpath)

if __name__ == "__main__":
    downloader(inputYoutubeUrl,inputOutPath)