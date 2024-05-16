import functions as f
from speaker import speaker

def splitter(text):
    word_list = text.split(" ")
    return word_list

f.greeter()

def command():
    cmd = ''
    speaker('Sir, How can I help you? Please enter your command here : ')
    cmd = input('Sir, How can I help you? Please enter your command here : ')
    cmd_mod = splitter(cmd)
    
    #################################
    #####Jokes function invoked######
    #################################
    if 'jokes' in cmd_mod:
        f.jokes()
    elif 'joke' in cmd_mod:
        f.jokes()
    
    ###################################
    #####Weather function invoked######
    ###################################
    if 'weather' in cmd_mod:
        f.weather()
    else:
        pass
    
    
    speaker('Sir, Do you want me to do something else?')
    next_iteration_vhoice = input('Sir, Do you want me to do something else?(yes/no)')
    
    if next_iteration_vhoice == 'yes':
        command()
    elif next_iteration_vhoice == 'no':
        speaker('Welcome sir, Have a nice day')
    else:
        print("Enter a valid command...")
        speaker("please enter a valid command")
        command()
command()