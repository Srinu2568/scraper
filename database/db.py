import sqlite3

class Database:
    def __init__(self): # Initialize connection to db and get cursor
        self.conn = sqlite3.connect('./database/verge_articles.db')
        self.cur = self.conn.cursor()

    def getCursor(self):
        try:
            # If table doesn't exist, create new one
            self.cur.execute('''
                CREATE TABLE theverge (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT NOT NULL,
                    headline TEXT NOT NULL,
                    author TEXT NOT NULL,
                    date TEXT NOT NULL
                    )
            ''')
        except:
            # If table exists
            pass
        return self.cur # return cursor
    
    def insert(self, data):
        '''
        Removes duplicate data and inserts fresh data
        '''

        cur = self.getCursor()

        url = data[0]
        headline = data[1]
        author = data[2]
        date = data[3]
        cur.execute('SELECT id from theverge WHERE url = ?', (url, ))
        res = cur.fetchone() # fetchone returns one row and None if no match
        if res == None or len(res) == 0:
            cur.execute('INSERT INTO theverge (url, headline, author, date) VALUES(?, ?, ?, ?)',
                            (url, headline, author, date))
        else:
            print("Duplicate data found and Ignored!")

    def save(self): # Save the changes
        '''
        Save the fresh cursor executions
        '''
        self.conn.commit()
        print('Data is saved to database successfully!')

    def printData(self):
        '''
        Prints Last 10 rows
        '''
        cur = self.getCursor()
        cur.execute('SELECT * FROM (SELECT * FROM theverge ASC LIMIT 10 ) ORDER BY id DESC')
        res = cur.fetchall() # Fetchall returns a array of results or empty array if none satisfied the condition
        print(res)



db = Database()
# data = ['google.com', 'this is google', 'sundar', '27-2-2003']
# db.insert(data)
# db.save()
db.printData()
