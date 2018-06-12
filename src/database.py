# -*- coding: utf-8 -*-
import pymysql
from src import err

__author__ = '''
       ________  ________   __
      / /  _/  |/  /  _/ | / /
 __  / // // /|_/ // //  |/ / 
/ /_/ // // /  / // // /|  /  
\____/___/_/  /_/___/_/ |_/ '''


class DB(object):
    @staticmethod
    def __get_db():
        try:
            db = pymysql.connect(**{
                "host": "Host",
                "user": "User",
                "password": "PassWord",
                "database": "DataBaseName",
                'charset': 'utf8',
            })
        except pymysql.err.MySQLError as e:
            if e.args[0] == 1045:
                raise err.DatabaseLoginError(e.args[1])
            elif e.args[0] == 1049:
                raise err.DatabaseNameError(e.args[1])
            elif e.args[0] == 2003:
                raise err.DatabaseHostError(e.args[1])
            else:
                raise err.ConnectDatabaseError(e)
        except Exception as e:
            raise err.DatabaseUnknownError(e)
        return db

    # 执行一条sql语句,返回受影响的行数
    def exec(self, sql):
        cursor = self.__get_db().cursor()
        return cursor.execute(sql)

    def select(self):
        db = self.__get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM `TableName`")
        db.close()
        # return cursor.fetchone()
        # cursor.fetchmany(3)
        return cursor.fetchall()

    def insert(self, one, two, three):
        db = self.__get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO `TableName` (`column_1`, `column_2`, `column_3`) "
                       "VALUES (%s, %s, %s)", (one, two, three))
        db.close()

    def alter(self, one, two, id):
        db = self.__get_db()
        cursor = db.cursor()
        cursor.execute("ALTER TABLE `TableName` SET`column_1` = %s, `column_2` = %s "
                       "WHERE `TableName`.`id` = %s", (one, two, id))
        db.close()

    def delete(self, id):
        db = self.__get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM `TableName` WHERE `TableName`.`id` = %s", id)
        db.close()

    # 获取上一条自增的id
    def get_last_id(self, one, two, three):
        db = self.__get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO `TableName` (`column_1`, `column_2`, `column_3`) "
                       "VALUES (%s, %s, %s)", (one, two, three))
        db.close()
        return cursor.lastrowid

    # 显示mysql将要执行的sql语句
    def show_sql(self, one, two, id):
        db = self.__get_db()
        cursor = db.cursor()
        return cursor.mogrify(("ALTER TABLE `TableName` SET`column_1` = %s, `column_2` = %s "
                               "WHERE `TableName`.`id` = %s", (one, two, id)))

