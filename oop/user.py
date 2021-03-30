class User:
    def __init__(self, email, username, password, job_title):
        self.email = email
        self.password = password
        self.username = username
        self.job_title = job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self,new_job_title):
        self.job_title = new_job_title

    def display_user_info(self):
        print(f"my username is {self.username} and my job title is {self.job_title}")
