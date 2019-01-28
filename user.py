class User:
    """

    Class that will generate new instances of users

    """

    user_detail = []

    def save_detail(self):

        """
        the method saves detail objects into the empty user_detail array
        """
        User.user_detail.append(self)

    def __init__(self,login_account,login_username):

        """
        the __init__method helps us define properties for our objectsself.

        """

        self.login_account = login_account
        self.login_username = login_username

        """
        arguments for our __init__method will include the following.

        """
