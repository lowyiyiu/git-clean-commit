import sys, tempfile, os, subprocess, random, string

def rand(n):
    return 'COMMITCLEANER-' + ''.join(random.choice(string.ascii_uppercase) for i in range())

def main():
    if len(sys.argv) != 3:
        print("usage: git-clean-commit [GIT PATH] [COMMIT TEXT]\n")
        exit()

    CONF_GIT_PATH = sys.argv[1]
    CONF_COMMIT_TEXT = sys.argv[2]
    CONF_TEMP_FOLDER = rand(5)
    CONF_TEMP_BRANCH = rand(5)

    try:
        os.chdir(tempfile.gettempdir())
    except:
        print("An error occurred!\n")
        exit

    if sys.version_info >= (3, 5):
        subprocess.run(["mkdir", CONF_TEMP_FOLDER])
        os.chdir(CONF_TEMP_FOLDER)
        subprocess.run(["git", "clone", CONF_GIT_PATH])
        os.chdir(os.listdir(os.getcwd())[0])
        subprocess.run(["git", "checkout", "--orphan", CONF_TEMP_BRANCH])
        subprocess.run(["git", "add", "-A"])
        subprocess.run(["git", "commit", "-am", CONF_COMMIT_TEXT])
        subprocess.run(["git", "branch", "-D", "master"])
        subprocess.run(["git", "branch", "-m", "master"])
        subprocess.run(["git", "push", "origin", "master", "--force-with-lease"])
        os.chdir("../../")
        subprocess.run(["rm", "-rf", CONF_TEMP_FOLDER])
    else:
        subprocess.call(["mkdir", CONF_TEMP_FOLDER])
        os.chdir(CONF_TEMP_FOLDER)
        subprocess.call(["git", "clone", CONF_GIT_PATH])
        os.chdir(os.listdir(os.getcwd())[0])
        subprocess.call(["git", "checkout", "--orphan", CONF_TEMP_BRANCH])
        subprocess.call(["git", "add", "-A"])
        subprocess.call(["git", "commit", "-am", CONF_COMMIT_TEXT])
        subprocess.call(["git", "branch", "-D", "master"])
        subprocess.call(["git", "branch", "-m", "master"])
        subprocess.call(["git", "push", "origin", "master", "--force-with-lease"])
        os.chdir("../../")
        subprocess.call(["rm", "-rf", CONF_TEMP_FOLDER])
    print("Done!\n")
    exit

if __name__== "__main__":
    main()
