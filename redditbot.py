import praw
from urllib.parse import urlparse, parse_qs
import configparser
import os

"""CONFIG_FILE = "User_profiles.ini"

def save_credentials(username, password, client_id, client_secret, user_agent, profile_name):
    config = configparser.ConfigParser()

    config.read(CONFIG_FILE)

    if "Profiles" not in config:
        config.add_section("Profiles")

    config[profile_name] = {
        "username": username,
        "password": password,
        "client_id": client_id,
        "client_secret": client_secret,
        "user_agent": user_agent
    }

    config["CurrentProfile"] = {"name": profile_name}

    with open(CONFIG_FILE, "w") as configfile:
        config.write(configfile)

def load_profiles():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    if "Profiles" in config:
        return list(config["Profiles"].keys())
    else:
        return []
    
def authenticate_profile(profile_name):
    profiles = load_profiles()

    if profiles and profile_name in profiles:
        credentials = profiles[profile_name]
        reddit = praw.Reddit(
            client_id = credentials["client_id"],
            client_secret = credentials["client_secret"],
            password = credentials["password"],
            user_agent = credentials["user_agent"],
            username = credentials["username"],
        )
        return reddit
    else: 
        return None
    
def remove_profile(profile_name):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    if "Profiles" in config and profile_name in config["Profiles"]:
        config.remove_option("Profiles", profile_name)

        with open(CONFIG_FILE, "w") as configfile:
            config.write(configfile)

def get_current_profile():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    if "CurrentProfile" in config and "name" in config["CurrentProfile"]:
        return config["CurrentProfile"]["name"]
    else:
        return None"""
    
def terminator():
    """config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    config.remove_section("Profiles")
    with open(CONFIG_FILE, "w") as configfile:
        config.write(configfile)
    os.remove(CONFIG_FILE)"""
    #print("All profiles and and credentials deleted. Exiting.")
    print("Process Terminated!")
    exit()
    
#profile_name = input("Write a name for your Profile: ")
cl_user = input("Enter username: ")
cl_pass = input("Enter password: ")
cl_id = input("Enter client ID: ")
cl_secret = input("Enter client secret: ")
cl_useragent = input("Enter User Agent ('<Console:***:1.0>' It must be unique for each Authentication): ")

reddit = praw.Reddit(
    client_id= cl_id,
    client_secret= cl_secret,
    password= cl_pass,
    user_agent= cl_useragent,
    username= cl_user,
)

#save_credentials(cl_user, cl_pass, cl_id, cl_secret, cl_useragent, profile_name)

def main():
    print("1. Upvote\n" 
          "2. Downvote\n" 
          "3. Comment\n" 
          "4. Post\n"
          "5. Exit\n"
          #"0. --PROFILE SETTING--"
          )
    index = int(input("Enter the respective index for desired function (i.e. 1 for Upvote): "))
    if index == 1:
        func_upvote()
    elif index == 2:
        func_downvote()
    elif index == 3:
        func_comment()
    elif index == 4:
        func_post()
    elif index == 5:
        terminator()
    #elif index == 0:
        #prof_setting()
    else:
        print("Please enter correct index!")

"""def prof_setting():

    current_profile = get_current_profile()
    if current_profile:
        print(f"Currently using Profile: {current_profile}")

    print("1. Switch Profile\n"
          "2. Add Profile\n"
          "3. Remove Profile\n"
          "4. Back\n")
    priv_index1 = int(input("Enter the index: "))
     
    if priv_index1 == 1:
        profile_name = input("Enter name of profile you want to switch to: ")
        reddit =  authenticate_profile(profile_name)

        if reddit:
            print(f"Switched to Profile: {profile_name}")
            main()
        else:
            print(f"Profile '{profile_name}' not found!")
            main()
    elif priv_index1 == 2:
        profile_name = input("Enter new Profile name: ")
        cl_user = input("Enter Username: ")
        cl_pass = input("Enter Password: ")
        cl_id = input("Enter Client ID: ")
        cl_secret = input("Enter Client secret: ")
        cl_useragent = input("Enter Useragent ('<Console:***:1.0>' It must be unique for each Authentication): ")

        save_credentials(cl_user, cl_pass, cl_id, cl_secret, cl_useragent, profile_name)

        print(f"Profile '{profile_name}' added!")
        main()
    elif priv_index1 == 3: 
        profile_name = input("Enter name of Profile you want to remove: ")
        remove_profile(profile_name)
        print(f"Profile '{profile_name}' removed!")
        main()
    elif priv_index1 == 4:
        main()    
    else:
        print("Please enter the correct index")
        main()"""

def func_upvote():
    post_url = input("Enter URL = ")

    parsed_url = urlparse(post_url)
    path_parts = parsed_url.path.split("/")

    if "comment" in path_parts:
        comment_id = path_parts[path_parts.index("comment") + 1]

        comment = reddit.comment(id = comment_id)
        comment.clear_vote()
        comment.upvote()

        print (f"Comment Upvoted! URL:{post_url}")
        main()
    else:
        post_id = path_parts[path_parts.index("comments") + 1]

        submission = reddit.submission(id = post_id)
        submission.clear_vote()
        submission.upvote()

        print (f"Post Upvoted! URL:{post_url}")
        main()

def func_downvote():
    post_url = input("Enter URL = ")

    parsed_url = urlparse(post_url)
    path_parts = parsed_url.path.split("/")

    if "comment" in path_parts:
        comment_id = path_parts[path_parts.index("comment") + 1]

        comment = reddit.comment(id = comment_id)
        comment.clear_vote()
        comment.downvote()

        print (f"Comment Downvoted! URL:{post_url}")
        main()
    else:
        post_id = path_parts[path_parts.index("comments") + 1]

        submission = reddit.submission(id = post_id)
        submission.clear_vote()
        submission.downvote()

        print (f"Post Downvoted! URL:{post_url}")
        main()

def func_comment():
    comment_content = input("Write your comment:  ")
    post_url = input("Enter the URL of Post/Comment you want to reply to: ")

    parsed_url = urlparse(post_url)
    path_parts = parsed_url.path.split("/")

    if "comment" in path_parts:
        comment_id = path_parts[path_parts.index("comment") + 1]

        comment = reddit.comment(id = comment_id)
        reply = comment.reply(comment_content)

        print (f"Reply posted! URL:{post_url}")
        main()
    else:
        post_id = path_parts[path_parts.index("comments") + 1]

        submission = reddit.submission(id = post_id)
        comment = submission.reply(comment_content)

        print (f"Comment posted! URL:{post_url}")
        main()


def func_post():
    print("1. Text post.\n"
          "2. URL post.\n"
          "3. Image post.\n"
          "4. Video post.\n"
          "5. Create a poll.\n"
          "6. Go back.\n")
    
    priv_index2 = int(input("Enter the index: "))
    if priv_index2 == 1:
        subreddit_name = input("Subreddit (i.e. 'python'): ")
        post_title = input("Enter title of post: ")
        post_content = input("Write post content: ")

        response = int(input("Are you sure you want to post? (Enter '1' to proceed or '2' to cancel): "))
        if response == 1:
            submission = reddit.subreddit(subreddit_name).submit(post_title, selftext = post_content)

            print(f"Post submitted! URL:{submission.url}")
            main()
        elif response == 2:
            func_post()

    elif priv_index2 == 2:
        subreddit_name = input("Subreddit (i.e. 'python'): ")
        post_title = input("Enter title of post: ")
        post_content = input("Enter URL you want to post: ")

        response = int(input("Are you sure you want to post? (Enter '1' to proceed or '2' to cancel): "))
        if response == 1:
            submission = reddit.subreddit(subreddit_name).submit(post_title, url = post_content)

            print(f"Post submitted! URL:{submission.url}")
            main()
        elif response == 2:
            func_post()

    elif priv_index2 == 3:
        subreddit_name = input("Subreddit (i.e. 'python'): ")
        post_title = input("Enter title of post: ")
        post_content = input("Enter the path of image: ")

        response = int(input("Are you sure you want to post? (Enter '1' to proceed or '2' to cancel): "))
        if response == 1:
            submission = reddit.subreddit(subreddit_name).submit_image(post_title, post_content)

            print(f"Post submitted! URL:{submission.url}")
            main()
        elif response == 2:
            func_post()

    elif priv_index2 == 4:
        subreddit_name = input("Subreddit (i.e. 'python'): ")
        post_title = input("Enter title of post: ")
        post_content = input("Enter the path of video: ")

        response = int(input("Are you sure you want to post? (Enter '1' to proceed or '2' to cancel): "))
        if response == 1:
            submission = reddit.subreddit(subreddit_name).submit_video(post_title, post_content)

            print(f"Post submitted! URL:{submission.url}")
            main()
        elif response == 2:
            func_post()

    elif priv_index2 == 5:
        subreddit_name = input("Subreddit (i.e. 'python'): ")
        post_title = input("Enter title of poll: ")
        choices = int(input("How many options in poll answers? (2 to 6 allowed): "))
        if choices<2 or choices>6:
            print("Select the number from within the range!")
            func_post()
        else:
            poll_choice = []
            for i in range(choices):
                choice = input(f"Enter choice #{i + 1}: ")
                poll_choice.append(choice)

        post_content = input("Write accompanying text of poll: ")
        dur = int(input("Enter the duration of poll: "))

        response = int(input("Are you sure you want to post? (Enter '1' to proceed or '2' to cancel): "))
        if response == 1:
            submission = reddit.subreddit(subreddit_name).submit_poll(post_title, options = poll_choice, selftext=post_content, duration=dur)

            print(f"Post submitted! URL:{submission.url}")
            main()
        elif response == 2:
            func_post()

    elif priv_index2 == 6:
        main()
    else:
        print("Please enter correct index!")
        main()



if __name__ == "__main__":
    main()