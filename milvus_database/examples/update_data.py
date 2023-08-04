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

    data = {
        "content_name": "hepatitis_b",
        "content": "Hepatitis B is caused by the hepatitis B virus, which is spread in the blood of an infected person. It's a common infection worldwide and is usually spread from infected pregnant women to their babies, or from child-to-child contact. It can also be spread through unprotected sex and injecting drugs. Hepatitis B is uncommon in the UK. It most commonly affects people who became infected while growing up in part of the world where the infection is more common, such as southeast Asia and sub-Saharan Africa. Most adults infected with hepatitis B are able to fight off the virus and fully recover from the infection within a couple of months. But most people infected as children develop a long-term infection. This is known as chronic hepatitis B, and can lead to cirrhosis and liver cancer. Antiviral medicine can be used to treat it. In the UK, vaccination against hepatitis B is recommended for people in high-risk groups, such as: healthcare workers, people who inject drugs, men who have sex with men, children born to mothers with hepatitis B, people travelling to parts of the world where the infection is more common, Hepatitis B vaccination is also part of the routine immunisation programme so all children can benefit from protection from this virus."
    }
    success = service.update_data(
        data= data
    )

    connection.stop()