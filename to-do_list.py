from termcolor import cprint

tasks = []

def print_menu():
    cprint ('\n--- 📋 To-Do List ---', 'cyan') 
    print ('1. View tasks')
    print ('2. Add task')
    print ('3. Remove task')
    print ('4. Quit')
    cprint ('----------------------', 'cyan')

def get_choice():
    while True:
        choice = input('Enter your choice (1-4): ').strip()
        valid_choices = ('1', '2', '3', '4')
        if choice in valid_choices:
            return choice
        else:
            cprint ('❌ Invalid choice! Please enter a number between 1 and 4.', 'red')
            
def view_tasks(tasks):
    if not tasks:
        print ('\n No tasks in the list.😊')
        return 
    
    cprint ('\n--- Your Tasks ---', 'cyan')
    for index, task in enumerate(tasks, start=1):
        print (f'{index}. {task}')
    cprint ('------------------', 'cyan')

def add_task(tasks):
    task = input ('\n Enter a new task: ').strip()
    if task:
        tasks.append(task)
        cprint (f' Task "{task}" added!🥳', 'green')
    else:
        cprint ('🚫 Task cannot be empty!', 'red')

def remove_task(tasks):
    if not tasks:
        print ('\n No tasks to remove.😊')
        return

    view_tasks(tasks)

    while True:
        try:
            task_number_input = input ('\nEnter the number of the task to remove \n OR type 0 to cancel: ').strip()
            
            if task_number_input.lower() == '0':
                cprint('🚫 Operation cancelled!!!', 'yellow')
                return

            task_number = int(task_number_input)

            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                cprint (f' Task "{removed_task}" removed successfully!🥳', 'green')
                break 
            else:
                cprint (f'🚫 Invalid task number! Please enter a number from 1 to {len(tasks)}.', 'red')
        
        except ValueError:
            cprint ('🚫 Invalid input! Please enter a valid task number.', 'red')

def main():
    cprint ('\nWelcome to your 📋 To-Do List!', 'magenta')
    while True:
        print_menu()

        choice = get_choice()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            cprint ('\n👋 Goodbye! Your tasks will not be forgotten.', 'green')
            print ()
            break

if __name__ == '__main__':
    main()