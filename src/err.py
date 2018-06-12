# -*- coding: utf-8 -*-
__author__ = '''
       ________  ________   __
      / /  _/  |/  /  _/ | / /
 __  / // // /|_/ // //  |/ / 
/ /_/ // // /  / // // /|  /  
\____/___/_/  /_/___/_/ |_/ '''


class Error(BaseException):
    pass


class DBError(Error):
    pass


class ConnectDatabaseError(DBError):
    pass


class DatabaseLoginError(ConnectDatabaseError):
    pass


class DatabaseNameError(ConnectDatabaseError):
    pass


class DatabaseHostError(ConnectDatabaseError):
    pass


class DatabaseUnknownError(DBError):
    pass

