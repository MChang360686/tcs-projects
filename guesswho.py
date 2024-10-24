students = {
    'alice': [95, 93, 97],
    'bob': [87, 97, 90]
}

def find_percentage(student_dictionary, student_name):
    grades = student_dictionary[student_name]
    sum = 0
    for i in range(0, len(grades)):
        sum += grades[i]
    return sum / len(grades)

print(find_percentage(students, 'alice'))

numbers = '2 32 8 10 47'

def calc_hash(n):
    numbers = tuple(n.split(' '))
    return hash(numbers)

