# App Service


### Pending Items
- [x] Set up CI for linting & Black
- [x] Add PyTest
- [ ] Add Tox
- [ ] Connect to Dynamdo DB
- [ ] Connect to S3 Bucket
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
Command to check all
```sh
poetry run task check_all
```
### Useful links
[Swagger](http://localhost:8000/docs)