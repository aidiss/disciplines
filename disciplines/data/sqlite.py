import sqlite3

mem_db = sqlite3.connect(':memory:')
db = sqlite3.connect('db/mydb')
cr = db.cursor()


name1 = 'Andres'
phone1 = '3366858'
email1 = 'user@example.com'
password1 = '1259'
name2 = 'gf'
phone2 = '666'
email2 = 'johndoe@example.com'
password2 = 'abcdef'

name3 = 'fds'
phone3 = '5557241'
email3 = 'johndoe@example.com'
password3 = 'abcdef'

cr.execute('''DROP TABLE users;''')

cr.execute('''CREATE TABLE users(
	StockNumber INTEGER PRIMARY KEY,
	name VARCHAR(50), 
	phone INTEGER,
	email INTEGER,
	password INT);''')
cr.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name1, phone1, email1, password1))
cr.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name2, phone2, email2, password2))
cr.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(:name,:phone, :email, :password)''',
                  {'name':name1, 'phone':phone1, 'email':email1, 'password':password1})

users = [(name1,phone1, email1, password1),
         (name2,phone2, email2, password2),
         (name3,phone3, email3, password3)]
	 
cr.executemany(''' INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?)''', users)
db.commit()

cr.execute('''SELECT name, phone, email, password FROM users;''')
print(cr.fetchone())

cr.execute('''SELECT * FROM users;''')
print(cr.fetchone())

#cr.execute('''UPDATE table_name SET column_name= value WHERE criteria;''')
"""

Syntax or Purpose
------ --------- ---------------------- ------------	
SELECT DISTINCT							Exclude duplicate records for fields selected.
SELECT DISTINCT	CASE WHEN expression	Conditional expression
SELECT DISTINCT	THEN expression	
SELECT DISTINCT	ELSE expression END	

SELECT FROM	table_name					Multiple table names are separated by commas.

SELECT WHERE	                        Row level filtering
SELECT WHERE expression	AND	expression	
SELECT WHERE expression	OR	expression	
SELECT WHERE IN							Comma delimited list enclosed in parenthesis
SELECT WHERE NOT IN						Comma delimited list enclosed in parenthesis
SELECT WHERE BETWEEN					Select records within the specified numeric range
SELECT WHERE NOT BETWEEN				Select records outside of the specified numeric range
SELECT WHERE LIKE						String with wildcard (%) enclosed in parenthesis
SELECT WHERE NOT LIKE					String with wildcard (%) enclosed in parenthesis

SELECT GROUP BY				

SELECT HAVING ORDER BY					Sorting of the output using a comma delimited list of column names
SELECT HAVING LIMIT						Limit the number of rows returned
"""						

db.close()



#id = cr.lastrowid
#print('Last row id: %d' % id)
