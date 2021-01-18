import sqlite3


class Users:
    """
        Creates database with users table includes:
        create query
        insert query
        select query
    """

    def __init__(self, tablename="users", password="password", username="username", email="email"):
        self.__tablename = tablename
        self.__password = password
        self.__username = username
        self.__email = email
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        query_str = "CREATE TABLE IF NOT EXISTS " + tablename + "(" + self.__username + " " + \
                    " TEXT PRIMARY KEY AUTOINCREMENT ,"
        query_str += " " + self.__password + " TEXT    NOT NULL ,"
        query_str += " " + self.__email + " TEXT    NOT NULL );"

        # conn.execute("drop table users")
        conn.execute(query_str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def __str__(self):
        return "table  name is ", self.__tablename

    def get_table_name(self):
        return self.__tablename

    def insert_user(self, username, password, email):
        conn = sqlite3.connect('test.db')
        insert_query = "INSERT INTO " + self.__tablename + " (" + self.__password + "," + self.__username + "," + self.__email +") VALUES" \
                   "(" + "'" + password + "'" + "," + "'" + username + "'" + "," + "'" + email + "'" + ");"
        print(insert_query)
        conn.execute(insert_query)
        conn.commit()
        conn.close()
        print("Record created successfully")

    def is_username_exist(self, new_username):
        return True

    def is_email_exist(self, new_eamil):
        return True

    def check_password(self, password):
        pass

    def select_user_by_username(self, username):
        """

        :param username:
        :return:
        """
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str1 = "select * from users;"
        strsql = "SELECT password, username, email from " + self.__tablename + " where " + self.__username + "=" \
            + str(username)
        print(str1)
        cursor = conn.execute(str1)
        for row in cursor:
            print("password = ", row[0])
            print("username = ", row[1])
            print("email = ", row[2])
        print("Operation done successfully")
        conn.close()



