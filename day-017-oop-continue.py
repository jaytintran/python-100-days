class User:
    # Initialize the object according to the class aka a constructor
    def __init__(self, user_id, user_name):
        print("New user is being created...")
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0
        self.level = 1
        self.health = 100

    # Create an object method
    def greeting(self):
        print(f"ID: {self.id}")
        print(f"NAME: {self.name}")
        print(f"FOLLOWERS: {self.followers}")
        print(f"FOLLOWING: {self.following}")
        print(f"LEVEL: {self.level}")
        print(f"HEALTH: {self.health}")

    def enter_beast_mode(self):
        self.health += 1000
        self.level += 100

    def learn_magic(self):
        if self.level < 10:
            print("No you can't learn magic. Your level is: {self.level} which is too low")
            return False
        else:
            return True

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "Jay")
user1.enter_beast_mode()

user2 = User("002", "Jayce")

user1.follow(user2)

user1.greeting()
user2.greeting()

