import os

project_path = input("Enter the path to the project: ")
if not os.path.exists(project_path + "/.git"):
    answer = input("There is no git repo here. Should I create one? (Y/n): ")
    if answer == "Y" or answer == "y":
        message_for_commit = input("Enter the message for commit: ")
        link_to_github = input("Enter the link to github: ")
        os.system('git init & git add . & git commit -m "' + message_for_commit +
                  '" & git push --set-upstream ' + link_to_github + ' master')
    else:
        print("Ok, what should I do then? Order pizza? Hack some celebrities? Bye, stoopid")
        exit()
else:
    message_for_commit = input("Enter the message for commit: ")
    os.system('git add . & git commit -m "' + message_for_commit + '"')
    answer = input("Is your local repo connected to remote? (Y/n): ")
    if answer == "N" or answer == "n":
        link_to_github = input("Enter the link to github: ")
        os.system("git push --set-upstream " + link_to_github + " master")
    elif answer == "Y" or answer == "y":
        os.system("git push")
