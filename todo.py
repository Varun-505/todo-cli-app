import json

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add task\n2. Show tasks\n3. Complete task\n4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            task = input("Enter task: ")
            tasks.append({"task": task, "done": False})
            save_tasks(tasks)
        elif choice == "2":
            for i, t in enumerate(tasks):
                status = "✔" if t["done"] else "✘"
                print(f"{i+1}. {t['task']} [{status}]")
        elif choice == "3":
            index = int(input("Task number: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["done"] = True
                save_tasks(tasks)
        elif choice == "4":
            break

main()
