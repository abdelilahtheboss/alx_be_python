task = input("Enter your task: ")
priority = input("priority (high/medium/low)")
time_bound = input("Is it time_bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"reminder: '{task}' is a {priority} priority task kthat requires immediate attention today!")
        else:
            print(f"note: '{task}' is a {priority} priority taskk. consider  completing it when you have free time.")
    case "medium": 
        if time_bound == "yes":
            print(f"reminder: '{task}' is a {priority} priority task kthat requires immediate attention today!")
        else:
            print(f"note: '{task}' is a {priority} priority taskk. consider  completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"reminder: '{task}' is a {priority} priority task kthat requires immediate attention today!")
        else:
            print(f"reminder: '{task}' is a {priority} priority task kthat requires immediate attention today!")