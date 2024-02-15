from TikTokApi import TikTokApi
import asyncio
import os
import json

ms_token = os.environ.get("ms_token", "4o-UAo89LaPE4AsLkXEClPde7rS4AKmwZ3G2jjgOJ55FLhRaPyEzJlyxgUInnBOj3KA73wRoBePz13OAdwhMYXZFmiiPr72G0MT3PBbvJaRqqzxZeb0kc6KkIPb-ooEuFUSSwGWZ8AswvyK3")  # set your own ms_token

async def get_hashtag_videos(hashtags):
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False)
        
        all_videos = []
        for hashtag_name in hashtags:
            tag = api.hashtag(name=hashtag_name)
            videos_list = []
            async for video in tag.videos(count=5):
                videos_list.append(video.as_dict)

            all_videos.extend(videos_list)

        # Display the result in JSON format
        result_json = json.dumps(all_videos, indent=2)

        # Save the result as a JSON file
        with open('result.json', 'w') as json_file:
            json_file.write(result_json)

        print("Result has been saved to result.json")

if __name__ == "__main__":
    hashtags_to_search = ["kz","depression"]  # Add more hashtags as needed
    asyncio.run(get_hashtag_videos(hashtags_to_search))
