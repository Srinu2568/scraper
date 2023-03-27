from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.handle_date import handle_date # Import handle_date util fuction

from database.db import Database # Import database class from db
from model import Model


db = Database()
model = Model()

class Scrape:
    def __init__(self):
        self.url = "https://theverge.com/"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get(self.url)

    def scrape(self):
        self.json_data = []
        elements = self.driver.find_elements(By.CLASS_NAME, 'max-w-content-block-mobile')
        for l in elements:
            data = []
            h2 = l.find_element(By.TAG_NAME, 'h2')
            a = h2.find_element(By.TAG_NAME, 'a')

            url = a.get_attribute('href')
            data.append(url)

            headline = a.get_attribute('innerHTML')
            data.append(headline)

            author_tag =l.find_element(By.CLASS_NAME, 'mr-8')
            author = author_tag.get_attribute('innerHTML')
            data.append(author)

            date_element = l.find_element(By.CLASS_NAME, 'text-gray-63')
            date = date_element.get_attribute('innerHTML')
            full_date = handle_date(date)
            data.append(full_date)

            self.json_data.append(data)

    def save(self):
        # Insert and save data to db
        for data in self.json_data:
            db.insert(data)
        db.save()

        # Save data to csv
        cur = db.getCursor()
        model = Model()
        model.saveToCSV(cur)
        cur.close()


if __name__ == "__main__":
    scrape = Scrape()
    scrape.scrape()
    scrape.save()
    print("Task completed!")