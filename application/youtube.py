from py_youtube import Data


data = Data("https://www.youtube.com/watch?v=dQw4w9WgXcQ").data()


def get_video_info():
    print(f" title: {data['title']}, \n views: {data['views']}")