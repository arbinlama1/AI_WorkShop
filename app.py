print("Hello World")
name = "Ram"
faculty ="computer Science"
dob = "03/07/2003";
print("Hello, " + name + "!" + " You are a student of " + faculty + "and your date of birth is " + dob);
print(f"Hello, {name}!");

print(f"Hello, {name}!. You are a student of {faculty} an your date of birth is {dob}")

# print(f"Hello, {}. You are a student of {} an your date of birth is {}".format(name, faculty, dob))
print(f"Type f name: {type(name)}");
print(f"Type of faculty: {type(faculty)}");
print(f"Type of dob: {dob}");

# multiples variables assign


# swap values
x, y = 10, 20
print("Before swap x = ", x, "y = ", y)
x,y = y, x
print("After swap: x = ", x, " y = ", y)

# list can hold the multiple data type it is like a array c 
student_info = ["Charlie", 21,88.0]
name, age, score = student_info

print("Unpacked ", name, age, score)

name, *age = student_info
print("Name: ", name, "age and score is" , age)

# creating list
student_name = ['arbin', 'nikesh', 'bibash', 'rajib'];
print("Frist student: ", student_name[0]);
print("Last Student: ", student_name[-1])
print("First three student: ", student_name[0:3]);
print("Every second student: ", student_name[::2])

# List operators 
student_name.append("Eva")
student_name.insert(1,"Frank")
student_name.remove("arbin")
print("After removing Bob: ", student_name)
student_socre = [85, 67, 95, 50]

# list comprehension(poserul feature!)
passing_score = [score for score in student_socre if score >= 80]
print("/Passing scores (>=80): ", passing_score)