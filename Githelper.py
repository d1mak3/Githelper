import os


def input_message_to_commit():
    message = input("Enter the message for commit: ")
    choice = input("Wanna change message? (Y/n): ")
    if choice == "N" or choice == "n":
        return message
    elif choice == "Y" or choice == "y":
        new_message_for_commit = input_message_to_commit()
        return new_message_for_commit


project_path = input("Enter the path to the project: ")
if not os.path.exists(project_path + "/.git"):
    answer = input("There is no git repo here. Should I create one? (Y/n): ")
    if answer == "Y" or answer == "y":
        message_for_commit = input_message_to_commit()
        link_to_github = input("Enter the link to github: ")
        os.system('git init & git add . & git commit -m "' + message_for_commit +
                  '" & git push --set-upstream ' + link_to_github + ' master')
    else:
        print("Ok, what should I do then? Order pizza? Hack some celebrities? Bye, stoopid")
        exit()
else:
    message_for_commit = input_message_to_commit()
    os.system('git add . & git commit -m "' + message_for_commit + '"')
    git_config = open(project_path + "/.git/config")
    if git_config.read().find("remote") == -1:
        link_to_github = input("Enter the link to github: ")
        os.system("git push --set-upstream " + link_to_github + " master")
    else:
        os.system("git push")
