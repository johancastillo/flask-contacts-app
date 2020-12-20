# Flask Contacts App
## By [Jc Johan][instagram] Developer

### Instructions:

1. Modificated the information of the data base

```python
# Conection to Data Base
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'jcjohan'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskcontacts'
```

2. Execute the sentensives SQL of the file database.sql in MySQL

```mysql
> source ./database.sql
```

3. Install dependencies

```shell
$ pip3 install -r requirements.txt
```

4. Run server

```shell
$ python3 App.py
```

<!-- Links -->
[instagram]: https://instagram.com/jcboxing2707