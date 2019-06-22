import unittest
from auction.card import Card

class Card_test (unittest.TestCase):

    def setUp (self):
        self.card = None

    def tearDown (self):
        self.card = None

    def testWrongCardNumber (self):
        with self.assertRaises(Exception) as context:
            self.card = Card("1234", "123", 2020, 11)
        self.assertTrue("Card number should be 16 digits long" in str(context.exception))

    def testWrongCVC (self):
        with self.assertRaises(Exception) as context:
            self.card = Card("1234567890123456", "aab", 2020, 11)
        self.assertTrue("Card CVC should 3 digits long" in str(context.exception))

    def testUnparsableDate (self):
        with self.assertRaises(Exception) as context:
            self.card = Card("1234567890123456", "123", "aabb", "cd")
        self.assertTrue("Couldn't parse input expiry year or month" in str(context.exception))

    def testInvalidCard (self):
        with self.assertRaises(Exception) as context:
            self.card = Card("1234567890123456", "123", 2008, 9)
        self.assertTrue("Card invalid" in str(context.exception))

    def testValidCard (self):
        self.card = Card("1234567890123456", "123", 2099, 7)
        self.assertEqual(self.card.number, "1234567890123456")
        self.assertEqual(self.card.cvc, "123")
        self.assertEqual(self.card.expiry_year, 2099)
        self.assertEqual(self.card.expiry_month, 7)