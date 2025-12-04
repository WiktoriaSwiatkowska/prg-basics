class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
    
    def display_timeline(self):
        print(self.username)
        print[self.posts]

def main():
    john= SocialMediaProfile("johndoe")
    john.add_post["Hello, world!","Had a great day at the park!","What's up, Natalie? How are you?"]
    john.display_timeline()


if __name__ =="__main__":
    main()