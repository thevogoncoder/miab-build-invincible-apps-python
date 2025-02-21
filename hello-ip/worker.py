import asyncio
import concurrent.futures

from activities import get_ip, get_location_info
from temporalio.client import Client
from temporalio.worker import Worker
from workflow import GetAddressFromIP


async def main():
    client = await Client.connect("localhost:7233", namespace="default")

    # Run the worker
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as activity_executor:

        worker = Worker(
            client,
            task_queue="greeting-tasks",
            workflows=[GetAddressFromIP],
            activities=[get_ip, get_location_info],
            activity_executor=activity_executor,
        )
        print("Starting the worker....")
        await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
