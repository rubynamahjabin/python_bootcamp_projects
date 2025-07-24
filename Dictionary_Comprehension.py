import random

#random score generation for students
names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
students_score={student:random.randint(1,100) for student in names}
print(students_score)

#new dictionary including only passed students
passed_students={
    student:score for (student,score) in students_score.items() if score>=60
}
print(passed_students)

#count number of letters in each word of a sentence
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {
    word:len(word) for word in sentence.split()
}
print(result)

#Convert each temperature to degree Fahrenheit
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {
    day:temp_c*9/5+32 for (day,temp_c) in weather_c.items()
}
print(weather_f)