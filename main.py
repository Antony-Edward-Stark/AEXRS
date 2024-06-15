from os import system, mkdir
from time import sleep
import platform

from speaker import speaker
import functions as f

system("clear")


# ============================================ #
jarpy_logo = """
+===============================================+
|        ██╗ █████╗ ██████╗  ██████╗ ██╗   ██╗  |
|        ██║██╔══██╗██╔══██╗ ██╔══██╗╚██╗ ██╔╝  |
|        ██║███████║██████╔╝ ██████╔╝ ╚████╔╝   |
|   ██   ██║██╔══██║██╔══██╗ ██╔═══╝   ╚██╔╝    |
|   ╚█████╔╝██║  ██║██║  ██║ ██║        ██║     |
|    ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═╝        ╚═╝     |
+===============================================+
"""
# ============================================ #


def splitter(text):
    word_list = text.split("=")
    return word_list


# ================================================================ #
#                         Starts Jarpy                             #
# ================================================================ #
def startup():
    speaker("Initiating jar pie...")
    print(jarpy_logo)
    print("To see all commands, type 'help' in the command field")


# ================================================================ #
#                         User Setup                               #
# ================================================================ #
def info_setup(state):
    if state == "i":
        # it's typed jar pie rather than jarpy due to pronunciation issues
        speaker("Welcome to jar pie, let's get you set up!")
    elif state == "r":
        speaker("Starting configurator")

    speaker("Please enter your name")
    name = input("Enter your name: ")

    speaker("To refer you as 'Sir' or 'Ma'am', please specify your gender")
    gender = input("Specify your gender(male/female): ").lower()
    if gender == "male":
        call_name = "Sir"
    elif gender == "female":
        call_name = "Ma'am"
    else:
        print("Please specify a valid gender")
        speaker("Please specify a valid gender")
        gender = input("Specify your gender(male/female): ").lower()

    speaker("For weather information, please specify your current city")
    location = input("Specify your current city: ").capitalize()

    speaker(
        "For weather information, please specify your Openweathermap API key. Enter 'n' if you don't have one.: "
    )
    ApiKey = input(
        "Specify your Openweathermap API key. Enter 'n' if you don't have one. : "
    )
    if ApiKey == "n":
        print("You will not be able to get weather information")
        speaker("You will not be able to get weather information")
        print(
            "To get your openweathermap API key, go to https://home.openweathermap.org/users/sign_up"
        )
        speaker("To get your openweathermap API key, go to the above given URL")
        speaker("Enter your openweathermap API key :")
        ApiKey = input("Specify your Openweathermap API key : ")

    speaker("Setting you up...")

    with open("/Users/Shared/userinfo.txt", "w") as setup:
        if gender == "male":
            call_name = "Sir"
        elif gender == "female":
            call_name = "Ma'am"
        setup.write(f"{name};{call_name};{location};{ApiKey}")

    with open("/Users/Shared/userinfo.txt", "r") as n:
        updated_info = n.read()
        f.greeter(updated_info.split(";"))

    command()


status = True
n = 0


# ================================================================ #
#                       Command  Function                          #
# ================================================================ #
def command():
    global status, n

    with open("/Users/Shared/userinfo.txt") as i:
        info = i.read()
        if len(info) > 0:
            info = info.split(";")

    while status:
        if n > 0:
            speaker(f"Please enter a command")
        cmd = input("\nEnter command: ").lower()
        cmd_mod = splitter(cmd)

        # ========================= Helper function invoked ====================== #
        if "help" in cmd_mod or "h" in cmd_mod:
            f.helper()

        # =========================== Reconfig invoked =========================== #
        if "config" in cmd_mod or "c" in cmd_mod:
            # r stands for reconfig
            info_setup("r")

        # ========================= Jokes function invoked ======================= #
        if "jokes" in cmd_mod or "joke" in cmd_mod or "j" in cmd_mod:
            f.jokes()

        # ======================== Weather function invoked ====================== #
        if "weather" in cmd_mod or "w" in cmd_mod:
            # split and join functions are to remove any whitespaces (e.g./n)
            f.weather("".join(info[2].split()))

        # ======================= Open app function invoked ====================== #
        if "open-app" in cmd_mod or "o-a" in cmd_mod or "oa" in cmd_mod:
            if platform.system() == "Windows":
                if len(cmd_mod) <= 1:
                    speaker("Open an app by specifying the name")
                    print(
                        """
                            .----------------------------------------------.
                            |Type 'LS' to get all apps available for launch|
                            '----------------------------------------------'
                            """
                    )
                    app_name = input("App name: ")
                    f.app_opener(app_name)
                else:
                    f.app_opener(cmd_mod[1])
            elif platform.system() == "Darwin":
                speaker("Open an app by specifying the name")
                print(
                    """
                                .----------------------------------------------.
                                |Type 'LS' to get all apps available for launch|
                                '----------------------------------------------'
                                """
                )
                app_name = input("App name: ").lower()
                f.app_opener(app_name)
        # ============================= Time invoked ============================= #
        if "time" in cmd_mod or "t" in cmd_mod:
            f.current_time()

        # ============================= Time invoked ============================= #
        if "lyrics" in cmd_mod or "l" in cmd_mod:
            speaker("Please enter the artist name.")
            artist = input("Artist name: ")
            speaker("Please enter the song name.")
            song = input("Song name: ")
            f.get_lyrics(artist, song)
            sleep(3)

        # ============================= Exit invoked ============================= #
        if "exit" in cmd_mod or "e" in cmd_mod:
            speaker(f"It's a pleasure {info[1]}, Have a nice day")
            status = False

        else:
            n += 1
            command()


startup()
try:
    with open("/Users/Shared/userinfo.txt") as i:
        info = i.read()
        if len(info) > 0:
            info = info.split(";")
    if len(info) == 0:
        # i stands for initial config
        info_setup("i")
    else:
        f.greeter(info)
        command()

except FileNotFoundError:
    info_setup("i")
