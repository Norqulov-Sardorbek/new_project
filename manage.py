from models import Todos,Singleton
from auth import login,register,logout
from db import get_all_todos,get_all_user
from utils import displayer,set_admin,del_user


def user_menu():
    while True:
        user=Singleton.get_instance() 
        print('-------------Main Menu------------')
        print('1 => Create Todo')
        print('2 => Read Todos')
        print('3 => Update Todo')
        print('4 => Delete Todo')
        print('q => Log out')
        answer = input('Enter your choice: ')

        if answer == '1':
            user=Singleton.get_instance()
            if not user:
                continue
            Todos.create_todo(user)
        elif answer == '2':
            user=Singleton.get_instance()
            if not user:
                continue
            displayer(response)
        elif answer == '3':
            user=Singleton.get_instance()
            if not user:
                continue
            displayer(response)
            Todos.update_todo(len(response))
        elif answer == '4':
            user=Singleton.get_instance()
            if not user:
                continue
            response = get_all_todos(user)
            displayer(response)
            Todos.delete_todo()
        elif answer == 'q':
            logout()
            landing_page()
        else:
            print('Invalid choice, please try again.')
def admin_menu():
    while True:
        print('-----Admin Menu-----')
        print('1=> Set as admin')
        print('2=> Create Todos')
        print('3=> Read Todos')
        print('4=> Update todos')
        print('5=> Delete todos')
        print('6=> Update User\'s info')
        print('7=> Delete User\'s')
        print('q=> Logout')
        answer = input('Enter your choice: ')
        if answer == '1':
            displayer(get_all_user(),False)
            username=input('Enter username which you want to make superuser: ')
            set_admin(username)
        elif answer == '2':
            user=Singleton.get_instance()
            if not user:
                continue
            Todos.create_todo(user)
        elif answer == '3':
            user=Singleton.get_instance()
            if not user:
                continue
            displayer(response)
        elif answer == '4':
            user=Singleton.get_instance()
            if not user:
                continue
            displayer(response)
            Todos.update_todo(len(response))
        elif answer == '5':
            user=Singleton.get_instance()
            if not user:
                continue
            response = get_all_todos(user)
            displayer(response)
            Todos.delete_todo()
        elif answer == '6':
            pass
        elif answer == '7':
            displayer(get_all_user(),False)
            username=input('Enter username which you want to make superuser: ')
            del_user(username)
        elif answer == 'q':
            logout()
            landing_page()
        else:
            print('Invalid choice, please try again.')

def landing_page():
    while True:
       
        print('Login/Sign up Page')
        print('1=> Login')
        print('2=> Register')
        print('q=> Exit')
        answer = input('Enter your choice: ')

        if answer == '1':
            login()
            user=Singleton.get_instance()
            if user.role=='user':
                user_menu()
            else:
                admin_menu()
        elif answer == '2':
            register() 
        elif answer == 'q':
            print('Goodbye')
            break
        else:
            print('Invalid choice, please try again.')


if __name__ == '__main__':
    landing_page()