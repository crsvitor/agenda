from typing import List, Dict, Callable

chores: List[Dict[str, bool]] = []
keep_session: bool = True

def add_chore():
    chore = input("New chore title: ")
    dict_chore = {
        "title": chore,
        "completed": False
    }
    chores.append(dict_chore)
    print("Chore added")

def list_chores():
    for index, chore in enumerate(chores):
        chore_number = index + 1
        title, completed = chore.values()
        message = f"{chore_number}. [✓] {title}" if completed else f"{chore_number}. [ ] {title}"
        print(message)

def update_chore():
    chore_number = int(input("Chore number: "))
    title = input("New chore title: ")
    selected_option_index = chore_number - 1
    chores[selected_option_index]["title"] = title
    print(f"Chore {chore_number} updated")

def complete_chore():
    chore_number = int(input("Chore number: "))
    selected_option_index = chore_number - 1
    chores[selected_option_index]["completed"] = True
    print(f"Chore {chore_number} completed")

def delete_completed_chores():
    for chore in chores:
        is_chore_completed = chore["completed"]
        if (is_chore_completed):
            chores.remove(chore)
    print("Completed chores removed")
    

def end_session():
    global keep_session 
    keep_session = False

def list_chore_options():
    for index, option in enumerate(user_options):
        option_number = index + 1
        option_text, _ = option.values() 
        print(f"{option_number}. {option_text}")

def start_session():
    while keep_session:
        try:
            print("Welcome to terminal chore list:")
            list_chore_options()

            user_selected_option = int(input("Chose a option: "))
            selected_option_index = user_selected_option - 1
            selected_function = user_options[selected_option_index]["function"]
            selected_function()

        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            print("\n")

    print("Session has finished")


user_options: List[Dict[str, Callable]] = [
    {
        "text": "Add chore",
        "function": add_chore, 
    },
    {
        "text": "List chores",
        "function": list_chores,
    },
    {
        "text": "Update chore",
        "function": update_chore,
    },
    {
        "text": "Complete chore",
        "function": complete_chore,
    },
    {
        "text": "Delete completed chores",
        "function": delete_completed_chores,
    },
    {
        "text": "End session",
        "function": end_session,
    }
]

start_session()
