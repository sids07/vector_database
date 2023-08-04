from milvus_database.src.repo.milvus_connection import MilvusDBConnection
from milvus_database.src.services.dummy_service import DummyEmbeddingService
from milvus_database.src.services.transformers_embedding_processor import TransformerEmbeddingProcessor

if __name__ == "__main__":

    connection = MilvusDBConnection()
    connection.start()

    content_name = "hepatitis_b"

    embedding_processor = TransformerEmbeddingProcessor(
        model_name="sentence-transformers/multi-qa-mpnet-base-dot-v1"
    )

    service = DummyEmbeddingService(
        embedding_service= embedding_processor
    )

    response = service.delete_data(
        content_name= content_name
    )

    connection.stop()