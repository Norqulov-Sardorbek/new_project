from models import Todos,Singleton
from auth import login,register
from db import get_all_todos
from utils import displayer

def main():
    while True:
        print('-------------Main Menu------------')
        print('1 => Create Todo')
        print('2 => Read Todos')
        print('3 => Update Todo')
        print('4 => Delete Todo')
        print('5 => Login')
        print('6 => Register')
        print('q => Exit')
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
            response = get_all_todos(user)
            displayer(response)
        elif answer == '3':
            user=Singleton.get_instance()
            if not user:
                continue
            response = get_all_todos(user)
            displayer(response)
            Todos.update_todo(len(response))
        elif answer == '4':
            user=Singleton.get_instance() 
            if not user:
                continue
            response = get_all_todos(user)
            displayer(response)
            Todos.delete_todo()
        elif answer == '5':
            login()
        elif answer == '6':
            register()
        elif answer == 'q':
            print('Goodbye!')
            break
        else:
            print('Invalid choice, please try again.')

if __name__ == '__main__':
    main()