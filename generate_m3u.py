import requests

API = "https://tv.volleyballworld.com/api/client-feed?feed-url=https%3A%2F%2Fzapp-5434-volleyball-tv.web.app%2Fjw%2Fplaylists%2FFljcQiNy"

BASE_STREAM = "https://livecdn.euw1-0005.jwplive.com/live/sites/fM9jRrkn/media/{id}/live.isml/.m3u8"

data = requests.get(API).json()

playlist = "#EXTM3U\n"

items = data["playlist"]["items"]

for item in items:

    video_id = item["mediaid"]
    title = item["title"]

    image = item["image"]

    stream = BASE_STREAM.format(id=video_id)

    playlist += f'#EXTINF:-1 tvg-logo="{image}" group-title="Volleyball",{title}\n'
    playlist += f"{stream}\n"
    
with open("munin.m3u", "w", encoding="utf-8") as f:
    f.write(playlist)

print("munin.m3u updated")
