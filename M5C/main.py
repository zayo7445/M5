import sys
import json


def get_data():
    with open("data.json", "r") as file:
        data = json.load(file)
        return data


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.data = get_data()
        self.items = self.data[username]["items"]

    def list_items(self):
        if self.items:
            print("These are your items:")
            for i, item in enumerate(self.items, 1):
                print(f"{i}) {item}")
        else:
            print("You have no items.")

    def add_item(self, item: str):
        self.items.append(item)
        self.save_items()

    def delete_item(self, item: str):
        if item in self.items:
            self.items.remove(item)
            self.save_items()
        else:
            print("Item does not exist.")

    def save_items(self):
        data = self.data
        data[self.username]["items"] = self.items
        with open("data.json", "w") as file:
            json.dump(data, file)


class Lagra:
    def __init__(self):
        self.user = None
        self.data = get_data()

    @staticmethod
    def welcome():
        print("Welcome to Lagra™")
        print("  l) Login")
        print("  q) Quit")

    @staticmethod
    def invalid():
        print("Invalid username or password")
        print("  r) Retry")
        print("  q) Quit")

    @staticmethod
    def actions():
        print("Select an action")
        print("  a) Add item")
        print("  d) Delete item")
        print("  l) List items")
        print("  q) Log out")

    @staticmethod
    def get_option(options: list) -> str:
        while True:
            opt = input("Option: ").lower()
            if opt in options:
                return opt
            else:
                print("Invalid input. Try again.")

    def manage(self):
        while True:
            self.actions()
            opt = self.get_option(["a", "d", "l", "q"])
            if opt == "a":
                item = input("Add item: ")
                self.user.add_item(item)
            elif opt == "d":
                item = input("Delete item: ")
                self.user.delete_item(item)
            elif opt == "l":
                self.user.list_items()
            elif opt == "q":
                self.main()

    def credentials(self, username: str, password: str):
        data = self.data
        if username in data:
            if data[username]["password"] == password:
                return True
        return False

    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        if self.credentials(username, password):
            self.user = User(username, password)
            print(f"Welcome {username}")
            self.manage()

    def main(self):
        self.welcome()
        opt = lagra.get_option(["l", "q"])
        if opt == "l":
            while True:
                self.login()
                self.invalid()
                opt = self.get_option(["r", "q"])
                if opt == "q":
                    sys.exit()
        elif opt == "q":
            sys.exit()


if __name__ == "__main__":
    lagra = Lagra()
    lagra.main()