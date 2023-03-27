import csv

class Model:
    def __init__(self):
        self.path = './ddmmyyy_verge.csv'
        self.count = 0 # Row count
    
    # Inserting the data
    def saveToCSV(self, cur):
        # Getting all the data
        cur.execute('SELECT * FROM theverge')
        rows = cur.fetchall()
        
        with open(self.path, 'w', newline='') as csvfile:
            # creating a csv writer object
            writer = csv.writer(csvfile)
            # Writing columns
            columns = ['id', 'url', 'headline', 'author', 'date']
            writer.writerow(columns)
            writer.writerows(rows)
        csvfile.close()

        print('Data Saved to CSV File successfully!')
