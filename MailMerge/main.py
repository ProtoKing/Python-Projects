#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

## Read the files
with open('C:\\Users\\Steve23\\Desktop\\CS - IT\\1. BootCamps\\100 Days of Python Coding\\MailMerge\\Input\\Letters\\starting_letter.txt') as letter:
    template = letter.read()

    # template = letter.readlines()

with open('C:\\Users\\Steve23\\Desktop\\CS - IT\\1. BootCamps\\100 Days of Python Coding\\MailMerge\\Input\\Names\\invited_names.txt') as names:
    invited = names.readlines()

for names in invited:
    name = names.strip('\n')
    with open(f"C:\\Users\\Steve23\\Desktop\\CS - IT\\1. BootCamps\\100 Days of Python Coding\\MailMerge\\Output\\ReadyToSend\\letter_for_{name}.txt", mode='w') as invitation:
       invitation = invitation.write(template.replace("[name]", name))



