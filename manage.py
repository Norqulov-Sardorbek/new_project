from models import Todos,Singleton
from auth import login,register
from db import get_all_todos,get_one_todo

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
            if isinstance(response, list):
                for index, todo in enumerate(response):
                    print(f'-------------{index+1}-todo---------------')
                    print(f'Todo\'s title is: {todo[1]} \nTodo\'s description is: {todo[2]} \nPriority is: {todo[3]}')
        elif answer == '3':
            user=Singleton.get_instance()
            if not user:
                continue
            response = get_all_todos(user)
            if isinstance(response, list):
                for index, todo in enumerate(response):
                    print(f'-------------{index+1}-todo---------------')
                    print(f'Todo\'s title is:{todo[0]}  {todo[1]} \nTodo\'s description is: {todo[2]} \nPriority is: {todo[3]}')
            Todos.update_todo(len(response))
        elif answer == '4':
            user=Singleton.get_instance() 
            if not user:
                continue
            response = get_all_todos(user)
            if isinstance(response, list):
                for index, todo in enumerate(response):
                    print(f'-------------{index+1}-todo---------------')
                    print(f'Todo\'s title is: {todo[1]} \nTodo\'s description is: {todo[2]} \nPriority is: {todo[3]}')
            Todos.delete_todo(len(response))
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