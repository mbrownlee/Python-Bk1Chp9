# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take varying number of children's names as the argument.

# For example, the run function would be defined as follows:


def run(*kids):
    for kid in kids:
        print(f"{kid} ran like a fool!")
    # Loop through all the kids and print that the child performed the activity.

run("Joe", "Jenna", "Pam", "Sam", "Andrea", "Will")

def swing(*kids):
    for kid in kids:
        print(f"{kid} swang high like a fool!")

swing("Marybeth", "Ariel", "Kevin", "Courtney")

def slide(*kids):
    for kid in kids:
        print(f"{kid} slid down the slide like a fool!")

slide("Mike", "Jack", "Jennifer", "Earl")

def hide(*kids):
    for kid in kids:
        print(f"{kid} hid like a fool!")

hide("Henry", "Heather", "Hayley", "Hugh")
# Output: 
# "Joe ran like a fool!"
# "Jenna ran like a fool!"
# Do the same for the following children:

# Running kids: Pam, Sam, Andrea, Will
# Swinging kids: Marybeth, Ariel, Kevin, Courtney
# Sliding kids: Mike, Jack, Jennifer, Earl
# Hiding kids: Henry, Heather, Hayley, Hugh