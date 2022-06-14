class User:
    def __init__(self,first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.status = "Bronze"
        self.is_rewards_member = False
        self.gold_card_points = 0

    def enroll(self):
        self.is_rewards_member = True
        print(self.is_rewards_member)
        self.gold_card_points += 200

    def membership(self):
        if self.gold_card_points >=200:
            self.status = "Gold"
            return f"Membership status: {self.status}"
        elif self.gold_card_points >=100:
            self.status = "Silver"
            return f"Membership status: {self.status}"
        else:
            return f"Membership status: {self.status}"

    def spend_points(self,amount):
        self.gold_card_points -= amount

    def display_info(self):
        return f"First Name: {self.first_name}| Last Name: {self.last_name}| Email: {self.email}| Age: {self.age}| Points Balance: {self.gold_card_points}| {self.membership()}"

# User's Profile
user_1 = User("Alex", "Valdez", "alex@email.com", 31,)
user_2 = User("John", "Doe", "john@email.com", 43)
user_3 = User("Bob", "Bunyon", "bob@email.com", 27)

# In the outer scope, create a user instance and call the display_info method to test.
# print(user_1.display_info())
# print(user_2.display_info())
# print(user_3.display_info())
# Add the enroll method to the User class, implement and test by calling the method on the user in the outer scope.
user_1.enroll()

# Implement the spend_points(self, amount) method
user_1.spend_points(50)

# Have the second user enroll.
user_2.enroll()

# Have the second user spend 80 points
user_2.spend_points(80)

# Call the display method on all the users.
print(user_1.display_info())
print(user_2.display_info())
print(user_3.display_info())