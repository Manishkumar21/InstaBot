from get_user_post import get_user_post
from get_own_post import get_own_post
from get_user_info import get_user_info
from like_user_post import like_user_post
from comment_user_post import comment_user_post1
from self_info import self_info

print("\t\t\t*****Welcome To InstaBot*****")
menu_choices = "What do you want to do. Select from the below Choices (1-6) \n\t1. Show Own Profile  \n\t2. Download Own Post " \
               "\n\t3. Get User's Information. \n\t4. Download User's Recent Post \n\t5. Like User's Post" \
               " \n\t6. Comment on User's Post \n\t7. Close Application"
show_menu = True
while show_menu:
    menu_choice = input(menu_choices)
    if (menu_choice) > 0:
        menu_choice = int(menu_choice)

        if menu_choice == 1:
            self_info()
            print("\n\n")


        elif menu_choice == 2:
            print (".....Downloading Your Own Recent Post.....\n")
            get_own_post()
            print("\n")
            print("\n")

        elif menu_choice == 3:
            insta_username = raw_input("Enter Username.........\n")
            print("Wait getting information.....")
            get_user_info(insta_username)
            print("\n")
            print("\n")

        elif menu_choice == 4:
            insta_username = raw_input("Enter Username.........\n")
            print("Wait Downloading user post......")
            get_user_post(insta_username)

            print("\n")
            print("\n")

        elif menu_choice == 5:
            insta_username = raw_input("Enter Username")
            print("Wait liking Ur POst......")
            like_user_post(insta_username)

        elif menu_choice == 6:
            insta_username = raw_input("Enter Username.........\n")
            comment_user_post1(insta_username)
            print("\n")
            print("\n")

        elif menu_choice == 6:
            exit()

        else:
            show_menu = False