from sqlite3 import *


# TODO : rewrite db using ORM
class Manager:

    def __init__(self):
        self.__create_tables()

    def __create_tables(self):
        cur = self.get_connection()
        cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER,chat_id INTEGER)')
        cur.execute('CREATE TABLE IF NOT EXISTS temp(id INTEGER,chat_id INTEGER)')

    def add_user(self, code, chat_id):
        cur = self.get_connection()
        cur.execute('INSERT INTO temp(id,chat_id) VALUES (?,?)', (code, chat_id))

    def verify(self, code):
        cur = self.get_connection()
        chat_id = cur.execute('SELECT chat_id FROM temp WHERE id=?', (code,)).fetchone()[0]
        cur.execute('INSERT INTO users(id,chat_id) VALUES (?,?)', (code, chat_id,))
        cur.execute('DELETE FROM temp WHERE id=?', (code,))
        cur.execute('CREATE TABLE IF NOT EXISTS w{}(word TEXT)'.format(chat_id))

    def add_word(self, code, word, chat_id=None):
        cur = self.get_connection()
        if (chat_id != None):
            cur.execute('INSERT INTO w{}(word) VALUES (?)'.format(chat_id), (word,))
        else:
            chat_id = cur.execute('SELECT chat_id FROM users WHERE id=?', (code,)).fetchone()[0]
            cur.execute('INSERT INTO w{}(word) VALUES (?)'.format(chat_id), (word,))

    def add_temp(self, temp_code, chat_id):
        cur = self.get_connection()
        if cur.execute('SELECT * FROM temp where id=?', (temp_code,)).fetchall() != None:
            cur.execute('INSERT INTO temp(id,chat_id) VALUES (?,?)', (temp_code, chat_id,))
        else:
            cur.execute('UPDATE temp SET id=? WHERE chat_id=?', (temp_code, chat_id,))

    def check_temp(self, temp_code):
        cur = self.get_connection()
        return cur.execute('SELECT * FROM TEMP where id=?', (temp_code,)).fetchall() != []

    def check_code(self, code):
        cur = self.get_connection()
        return cur.execute('SELECT * FROM users where id=?', (code,)).fetchall() != []

    def get_list_of_words(self, chat_id):
        pass

    def get_all_words(self):
        pass

    def get_connection(self):
        return connect('Ext.db', isolation_level=None)
