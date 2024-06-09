from typing import List, Dict, Callable

chores: List[Dict[str, bool]] = []
keep_session: bool = True

def add_chore():
    return

def list_chores():
    return

def update_chore():
    return

def complete_chore():
    return

def delete_completed_chores():
    return

def end_session():
    return

def loadOptions():
    for index, option in enumerate(user_options):
        option_number = index + 1
        option_text, _ = option.values() 
        print(f"{option_number}. {option_text}")

def start_session():
    try:
        loadOptions()

        user_selected_option = int(input("Chose a valid option:"))
        selected_option_index = user_selected_option - 1
        selected_function = user_options[selected_option_index]["function"]
        selected_function()

    except Exception:
        print(f"Error: {Exception}")

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
