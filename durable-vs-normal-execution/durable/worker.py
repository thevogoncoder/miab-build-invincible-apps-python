import asyncio
import concurrent.futures
import logging
import sys

from counter import CountingWorkflow, add_one
from temporalio.client import Client
from temporalio.worker import Worker


async def main():
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    client = await Client.connect("localhost:7233", namespace="default")

    try:
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=100
        ) as activity_executor:
            worker = Worker(
                client,
                task_queue="durable",
                workflows=[CountingWorkflow],
                activities=[add_one],
                activity_executor=activity_executor,
            )
            logging.info(f"Starting the worker....{client.identity}")
            await worker.run()
    except asyncio.exceptions.CancelledError:
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())
