import asyncio

class CommentExecutor:
    
    def __init__(self):
        self.work_queue = asyncio.Queue()

    async def add_video(self, new_vids):
        for vid in new_vids:
            await self.work_queue.put(vid)

    async def execute(self, task, num_workers=5):
        tasks = [asyncio.create_task(task(self.work_queue)) for _ in range(num_workers)]

        await asyncio.gather(*tasks)
