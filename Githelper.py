import os

path = input("Enter the path to project: ")
if not os.path.exists(path + "/.git"):
    response = input("Git repository doesn't exist. Create one? (Y/n): ")
    if response == "Y" or response == "y":
        os.system("git init")
        print("Successfully")
        message = input("Enter the message to commit: ")
        link = input("Enter the link to repo: ")
        os.system('git add . & git commit -m "' + message + '" & git push --set-upstream ' + link + ' master')
