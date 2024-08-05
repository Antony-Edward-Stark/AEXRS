###################################################################################################
# By      : Antony Edward Stark
# Name    : main.py
# Funtion : Integrates the funtions.py and provides the platform for dispatchimg required functions
###################################################################################################
from os import system
from time import sleep
import platform

from speaker import speaker
import functions as f


if platform.system() == "Windows":
    system("cls")
elif platform.system() == "Darwin":
    system("clear")
elif platform.system() == "Linux":
    system("clear")


# ====================================================== #
friday_logo = """
+=================================================================+
|  ||||||||  ||||||||     |||  ||||      |||||||||  ||      ||    |
|  ||        ||     ||    |||  ||  ||    ||     ||   ||    ||     |
|  ||||||||  ||||||||     |||  ||    ||  ||     ||    ||  ||      |
|  ||        || ||        |||  ||    ||  |||||||||     ||||       |
|  ||        ||   ||      |||  ||  ||    ||     ||      ||        |
|  ||        ||     ||    |||  ||||      ||     ||     ||         |
+=================================================================+
"""
# ====================================================== #


def splitter(text):
    word_list = text.split(" ")
    return word_list


def startup():
    # ================================================================ #
    #                         Starts Jarpy                             #
    # ================================================================ #
    speaker("Initiating friday...")
    print(friday_logo)
    print("To see all commands, type 'help' in the command field")


def info_setup(state):
    # ================================================================ #
    #                         User Setup                               #
    # ================================================================ #
    if state == "i":
        speaker("Welcome to friday, let's get you set up!")
    elif state == "r":
        speaker("Starting configurator")

    speaker("Please enter your name")
    name = input("Enter your name: ")

    speaker("To refer you as 'Sir' or 'Madam', please specify your gender")
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

    speaker("For weather information, please specify your Openweathermap API key. Enter 'n' if you don't have one.")
    ApiKey = input("Specify your Openweathermap API key. Enter 'n' if you don't have one. : ")
    if ApiKey == "n":
        ApiKey = 'n'
        print("You will not be able to get weather information")
        speaker("You will not be able to get weather information")
        print("To get your openweathermap API key, go to https://home.openweathermap.org/users/sign_up")
        speaker("To get your openweathermap API key, go to the given given URL")

    speaker("Setting you up...")
    if platform.system == "Darwin":
        with open("/Users/Shared/userinfo.txt", "w") as setup:
            if gender == "male":
                call_name = "Sir"
            elif gender == "female":
                call_name = "Ma'am"
            setup.write(f"{name};{call_name};{location};{ApiKey}")

        with open("/Users/Shared/userinfo.txt", "r") as n:
            updated_info = n.read()
            f.greeter(updated_info.split(";"))

    elif platform.system() == "Windows":
        with open("userinfo.txt", "w") as setup:
            if gender == "male":
                call_name = "Sir"
            elif gender == "female":
                call_name = "Ma'am"
            setup.write(f"{name};{call_name};{location};{ApiKey}")
    command()


status = True
n = 0


def command():
    # ================================================================ #
    #                       Command  Function                          #
    # ================================================================ #
    global status, n

    with open("userinfo.txt") as i:
        info = i.read()
        if len(info) > 0:
            info = info.split(";")

    while status:
        if n > 0:
            speaker(f"Please enter a command")
        cmd = input("\nEnter command: ").lower()
        cmd_mod = splitter(cmd)
        print(cmd_mod)
        for command in cmd_mod:
            # ========================= Helper function invoked ====================== #
            if "help" == command:
                f.helper()

            # =========================== Reconfig invoked =========================== #
            elif "config" == command:
                # r stands for reconfig
                info_setup("r")

            # ========================= Jokes function invoked ======================= #
            elif "jokes" == command or "joke" == command:
                f.jokes()

            # ======================== Weather function invoked ====================== #
            elif "weather" == command:
                f.weather()
            # ======================= Open app function invoked ====================== #
            elif "open-app" == command:
                if platform.system() == "Windows":
                    pass #working for windows 11

                elif platform.system() == "Darwin":
                    speaker("Open an app by specifying the name")
                    app_name = input("App name: ").lower()
                    f.app_opener(app_name)
            # ============================= Time invoked ============================= #
            elif "time" == command:
                f.current_time()

            # ============================= Time invoked ============================= #
            elif "lyrics" == command:
                speaker("Please enter the artist name.")
                artist = input("Artist name: ")
                speaker("Please enter the song name.")
                song = input("Song name: ")
                f.get_lyrics(artist, song)
                sleep(3)

            #=============================News invoked ===============================#
            elif 'news' == command:
                f.news_gatherer()
            # ============================= Exit invoked ============================= #
            if "exit" == command:
                speaker(f"It's a pleasure {info[1]}, Have a nice day")
                status = False


startup()


try:
    with open("userinfo.txt") as i:
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
