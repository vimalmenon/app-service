# App Service


### Pending Items
- [x] Connect to Dynamo DB
- [ ] Update query types
- [ ] Connect to S3 Bucket
- [ ] Add Tox
- [ ] Set up Authentication
- [ ] Set up CD
- [ ] Push image to DockerHub


### Useful command
Start poetry
```sh
poetry shell
```
Allow Live reload
```sh
uvicorn main:app --reload
```
Start server
```sh
uvicorn main:app
```
Run Pylint
```sh
poetry run pylint **/*.py
```
Run Black
```sh
poetry run black **/*.py
```
Run Pytest
```sh
poetry run pytest -sv
```
### Useful links
[Swagger](http://localhost:8000/docs)
[DB](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/dynamodb/GettingStarted/update_and_query.py)
[Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/put_item.html#)