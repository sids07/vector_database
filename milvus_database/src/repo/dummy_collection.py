from pymilvus import Collection, DataType, CollectionSchema, FieldSchema
from pymilvus import utility

from milvus_database.src.repo.milvus_collection_base import MilvusCollectionBase

class DummyCollection(MilvusCollectionBase):

    def __init__(self):
        self.collection_name = "dummy"
        self.collection = None
        self._create_collection(self.collection_name)

    def _create_collection(self, collection_name):
        if utility.has_collection(collection_name):
            print("Collection is already created.")
            collection = Collection(collection_name)
            collection.load()
            self.collection = collection
        
        else:
            index_params = {
                "index_type": "IVF_FLAT",
                "metric_type": "IP",
                "params": {
                    "nlist": 1024
                }
            }

            id = FieldSchema(
                name = "id",
                dtype = DataType.INT64,
                is_primary = True,
                auto_id = True
            )

            content_name = FieldSchema(
                name="content_name",
                dtype = DataType.VARCHAR,
                max_length = 100
            )

            content_embeddings = FieldSchema(
                name="content_embeddings",
                dtype = DataType.FLOAT_VECTOR,
                dim=768
            )

            schema = CollectionSchema(
                fields= [id, content_name, content_embeddings],
                description="Dummy Collection For Testing."
            )

            collection = Collection(
                name = collection_name,
                schema = schema,
                using = "default",
                shards_num = 2,
                consistency_level = "Strong"
            )

            collection.create_index(
                field_name = "content_embeddings",
                index_params = index_params
            )

            self.collection = collection
            self.collection.load()
        
    def insert(self, data):
        try: 
            insert_response = self.collection.insert(
                data
                )
            return True
        except Exception as e:
            print("Error while inserting data")
            return False
        
    def delete(self, expr):
        count = self.collection.delete(
            expr
        )
        print("Total number of deleted items: ", count)
        return True
    
    
    def hybrid_search(self, embeddings, anns_field:str, content_name:str=None, top_k: int = 5):
        search_params = {
            "metric_type":"IP",
            "params":{
                "nprobe":16
            }
        }

        if content_name:
            print("content_name found")
            search_result = self.collection.search(
                data = embeddings,
                anns_field=anns_field,
                param = search_params,
                limit = top_k,
                expr = f'content_name == \"{content_name}\"',
                output_fields = ["id","content_name"]
            )
        else:
            print("content_name not found")
            search_result = self.collection.search(
                data = embeddings,
                anns_field=anns_field,
                param = search_params,
                limit = top_k,
                output_fields = ["id","content_name"]
            )    
        return search_result

    def get_primary_keys_associated(self, content_name):
        exp = f'content_name == \"{content_name}\"'
        results = self.collection.query(
            expr=exp
        )
        primary_key_list = []
        for result in results:
            primary_key_list.append(result['id'])
        return primary_key_list
    
    def is_content_exist(self, content_name):
        exp = f'content_name == \"{content_name}\"'
        res = self.collection.query(
            expr=exp
        )
        print("TESTED:", len(res))
        return len(res) > 0
