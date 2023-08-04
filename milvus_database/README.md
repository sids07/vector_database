# Milvus vector database

Here, I have shown basic CRUD and search functionality within Milvus Vector Database.

## To run the code follow the below procedure:

1. It is recommended to create a new virtual environment.
   ```
   conda create --name env_name python==3.9
   ```
2. Now install the required packages.
   ```
   pip install -r requirements.txt
   ```
3. Now, we have docker-compose present within the scripts sub-directory. We need to run that docker-compose in order to make the Milvus server run locally.
   ```
   docker-compose -f scripts/milvus-docker-compose.yml up -d
   ```
   <b>NOTE</b>: You can now access the Milvus server in URL `localhost:7000`
4. If your PYTHONPATH is not set properly just use the below command to set it:
   ```
   export PYTHONPATH=your_directory_where_you_clone_this_repo/vector_database/milvus_database
   ```
5. Now, follow the codes given on `examples/` to do the respective task just make sure you first create collections and insert some data to perform other tasks.
   
   a. First run `examples/create_collection.py`. Make changes to the field schema based on your requirements and use cases.
   b. Then insert a few data into the created collection using `examples/insert_data.py`.
   c. Once the above a and b steps are done, you can perform any of the remaining functionalities mentioned in examples/. 

## Few important considerations on data for each task before running examples code:

### Insertion:
Data must be in any one of the following formats:

   a. CSV file:
   ```
   treatment_plan_name,content
   a,"Hi,my name is Siddhartha and I am from Nepal"
   b,I am interested in Natural Language Processing
   ```

   b. Dictionary Format:
   ```
   {
     "treatment_plan_name":"a",
     "content":"Hi my name is Siddhartha and I am from Nepal"
   }
   ```

### Deletion:
For deletion, you must provide the `treatment_plan_name` for which you want to delete the record.

### Update:
For Updating, data must be in Dictionary Format:
```
{
  "treatment_plan_name":"a",
  "content":"Hi my name is Siddhartha and I am from Nepal"
}
```

Then, it will update if the treatment plan name already exists on the database. Else it will simply insert new data.

### Similarity Search:
For similarity search, we will simply need to provide a query from a user, the threshold score and finally treatment_plan_name if we want to filter data based on treatment_plan and then do similarity search.