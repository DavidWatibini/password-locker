import unittest
from user from User
class TestUser(unittest.TestCase):

    """
    Test class that defines test cases for the user class behaviours,
    the arguments help in creating test cases.

    """

    def setUp(self):

        """
        this method runs before each test case, carries the instrctions of what is to be done

        """

        self.new_user = User("facebook","watibini")
