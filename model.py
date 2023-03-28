import csv
from database.db import Database
db = Database()

class Model:
    def __init__(self, path='./ddmmyyy_verge.csv'):
        self.path = './ddmmyyy_verge.csv'
        self.count = 0 # Row count
        self.cur = db.getCursor()
    
    # Inserting the data
    def saveToCSV(self):
        # Getting all the data
        self.cur.execute('SELECT * FROM theverge')
        rows = self.cur.fetchall()
        
        with open(self.path, 'w', newline='') as csvfile:
            # creating a csv writer object
            writer = csv.writer(csvfile)
            # Writing columns
            columns = ['id', 'url', 'headline', 'author', 'date']
            writer.writerow(columns)
            writer.writerows(rows)
        csvfile.close()

        print('Data Saved to CSV File successfully!')
