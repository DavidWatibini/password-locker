#!/usr/bin/env python3.6
from user import User
from  credentials import Credential

def create_account(login_account,login_username,credential_detail):

    """
    function to create a new account
    """

    new_user = User(login_account,login_username,)
    new_password = Credential(credential_detail)

    return new_user
    return new_password

def save_details(detail):

    """
    function to save save_details
    """
    detail.save_detail()

def save_creadential(credential_detail):

    """
    function to save passwords
    """
    credential_detail.save_creadential()


def display_all_details():

    """
    function used toreturn all saved save_details
    """
    return User.display_all_details
