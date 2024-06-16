#TODO: Create a letter using starting_letter.txt
with open("Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

with open("Input/Names/invited_names.txt") as file:
    invited_names = []
    for lines in range(8):
        invited_names.append(file.readline().replace('\n', ""))

print(invited_names)
#for each name in invited_names.txt
for name in invited_names:
    with open(f"Output/ReadyToSend/letter_for_{name}", "w") as file:
        file.write(starting_letter.replace("[name]", name))


#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp