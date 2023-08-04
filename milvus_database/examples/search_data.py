from milvus_database.src.repo.milvus_connection import MilvusDBConnection
from milvus_database.src.services.dummy_service import DummyEmbeddingService
from milvus_database.src.services.transformers_embedding_processor import TransformerEmbeddingProcessor

import pandas as pd

if __name__ == "__main__":
    connection = MilvusDBConnection()
    connection.start()

    embedding_processor = TransformerEmbeddingProcessor(
        model_name="sentence-transformers/multi-qa-mpnet-base-dot-v1"
    )
    service = DummyEmbeddingService(
        embedding_service= embedding_processor
    )

    # If you want to first filter data based on some content_name then uncomment below res:

    # res = service.sentence_similarity_search(
    #     query= "what is type 2 diabetes?",
    #     thresh= 0.001,
    #     content_name= "type_2_diabetes"
    # )

    res = service.sentence_similarity_search(
        query= "I have problem with insulin which disease does it matches most.",
        thresh= 0.01
    )

    print("RESULTS: ", res)

    connection.stop()