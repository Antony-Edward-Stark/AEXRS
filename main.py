import functions as f

# f.greeter()
# f.weather()

def splitter(text):
    word_list = text.split(" ")


def command():
    cmd = ''
    cmd = input('Sir, How can I help you? Please enter your command here.')
    f.speaker('Sir, How can I help you? Please enter your command here : ')
    cmd_mod = splitter(cmd)
    if 'jokes' in cmd_mod:
        f.jokes()
    command()

command()