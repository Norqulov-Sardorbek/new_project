import bcrypt
import psycopg2



db_info = {
    "database": "lesson",
    "user": "postgres",
    "password": "123",
    "host": "localhost",
    "port": 5432,
}
class Response:
    def __init__(self,status,message):
        self.status=status
        self.message=message
    def __str__(self):
         return self.message




def hash_password(raw_password: str):
    raw_password = raw_password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(raw_password, salt).decode('utf-8')


def match_password(raw_password: str, hashed_password):
    raw_password = raw_password.encode('utf-8')
    hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(raw_password, hashed_password)

def priority_picker():
    print('------Priority-------')
    print('1=> low')
    print('2=> medium')
    print('3=> high')
    chose=input('Which priority you wanna choose: ')
    if chose=='1':
        return 'low'
    elif chose=='2':
        return 'medium'
    elif chose=='3':
        return 'high'
    else:
        print('You have to chose one of them!')
def del_user(username):
    del_query = '''SET search_path TO todo; DELETE FROM user_info WHERE username = %s;'''
    with psycopg2.connect(**db_info) as conn:
        with conn.cursor() as cur:
           
            cur.execute(del_query, (username,))    
            if cur.rowcount > 0:
                print(Response(status='success', message='User deleted successfully'))
            else:
                print(Response(status='error', message='User not found'))
def set_admin(username):
    update_user_query = '''set search_path to todo; update user_info set role='superuser'where username = %s returning id;'''
    with psycopg2.connect(**db_info) as conn:
        with conn.cursor() as cur:
            cur.execute(update_user_query,(username,))
            todos = cur.fetchall()
            if not todos:
                print(Response(status='error', message=f'Couldn\'t update role of user {username}'))
            print(Response(status='succes',message='Role changed to Superuser'))
    
  
    



def displayer(response,todo=True):
    if todo and isinstance(response, list):
        for index, todo in enumerate(response):
            print(f'-------------{index+1}-todo---------------')
            print(f'Todo\'s title is: {todo[1]} \nTodo\'s description is: {todo[2]} \nPriority is: {todo[3]}')
    if not todo and isinstance(response,list):
        for index, user in enumerate(response):
            print(f'User {index+1} : {user[1]}, {user[3]}')


def validation(user):
    if not user.username:
        print(Response(status='error',message='Username is required'))
        return

    if not user.password:
        print(Response(status='error',message='Password is required'))
        return
    return 'eflkamfl'
