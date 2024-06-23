import os
import subprocess


def open_app(app_name):
    """Attempts to open an application on Windows using two methods:

    - Using the `os.startfile` function (preferred):
        - Launches the application by opening its associated file.
    - Using the `subprocess.call` function (fallback):
        - Executes a shell command to open the application using its executable path.

    Args:
        app_name: The name of the application to open (e.g., "notepad", "chrome")

    Returns:
        True if the application is opened successfully, False otherwise.
    """

    # Attempt to open using os.startfile (preferred method)
    try:
        if os.path.isfile(app_name):
            os.startfile(app_name)
        else:
            program_files = os.environ.get("PROGRAMFILES", "")
            program_files_x86 = os.environ.get("PROGRAMFILES(x86)", "")
            potential_paths = [
                os.path.join(program_files, app_name + ".exe"),
                os.path.join(program_files_x86, app_name + ".exe"),
            ]
            for path in potential_paths:
                if os.path.isfile(path):
                    os.startfile(path)
                    return True
            raise FileNotFoundError(
                f"Application '{app_name}' not found using os.startfile"
            )
        return True
    except Exception as e:
        pass

    # Fallback: Open using subprocess.call (if os.startfile fails)
    try:
        subprocess.call(app_name, shell=True)
        return True
    except Exception as e:
        print(f"Error opening '{app_name}' using subprocess.call: {e}")
        return False


# # Example usage
# app_to_open = input("Enter the name of the application to open: ")  # Replace with your desired application name
# success = open_app(app_to_open)

# if success == True:
#     print(f"Successfully opened '{app_to_open}'")
# else:
#     print(f"Failed to open '{app_to_open}'")

#######################################################################################################################################################################

import functions as f
f.get_lyrics("Alan Walker", "Unsure")