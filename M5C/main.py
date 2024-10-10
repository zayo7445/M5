import sys
from pathlib import Path
import json


class User:
    def __init__(self, username: str, password: str, data: dict):
        self.username = username
        self.password = password
        self.data = data

    def add_item(self, item: str):
        if item:
            self.data["items"].append(item)
            print(f"'{item}' added to items")
        else:
            print("Invalid item")

    def delete_item(self, item: str):
        if item in self.data["items"]:
            self.data["items"].remove(item)
            print(f"'{item}' removed from items")
        else:
            print("Item not found")

    def list_items(self):
        if self.data["items"]:
            print("\nThese are your items")
            for i, item in enumerate(self.data["items"], 1):
                print(f"{i}) {item}")
        else:
            print("\nYou have no items")


class Lagra:
    def __init__(self):
        self.user = None
        self.data = self.get_data()

    @staticmethod
    def get_data(path=Path("data.json")) -> dict:
        if path.exists():
            with open(path, "r") as file:
                data = json.load(file)
                return data
        return {}

    def save_data(self, path=Path("data.json")):
        if self.user:
            self.data[self.user.username]["items"] = self.user.data.get("items")
        with open(path, "w") as file:
            json.dump(self.data, file)

    @staticmethod
    def get_option(options: list) -> str:
        while (option := input("Option: ").strip()) not in options: print("\nInvalid input\n")
        return option

    def manage(self):
        while True:
            self.user.list_items()
            print("\nActions")
            print("a) Add item")
            print("d) Delete item")
            print("q) Log out\n")
            option = self.get_option(["a", "d", "q"])
            if option == "a":
                item = input("\nAdd item: ").strip()
                self.user.add_item(item)
            elif option == "d":
                item = input("\nDelete item: ").strip()
                self.user.delete_item(item)
            elif option == "q":
                self.save_data()
                break

    def credentials(self) -> bool:
        username = input("\nUsername: ")
        password = input("Password: ")
        data = self.data.get(username)
        if data and data.get("password") == password:
            self.user = User(username, password, data)
            print(f"\nWelcome {username}")
            self.manage()
            self.user = None
            return True
        return False

    def log_in(self):
        while not self.credentials():
            print("\nInvalid username or password")
            print("r) Retry")
            print("b) Back")
            print("q) Quit\n")
            option = self.get_option(["r", "b", "q"])
            if option == "b":
                break
            elif option == "q":
                sys.exit()

    def register(self):
        while True:
            username = input("\nUsername: ")
            if username not in self.data:
                password = input("Password: ")
                self.data[username] = {"password": password, "items": []}
                self.save_data()
                print(f"\nAccount created for {username}")
                break
            print("Username already exists")

    def main(self):
        while True:
            print("\nWelcome to Lagra™\n")
            print("l) Log in")
            print("r) Register")
            print("q) Quit\n")
            option = self.get_option(["l", "r", "q"])
            if option == "r":
                self.register()
                continue
            elif option == "q":
                sys.exit()
            self.log_in()


if __name__ == "__main__":
    lagra = Lagra()
    lagra.main()
