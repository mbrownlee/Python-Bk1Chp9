def add(*list_of_numbers):
    sum = 0
    
    for number in list_of_numbers:
        sum = sum + number

    print("Sum:",sum)

add(3,5)
add(4,5,6,7)
add(1,2,3,5,6)
add(376, 42, 995, 10)

def list_person(**person):
    for key, value in person.items():
        print(f"{key} is {value}")

list_person(first_name="Melissa", last_name="Bell", age=25, occupation="Software Developer")

def calculate_average(subject, *test_scores, **student_details):
    print("Type & value of subject: ", type(subject), subject)
    print("Type & value of test_scores: ", type(test_scores), test_scores)
    print("Type & value of the student_details: ", type(student_details), student_details)

    if subject == "English":
        average_score = 49
    else:
        average_score = sum(test_scores)/len(test_scores)
    
    print(f"{student_details['last_name']}, {student_details['first_name']} got an average score of {average_score} in {subject}.")


calculate_average("Math", 75, 64, 35, first_name="Bryan", last_name="Nilsen")
