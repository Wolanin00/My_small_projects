
class User:

    def __init__(self, user_id: str, name: str) -> None:
        self.user_id = user_id
        self.name = name.capitalize()
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(user_id='001', name='jack')
user_2 = User(user_id='002', name='patric')

user_1.follow(user_2)

print(user_1.following)
