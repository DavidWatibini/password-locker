import unittest
from user import User
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

    def test_init(self):

        """
        used to test if the objects have been initialized properly

        """

        self.assertEqual(self.new_user.login_account,"facebook")
        self.assertEqual(self.new_user.login_username,"watibini")

if __name__ == '__main__':
    unittest.main()
