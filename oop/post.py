import user
import datetime


class Post:

    def __init__(self, name, author):
        self.name = name
        self.created_at = datetime.datetime.now()
        self.author = author

    def display_post_info(self):
        print(f"this post is called {self.name} and "
              f"this post is created at {self.created_at} the author of him is {self.author.username} "
              f"and he work as {self.author.job_title}")
