import unittest
import requests
import os
from app import score

class FlaskTest(unittest.TestCase):
    
    def setUp(self):
        os.environ['NO_PROXY'] = '0.0.0.0'
        

    def tearDown(self):
        pass
    
    def test_pos_sentiment_score(self):
        text1 = "I am happy"
        print("1st test:")
        self.assertEqual(score(text1), None)
    
    def test_neg_sentiment_score(self):
        text2 = "I am unhappy"
        print("2nd test:")
        self.assertEqual(score(text2), None)
        
    def test_neu_sentiment_score(self):
        text3 = "I am walking on the street"
        print("3rd test:")
        self.assertEqual(score(text3), None)        
        
        
if __name__ == '__main__':
    unittest.main()