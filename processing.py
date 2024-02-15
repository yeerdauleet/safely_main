import json

with open('result.json') as jsonFile:
    data = json.load(jsonFile)

    for video_data in data:
        # Accessing the "desc" field of the current video data
        description = video_data.get("desc", "No description available")

        # Accessing the "playUrl" field inside the "music" field of the current video data
        music_url = video_data.get("music", {}).get("playUrl", "No url")

        # Accessing author information
        author_info = video_data.get("author", {})
        nickname = author_info.get("nickname", "No nickname")
        email = author_info.get("signature", "").split('\nEmail: ')[-1]

        # Print or store the extracted information as needed
        print("Description:", description)
        print("Music URL:", music_url)
        print("Nickname:", nickname)
        print("Email:", email)
        print("\n")
