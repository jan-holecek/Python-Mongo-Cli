<h1 align="center">MongoApp</h1>

<div align="center">
<br>
A simple Mongo App in the terminal to manage the database
<br><br>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

</div>

## Installation
You will need to have python installed to run

Install all packages.
```
pip install -r requirements.txt
```
Now you will need to configure the `settings.json` file.
(You can find your database account under Security as Database Access)
```json
{
	"name": "<name of your database account>",
	"password": "<password of your database account>",
	"dbName": "<name of your Mongo database>",
}
```
You will need to modify the database name (subdatabase) and collection name in `main.py` file.
```py
db = mongoClient.test #Edit the .test name according to the name of the database (subdatabase).
collection = db.posts #Edit the .posts name to match the collection name in the database.
```
Run the project.
```
python main.py
```
## Authors

- [@jan-holecek](https://www.github.comjan-holecek)
