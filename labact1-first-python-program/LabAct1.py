print("+++++++++++++++++++++++++++++++++++")
print("This is programmed by Jennylyn Carbonell")
print("===================================")
print("***Pounds to Kilograms converter***")

pounds = 45
conversion = 2.205
kilograms = (pounds) / (conversion)


print("Weight in pounds (lbs):" + str(pounds))
print("Weight converted to kilograms (kg):" + str(kilograms))

print("===================================")
print("***Miles to Kilometers converter***")

miles = 15
conversion = 1.60934
kilometers = (miles) * (conversion)

print("Length in miles (mi):" + str(miles))
print("Length converted to kilometers (km):" + str(kilometers))

print("===================================")
print("***Farenheit to Celsius converter***")

farenheit = 35
conversion = 0
celcius = (farenheit - 32) * (5/9)

print("Temperature in farenheit (°F):" + str(farenheit))
print("Temperature converted to celsius (°C):" + str(celcius))

print("===================================")

Age_of_student_1 = 12
Age_of_student_2 = 12
Age_of_student_3 = 15
Age_of_student_4 = 13
Age_of_student_5 = 12
Age_of_student_6 = 14
Age_of_student_7 = 15
Age_of_student_8 = 13
Age_of_student_9 = 15
Age_of_student_10 = 14

print("Age of student 1: " + str(Age_of_student_1))
print("Age of student 2: " + str(Age_of_student_2))
print("Age of student 3: " + str(Age_of_student_3))
print("Age of student 4: " + str(Age_of_student_4))
print("Age of student 5: " + str(Age_of_student_5))
print("Age of student 6: " + str(Age_of_student_6))
print("Age of student 7: " + str(Age_of_student_7))
print("Age of student 8: " + str(Age_of_student_8))
print("Age of student 9: " + str(Age_of_student_9))
print("Age of student 10: " + str(Age_of_student_10))

students_lst = [12,12,15,13,12,14,15,13,15,14]

sum_students_age_lst = sum(students_lst)

lst_avg = sum_students_age_lst/len(students_lst)

print("The average age of the students is: " + str(lst_avg))

print("===================================")

characters = ["Zeri", "Jett", "Jinx", "Draven", "Viper"]
abilities = ["nova of energy", "updraft", "trap ability", "spinning blade", "snakebite"]
item = "flaming sword"
place = "Noxus"

multiline_st1 = """
     A million years ago, there were demons who stole the {} which is believed to be the most powerful item in the world.
"""
multiline_st2 = """ {} is a powerful empire with a fearsome reputation; however, at that time, the protectors of the said item went to train their powers in another empire along with another ruler. The demons want to rule and own everything. Fortunately, there are five heroes who are brave and capable enough to fight against them.
"""
multiline_st3 = """
     Meet {}, {}, {}, {}, and {}. Together, they went to get back the lost sword and save the world from the evil hands of their opponents. The five traveled far away, and before arriving at their destination, they encountered numerous obstacles along the route.
When they arrived at the empire of the demons, a lot of them had already started to attack them. 
"""
multiline_st4 = """   
     {} moved first by blowing her {}, which caused mass destruction to the place. The demons released more warriors to fight, but some were caught by {}'s {}. {} dealt a lot of damage with his {}, as well as {} poisoning everyone with his {}. With the final blow, {} used his {} ability to throw blades against the demons.
"""
multiline_st5 = '''
     They eventually succeeded in recovering the {}. After destroying the demons, the empire starts to live peacefully once more.
It was all down to the five valiant heroes who stood up for their homeland. Following that, the world is free of the darkness that the demons had brought.
'''
print(multiline_st1.format(item) + multiline_st2.format(place) + multiline_st3.format(characters[0], characters[1],characters[2], characters[3], characters[4]) + multiline_st4.format(characters[0], abilities[0], characters[1], abilities[1], characters[2], abilities[2], characters[3], abilities[3], characters[4], abilities[4]) + multiline_st5.format(item))