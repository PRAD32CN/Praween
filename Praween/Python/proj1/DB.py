import sqlite3

conn = sqlite3.connect('Praween.db')

c = conn.cursor()
c.execute('''
          CREATE TABLE tblChandan
          (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
          ''')
c.execute('''
          CREATE TABLE tblAddress_1
          (id INTEGER PRIMARY KEY ASC, street_name varchar(250), street_number varchar(250),
           post_code varchar(250) NOT NULL, person_id INTEGER NOT NULL,
           FOREIGN KEY(person_id) REFERENCES tblChandan(id))
          ''')

c.execute('''
          INSERT INTO tblChandan VALUES(1, 'pythoncentral')
          ''')
c.execute('''
          INSERT INTO tblAddress_1 VALUES(1, 'python road', '1', '00000', 1)
          ''')

conn.commit()
conn.close()