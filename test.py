import unittest
import sqlite3
from unittest.mock import MagicMock, mock_open, patch
from database.db import Database
from model import Model

class TestCase(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.model = Model('./test.csv')

    def test_get_cursor(self):
        # Get the cursor from the database
        cur = self.db.getCursor()
        cur.execute('SELECT * FROM theverge LIMIT 1')
        # Verify that the data returned by the cursor is correct
        assert cur.fetchone() == (1, 'https://www.theverge.com/2023/3/27/23658536/multiversus-open-beta-shutting-2024-launch', 'MultiVersus’ open beta is shutting down, but the game is set to return in 2024', 'Jay Peters', '28-3-2023')
        cur.close()



if __name__ == '__main__':
    unittest.main()