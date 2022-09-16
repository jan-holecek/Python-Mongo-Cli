<h1 align="center">Python-Mongo-Cli</h1>

<div align="center">
A simple terminal application for managing a Mongo database.
<br><br>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

</div>

## Installation
You will need to have Python installed to run

#### Clone respository
```
git clone https://github.com/jan-holecek/Python-Mongo-Cli.git
```
#### Install all packages.
```
pip install -r requirements.txt
```
#### Now you will need to configure the `settings.json` file.
(You can find your database account under Security as Database Access)
```json
{
	"name": "<name of your database account>",
	"password": "<password of your database account>",
	"dbName": "<name of your Mongo database>",
	"subdatabaseName": "<name of your subdatabase in database>",
	"collectionName": "<name of your collection in subdatabase>"
}
```
#### Run the project.
```
python main.py
```
## Authors

- [@jan-holecek](https://www.github.com/jan-holecek)
