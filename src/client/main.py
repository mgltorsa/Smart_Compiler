from client.factory.base_factory import ClientFactory
from client.abstract.base_client import AbstractMCPClient
import asyncio
import sys

from shared.logging import get_logger

logger = get_logger()

async def main(client: AbstractMCPClient):
    

    logger.debug("client initiated")
    try:
        await client.connect_to_server()
        logger.debug("connected to server")
        logger.debug("chat loop started")
        await client.chat_loop()
        logger.debug("chat loop finished successfully")
    finally:
        logger.debug("cleaning up")
        await client.cleanup()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python client.py <path_to_server_script>")
        sys.exit(1)
    server_script_path = sys.argv[1]
    client_factory = ClientFactory()
    client = client_factory.create_client("ollama")
    asyncio.run(main(client))

