from get_user_post import get_user_post
from get_own_post import get_own_post
from get_user_info import get_user_info

print("\t\t\t*****Welcome To InstaBot*****")
menu_choices = "What do you want to do. Select from the below Choices (1-6) \n\t1. Like A Post \n\t2. Comment on a post \n\t3. Download Own Post "\
               "\n\t4. Download Friend's post \n\t5. Get Friend Info. \n\t6. Close Application \n"
menu_choice = input(menu_choices)
if (menu_choice) > 0:
    menu_choice = int(menu_choice)

    if menu_choice == 1:
        insta_username = raw_input("Enter Username")
        print("Wait liking Ur POst......")
        like_user_post(insta_username)
        print("\n")
        print("\n")

    elif menu_choice == 2:
        insta_username = raw_input("Enter Username.........\n")
        comment_user_post(insta_username)
        print("wait work under process.......")
        print("\n")
        print("\n")
    elif menu_choice == 3:
        print ("WAit Getting ur post.......\n")
        get_own_post()
        print("\n")
        print("\n")
    elif menu_choice == 4:
        insta_username = raw_input("Enter Username.........\n")
        print("Wait Downloading user post......")
        get_user_post(insta_username)

        print("\n")
        print("\n")
    elif menu_choice == 5:
        insta_username = raw_input("Enter Username.........\n")
        print("Wait getting information.....")
        get_user_info(insta_username)
        print("\n")
        print("\n")
    elif menu_choice == 6:
        print "Thanks"
        exit()