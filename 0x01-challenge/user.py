#!/usr/bin/python3
""" Module for user opject """


class User():
    """ User Class """

    def __init__(self):
        """ Intlization of user """
        self.__email = None

    @property
    def email(self):
        """ Emeil property """
        return self.__email

    @email.setter
    def email(self, value):
        """ Setter for email """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
