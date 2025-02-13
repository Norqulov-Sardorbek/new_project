from utils import Response, hash_password, match_password,  validation
from models import User, Singleton


def register():
    username = input('Enter new username: ')
    password = input('Enter new password: ')
    role = 'user'
    
    hashed_password = hash_password(password)
    user = User(username, hashed_password, role)
    
    if validation(user) is None:
        return  
    
    id= user.save()
    
    Singleton.get_instance(username,role,id)  
    

def login():
    username = input('Enter your username: ')
    user_data=User.load(username)
    if not user_data:
        print(Response(status='error',message='This user not exists!'))
        return
    password = input('Enter your password: ')
    if not match_password(password,user_data[2]):
        print(Response(status='error',message='Wrong password!'))
        return
    Singleton.get_instance(username,user_data[3],user_data[0]) 
   
    print(f'Welcome user {username}')
    return
        
    


def logout():
    Singleton._instance=None