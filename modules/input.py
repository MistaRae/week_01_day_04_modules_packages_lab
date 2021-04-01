
def select_an_option(input):
    option = input
    input("Select an option 1, 2, 3, 4, 5, 6, 7 or (Q)uit: ")
    return option

print(select_an_option(input))

def search_task_by_description (input):
    task_to_add: input
    input("Enter task description to search for: ")
    return task_to_add

def enter_task_duration (input):
    new_task_duration = input
    int(input("Enter task duration: "))
    return new_task_duration

def enter_task_description (input):
    new_task_description = input
    input("Enter description: ")
    return new_task_description

def enter_time_taken(input):
    new_time_taken = input
    int(input("Enter time taken: "))
    return new_time_taken
