import unittest
from rabbit import Rabbit

class TestSuite(unittest.TestCase):

    def test(self):
        rabbit = Rabbit()
        rabbit.sendMessage()
        things = rabbit.relayMessage()
        things = things.decode("unicode_escape")
        self.assertFalse(things != "Hello World!")


def main():
	unittest.main()

if __name__ == "__main__":
    main()
