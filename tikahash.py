from TikTokApi import TikTokApi
import asyncio
import os

# Set your own ms_token (verifyFp), needs to have done a search before for this to work
verifyFp = "verify_lq5a9jwh_i6F7QDD1_1lsB_4T8l_9mLa_KmSpMLeAYT3l"
ms_token="3xIXqKZpwOVTs6_arKIfwIdStGkUXnejQ72TThKU7JTjQ8k5FuukMCJi8_VixMFNn2hcQUwdmt3mSYTwlbhwEFZNdB-u1n_Jmqj8faOFOcGKs5LDgkqgLpGO1BTwAxKWvGVcdjxunB57_fPb"
async def search_users():
    api = TikTokApi()
    api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False)
    await api.create_sessions(ms_tokens=[verifyFp], num_sessions=1, sleep_after=3)
    
    async for user in api.search.users("david", count=10):
        print(user)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = loop.create_task(search_users())
    loop.run_until_complete(task)
