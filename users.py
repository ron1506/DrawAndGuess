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
        conn = sqlite3.connect('users.db')
        print("Opened database successfully")
        query_str = "CREATE TABLE " + self.__tablename + " (" + self.__username +  "	TEXT NOT NULL UNIQUE, " +\
            self.__password + "	TEXT NOT NULL," + self.__email+ " TEXT NOT NULL UNIQUE,PRIMARY KEY(" + username + "));"
        conn.execute("drop table users")
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
        insert_query = "INSERT INTO " + self.__tablename + " (" + self.__username + "," + self.__password + "," + self.__email +") VALUES" \
                   "(" + "'" + password + "'" + "," + "'" + username + "'" + "," + "'" + email + "'" + ");"
        print(insert_query)
        conn.execute(insert_query)
        conn.commit()
        conn.close()
        print("Record created successfully")

    def check_password(self, username, email, password):
        """

        :param username:
        :param email:
        :param password:
        :return:
        """
        user = self.select_user_by_username(username, email)
        if password in user:
            return True
        return False

    def is_username_exist(self, username, email):
        """

        :param username:
        :return:
        """
        conn = sqlite3.connect('users.db')
        print("Opened database successfully")
        str1 = "SELECT username, password, email FROM" + self.__tablename + " WHERE username = " + username + "AND email = " + email
        cursor = conn.execute(str1)
        ok = True
        for row in cursor:
            ok = ok and username == row[0]
            # print("password = ", row[1])
            ok = ok and email == row[2]

        print("Operation done successfully")
        conn.close()
        return ok





u1 = Users()
u1.insert_user('ron', '1234', 'a@a.com')