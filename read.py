from db import SQLite

sql = SQLite('f.sqlite3')

print(sql.read_company())
print(sql.read_office())