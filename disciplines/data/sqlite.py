import sqlite3

mem_db = sqlite3.connect(':memory:')
db = sqlite3.connect('db/mydb')
cr = db.cursor()

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