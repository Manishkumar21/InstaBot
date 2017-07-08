from get_user_post import get_user_post
from get_own_post import get_own_post
from get_user_info import get_user_info
from like_user_post import like_user_post
from comment_user_post import comment_user_post1
from self_info import self_info
from delete_negative_comments import delete_negative_comment
from show_all_user_post_comment import show_all_comment

print("\t\t\t*****Welcome To InstaBot*****\n")
menu_choices = "What do you want to do. Select from the below Choices (1-6)" \
               "\n\n\t\t1. Show Own Profile Info " \
               "\n\t\t2. Download Own Post " \
               "\n\t\t3. Get User's Profile Information. " \
               "\n\t\t4. Download User's Recent Post " \
               "\n\t\t5. Like User's Recent Post" \
               " \n\t\t6. Comment on User's Recent Post " \
                " \n\t\t7. Show Comments From User's Recent Post " \
                " \n\t\t8. Delete Negative Comments From User's Recent Post " \
               "\n\t\t9. Close Application  "

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

        elif menu_choice == 3:
            insta_username = raw_input("Enter The Username Who's Information You Want. \n")
            print("Wait ** Information is Downloading...")
            get_user_info(insta_username)
            print("\n")

        elif menu_choice == 4:
            insta_username = raw_input("Enter The Username Who's Recent Post You Want To Download. \n")
            print("Wait ** User's Recent Post is Downloading...")
            get_user_post(insta_username)
            print("\n")

        elif menu_choice == 5:
            insta_username = raw_input("Enter The Username Who's Recent Post You Want To Like. ")
            print("Wait ** Liking The User's Recent Post...")
            like_user_post(insta_username)
            print("\n")

        elif menu_choice == 6:
            insta_username = raw_input("Enter The Username Who's Recent Post You Want To Write Something. \n")
            print("Wait ** Commenting in the User's Recent Post...")
            comment_user_post1(insta_username)
            print("\n")

        elif menu_choice == 7:
            insta_username = raw_input("Enter The Username Who's Recent Post's Comments You Want to Show \n")
            print("Wait ** Fetching the User's Recent Comment...")
            show_all_comment(insta_username)
            print("\n")

        elif menu_choice == 8:
            insta_username = raw_input("Enter The Username Who's Recent Post You Want To Delete Something. \n")
            print("Wait ** Deleting the User's Recent Comment...")
            delete_negative_comment(insta_username)
            print("\n")

        elif menu_choice == 9:
            exit()

        else:
            show_menu = False