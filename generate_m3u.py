import requests

API = "https://tv.volleyballworld.com/api/client-feed?feed-url=https://zapp-5434-volleyball-tv.web.app/jw/playlists/FljcQiNy"

playlist = "#EXTM3U\n"

try:
    r = requests.get(API, timeout=10)
    data = r.json()

    items = data.get("playlist", [])

    for item in items:
        vid = item.get("mediaid")
        title = item.get("title", "Unknown")

        image = ""
        if "images" in item:
            for img in item["images"]:
                if img.get("width") == 1920:
                    image = img.get("src")

        if vid:
            stream = f"https://livecdn.euw1-0005.jwplive.com/live/sites/fM9jRrkn/media/{vid}/live.isml/.m3u8"

            playlist += f'#EXTINF:-1 tvg-logo="{image}",{title}\n'
            playlist += stream + "\n"

except Exception as e:
    print("ERROR:", e)

with open("munin.m3u", "w", encoding="utf-8") as f:
    f.write(playlist)

print("Playlist updated")
