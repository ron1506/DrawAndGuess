import sqlite3


class Users:
    """
        Creates database with users table includes:
        create query
        insert query
        select query
    """

    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        # print("Opened database successfully")
        # print("Table created successfully")
        #self.conn.commit()

    def __str__(self):
        return "table  name is ", self.__tablename

    def get_table_name(self):
        return self.__tablename

    def insert_user(self, username, password, email):
        """

        :param username:
        :param password:
        :param email:
        :return:
        """
        print("i am inserting the user")
        insert_query = "INSERT INTO Users (username, password, email) \
              VALUES (?, ?, ?)"
        self.conn.execute(insert_query, (username, password, email))
        print("I have inserted the user, now lets check")
        print(list(self.conn.execute('SELECT * FROM Users WHERE email=?', (email,))))
        self.conn.commit()

    def to_register(self, username, password, email):
        """
        the function that handles the registration.
        :param username:
        :param email:
        :param password:
        :return:
        """
        row_username = list(self.conn.execute('SELECT * FROM Users WHERE username=?', (username,)))
        row_email = list(self.conn.execute('SELECT * FROM Users WHERE email=?', (email,)))
        if len(row_username) > 0 or len(row_email) > 0:
            return False
        self.insert_user(username, password, email)
        return True

    def to_log_in(self, username, password):
        """
        the function that handles the log in.
        :param username:
        :return:
        """
        if username == "" or password == "":  # all fields must be filled.
            return False
        row_username = list(self.conn.execute('SELECT * FROM Users WHERE username=?', (username,)))
        if row_username != [] and row_username[0][1] == password:
            return True
        return False



