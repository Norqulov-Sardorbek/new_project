import psycopg2
from typing import NamedTuple
from utils import Response,priority_picker

db_info = {
    "database": "lesson",
    "user": "postgres",
    "password": "123",
    "host": "localhost",
    "port": 5432,
}

class Singleton:
    _instance = None

    @classmethod
    def get_instance(cls, username=None, role=None,id=None):
        if cls._instance is None:
            if username is None or role is None:
                print("Login first")
                return False
            cls._instance = object.__new__(cls)

        if username and role and id:
            cls._instance.username = username
            cls._instance.role = role
            cls._instance.id = id

        return cls._instance




    




class User:
    def __init__(self, username: str, password: str,role:str):
        self.username = username
        self.password = password
        self.role=role
    @staticmethod
    def load(username):
        get_users='''
SET SEARCH_PATH TO todo;
SELECT * FROM user_info WHERE username = %s;
'''
        with psycopg2.connect(**db_info)as conn:
            with conn.cursor() as cur:
                cur.execute(get_users,(username,))
                info=cur.fetchone()
                if not info:
                    return 
                return info
    
    def save(self):
        set_users = '''set search_path to todo; INSERT INTO user_info (username, password, role) VALUES (%s, %s, %s) RETURNING id;'''
        check_user_query = "set search_path to todo; SELECT * FROM user_info WHERE username = %s;"
        with psycopg2.connect(**db_info) as conn:
            with conn.cursor() as cur:
                cur.execute(check_user_query, (self.username,))
                if cur.fetchone():
                    print(Response(status='error', message='User already exists'))
                    return

                cur.execute(set_users, (self.username, self.password, self.role))
                
                user_id = cur.fetchone() 
                if user_id:
                    print(Response(status='success', message=f'User saved to database!'))
                    return user_id
                else:
                    print(Response(status='error', message='User could not be saved'))
                    return



class Todo(NamedTuple):
    title: str
    description: str
    priority: str


class Todos:
    def __init__(self, todo: Todo):
        self.todo = todo
        user=Singleton()
    @staticmethod
    def create_todo(user):
        title = input('Enter todo title: ')
        description = input('Enter todo description: ')
        priority = priority_picker()
        if priority is None:
            return
        todo=Todo(title,description,priority)
        insert_query = '''
        SET SEARCH_PATH TO todo;
        INSERT INTO todos (title, description, priority,userid)
        VALUES (%s, %s, %s,%s);
        '''
        with psycopg2.connect(**db_info) as conn:
            with conn.cursor() as cur:
                cur.execute(insert_query, (todo.title, todo.description, todo.priority,user.id))
                
                print(Response(status='success', message=f"Todo saved successfully !"))

    @staticmethod
    def update_todo(len):
        todo_id =int( input('Enter todo id you want to update: '))
        if todo_id >len:
            print(Response(status='error',message='You are trying to update not exist todo'))
            return
        title=input('Enter new title: ')
        new_description = input('Enter new description: ')
        new_priority = priority_picker()
        if new_priority is None:
            return
        update_query = '''
        SET SEARCH_PATH TO todo;
        UPDATE todos
        SET title=%s, description = %s, priority = %s
        WHERE id = %s;
        '''
        with psycopg2.connect(**db_info) as conn:
            with conn.cursor() as cur:
                cur.execute(update_query, (title,new_description, new_priority, todo_id))
                
                if cur.rowcount == 0:
                    print( Response(status='error', message='No todo found with this ID to update.'))
                    return
                print(Response(status='success', message='Todo updated successfully!'))
                return

    @staticmethod
    def delete_todo(len):
        todo_id=input('Which todo you want to updade: ')
        if todo_id >len:
            print(Response(status='error',message='You are trying to delete not exist todo'))
            return
        delete_query = '''
        SET SEARCH_PATH TO todo;
        DELETE FROM todos
        WHERE id = %s;
        '''
        with psycopg2.connect(**db_info) as conn:
            with conn.cursor() as cur:
                cur.execute(delete_query, (todo_id,))
                
                if cur.rowcount == 0:
                    return Response(status='error', message='No todo found with this ID to delete.')
                return Response(status='success', message='Todo deleted successfully!')