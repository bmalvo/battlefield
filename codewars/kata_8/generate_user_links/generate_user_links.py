"""Your task is to create userlinks for the url, you will be given a username 
and must return a valid link."""
from urllib.parse import quote


def generate_link(user_name):
    """output link for the user name"""
    return  f'http://www.codewars.com/users/{quote(user_name)}'
