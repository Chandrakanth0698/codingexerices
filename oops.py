class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        return self.name.upper()

    def age(self, current_year=2023):
        return current_year - self.birthyear


if __name__ == "__main__":
    chandu = User("chandu", 1999)
    print(chandu.age())
    print(chandu.get_name())
