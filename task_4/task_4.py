from pathlib import Path

def parse_input(user_input: str):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.lower(), args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Помилка: команда 'add' очікує 2 аргументи: add <ім'я> <телефон>."
    name, phone = args[0], args[1]
    key = name.lower()
    contacts[key] = {"name": name, "phone": phone}
    return "Contact added."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Помилка: команда 'change' очікує 2 аргументи: change <ім'я> <новий_телефон>."
    name, new_phone = args[0], args[1]
    key = name.lower()
    if key not in contacts:
        return f"Помилка: контакт '{name}' не знайдено."
    contacts[key]["phone"] = new_phone
    return "Contact updated."

def show_phone(args, contacts):
    if len(args) < 1:
        return "Помилка: команда 'phone' очікує 1 аргумент: phone <ім'я>."
    name = args[0]
    key = name.lower()
    if key not in contacts:
        return f"Помилка: контакт '{name}' не знайдено."
    return contacts[key]["phone"]

def show_all(contacts):
    if not contacts:
        return "Немає збережених контактів."
    lines = []
    for key in sorted(contacts.keys()):
        entry = contacts[key]
        lines.append(f"{entry['name']}: {entry['phone']}")
    return "\n".join(lines)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "":
            print("Invalid command.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()