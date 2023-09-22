# Real State With Fast Api

Real State API using fast API

## Warning
Make sure that you are using the latest version of Python and fastapi.
Also, You have to create a Postgres remote database  and put its name in databse\connection.py in :
```
DATABASE_URL = "postgresql+asyncpg://username:password@localhost/your_db_name"
```
finally, you have to create the migrations with Alembic that i explain this later

## Features
- CRUD Operation For Listing(The Name of House Api)
- CRUD Operation For User
- Authentication Users With JWT
- Connection To A Remote Database
- Handle To Many Requests

## Installation
1. Clone the repository
```
Clone git@github.com:mobinghanbari/house_api.git
```
```
cd listing
```
2. Create a virtualenv
```
python -m venv venv
```
```
venv\Scripts\activate.bat
```

3. Install the requirements
```
pip install -r requirements.txt
```
4. Install the alembic
```
pip install alembic
```
5. Create alembic files
```
alembic revision --autogenerate -m "create a listing and user migrations"
```
6. Apply changes in the database
```
alembic upgrade head
```
7. Running the Belov file
```
start.bat
```

8. Go to the belov address
```
http://127.0.0.1:3000/docs
```
## Contributing

## Note
this project has optional property for you
1. You can test the API using a file that tells the name of the file late
in order to test APIs you just override this file with new data that you added
2. use can add a user automatically using seeds, you just call the seed_users method(which has no parameters) in the main file
```
test file name: test_main
main file: seed_users()
```

Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Create a pull request.


## Contact me
## Email: mobinghnbari222@gmail.com
