import yt_dlp
from back import USERNAME, PASSWORD


def extraer_links_playlist(url_playlist: str) -> list[str]:
    """Devuelve una lista de links completos de una playlist de YouTube."""

    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "noplaylist": False,
    }


    links: list[str] = []

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url_playlist, download=False) or {}

        entries = info.get("entries")
        if entries is None:
            entries = info.get("playlist") or info.get("_type")

        entries = entries or []


        for entry in entries:
            if not entry:
                continue
            url = entry.get("url")
            if isinstance(url, str) and url:
                links.append(url)
                continue

            video_id = entry.get("id")
            if isinstance(video_id, str) and video_id:
                links.append(f"https://www.youtube.com/watch?v={video_id}")

    except Exception:
        return []

    return links



if __name__ == "__main__":
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'username': f'{USERNAME}',  
    'password': f'{PASSWORD}', 
    }

    print("1. Video")
    print("2. PlayList")
    option = input("> ")

    if option == "1":
        link = input("paste link: ")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

    elif option == "2":
        linkPlayList = input("paste link of playlist: ")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for link in extraer_links_playlist(linkPlayList):
                ydl.download([link])

    else:
        print("Opcion no reconocida, saliendo...")

