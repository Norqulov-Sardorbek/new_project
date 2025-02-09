import psycopg2
from models import db_info
from utils import Response


def get_all_todos(user):
    if user.role == 'superuser':
        get_todo_query = '''
        SET search_path TO todo;
        SELECT * FROM todos;
        '''
        query_params = ()
    else:
        get_todo_query = '''
        SET search_path TO todo;
        SELECT * FROM todos
        WHERE userid = (SELECT id FROM user_info WHERE username = %s);
        '''
        query_params = (user.username,)

    with psycopg2.connect(**db_info) as conn:
        with conn.cursor() as cur:
            cur.execute(get_todo_query, query_params)
            todos = cur.fetchall()
            if not todos:
                return Response(status='error', message='No saved todos yet!')
            return todos


def get_one_todo(user, todo_id):
    get_todo_query = '''
    SET search_path TO todo;
    SELECT * FROM todos
    WHERE id = %s;
    '''

    with psycopg2.connect(**db_info) as conn:
        with conn.cursor() as cur:
            cur.execute(get_todo_query, (todo_id,))
            todo = cur.fetchone()
            if todo is None:
                return Response(status='error', message='No todo found with this ID')
            return f'Todo ID: {todo[0]}\nTitle: {todo[1]}\nDescription: {todo[2]}\nPriority: {todo[3]}'
