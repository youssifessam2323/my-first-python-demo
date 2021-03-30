import user
import post
import datetime


new_user1 = user.User("essamyoussif@gmail.com", "jooe", "13123131", "SW Engineer")
new_user2 = user.User("yousf@gmail.com", "essamico", "12313123131", "Frontend Developer")
new_user3 = user.User("yoyo@gmail.com", "youssiffio", "12313123131", "Backend Developer")

post1 = post.Post("post 1", new_user1)
post2 = post.Post("post 2", new_user2)
post3 = post.Post("post 3", new_user3)

post1.display_post_info()