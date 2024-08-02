import asyncio

from database import database_util
from ingests.ingest_subclasses import IngestCandidateMasterCN

from tortoise import connections


async def main():
    await setup_db()
    conn: BaseDBAsyncClient = connections.get("default")
    await IngestCandidateMasterCN.evaluate(conn)

    await connections.close_all()


# Setup mysql database
async def setup_db():
    try:
        await database_util.db_init()
    except Exception as e:
        pass

if __name__ == '__main__':

    # Process files into tables
    asyncio.run(main())
