from Post import Post
user_input = ""
all_posts_archive = []

# your code here
post1 =  Post("Marie", "This is my first post")
print(post1)
post2 = Post("Jacob", "This is a post?")
print(post2)
post3 = Post("Moshe", "uhhhhh")
print(post3)
username = input("Enter your username: ")
print(f"Welcome to your profile, {username}!")
print("new - Add a post to the archive")
print("remove - Remove a post from the archive")
print("change user - Change your username associated with future posts")
print("print - Display the current, up-to-date list of all posts")
print("quit - End the program")

while (user_input != "quit"):
    user_input = input ("What would you like to do? ")
    if user_input == "new":
        content = input("Enter the content of your post: ")
        new_post = Post(username, content)
        all_posts_archive.append(new_post)

    elif user_input == "remove":
        if len(all_posts_archive) == 0:
            print("Invalid number.")
        elif len(all_posts_archive) > 0:
            index = int(input("Enter the index of the post you want to remove (1st is index 0): "))
            del all_posts_archive[index]
    
    elif user_input == "change user":
        username = input("Enter your new username: ")
        print(f"Your username has been changed to {username}.")
    
    if user_input == "print":
        for post in all_posts_archive:
            print(post)