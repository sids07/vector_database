from milvus_database.src.repo.milvus_connection import MilvusDBConnection
from milvus_database.src.repo.dummy_collection import DummyCollection

if __name__ == "__main__":
    connection = MilvusDBConnection()
    connection.start()

    collection = DummyCollection()

    connection.stop()

    