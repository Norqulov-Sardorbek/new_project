import bcrypt
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
    
def role_pick():
    print('--------Roles------')
    print('1=> User')
    print('2=> Superuser')
    chose=input('Chose your role: ')
    if chose=='1':
        return 'user'
    elif chose=='2':
        return 'superuser'
    else:
        print('You have to chose one of them!')

def displayer(response):
    if isinstance(response, list):
                for index, todo in enumerate(response):
                    print(f'-------------{index+1}-todo---------------')
                    print(f'Todo\'s title is: {todo[1]} \nTodo\'s description is: {todo[2]} \nPriority is: {todo[3]}')

def validation(user):
    if not user.username:
        print(Response(status='error',message='Username is required'))
        return

    if not user.password:
        print(Response(status='error',message='Password is required'))
        return
    return 'eflkamfl'
