from milvus_database.src.repo.dummy_collection import DummyCollection
from milvus_database.src.utils.utils import filter_search_results
import pandas as pd

class DummyEmbeddingService:
    def __init__(self, embedding_service):
        self.embedding_processor = embedding_service
        self.dummy_collection = DummyCollection()

    def insert_data(self, data):

        if type(data) == dict:
            content_list = [data["content"]]
            content_name_list = [data["content_name"]]

        elif type(data) == pd.DataFrame:
            content_list = list(data["content"])
            content_name_list = list(data["content_name"])
    
        content_embedding_list = self.embedding_processor.get_embeddings(text_list=content_list)

        data = [content_name_list, content_embedding_list]

        success = self.dummy_collection.insert(
            data=data
        )

        if success:
            print("Insertion Successfull")
        
        else:
            print("Insertion Failed")

        return success
    
    def sentence_similarity_search(self, query, content_name= None, thresh = 0.6):

        if len(query)>1:
            query_embeddings = self.embedding_processor.get_embeddings(
                list(query)
            )

            search_result_content_name = self.dummy_collection.hybrid_search(
                embeddings= query_embeddings,
                anns_field= "content_embeddings",
                content_name= content_name
            )

            final_search_result = filter_search_results(
                results= search_result_content_name,
                thresh= thresh
            )

            print("Results obtained: ", final_search_result)
            return final_search_result
        
        else:
            print("Query not found")
    
    def delete_data(self, content_name):

        primary_key = self.dummy_collection.get_primary_keys_associated(
            content_name=content_name
        )

        if len(primary_key)>0:
            expr = f"id in {primary_key}"
            print(expr)
            self.dummy_collection.delete(
                expr= expr
            )
        else:
            print("No Content Name found")
    
    def update_data(self,data):
    
        if self.dummy_collection.is_content_exist(data["content_name"]):
            print("Content Name Exists")

            self.delete_data(
                content_name=data["content_name"]
                )
            
            insert_response = self.insert_data(
                data= data
            )

            return insert_response
        
        print("Content  Doesn't exist")
        insert_response = self.insert_data(
            data=data
        )

        return insert_response

        



