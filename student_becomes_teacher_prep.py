lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
# write a func called average that has the argument numbers
def average(numbers):
  # call sum for numbers in total
  total = sum(numbers)
  # call float for total in total
  total = float(total)
  # devide total by len of numbers
  return total / len(numbers)

# define a func that takes argument "student"
def get_average(student):
  #make a var homeowrk that stores average() of student["homework"]
  homework = average(student["homework"]) * 0.10
  #make a var quizzes that stores average() of student["quizzes"]
  quizzes = average(student["quizzes"]) * 0.30
  #make a var tests that stores average() of student["tests"]
  tests = average(student["tests"]) * 0.60
  # return the sum of the three vars multipied by weights 
  return homework + quizzes + tests

  def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >=80:
    return "B"
  elif score >=70:
    return "C"
  elif score >=60:
    return "D"
  else:
    return "F"
  
print get_letter_grade(get_average(lloyd))

def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)
  print average(results)

  students = [lloyd,alice,tyler]

print get_class_average(students)

print get_letter_grade(get_class_average(students))

  