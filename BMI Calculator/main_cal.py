# calculate daily maintainance calories

def greet():
    print("Let's calculate your Daily maintainance calories.")
    
wel = greet()
height = float(input("Enter your height in cms: "))
weight = float(input("Enter your weight in kgs: "))
age = float(input("Enter your age in years: "))
gender= input("enter your gender")



def calculate_bmr(gender, weight, height, age):
    male = ["male", "M" , "m", "Male"]
    female = ["female", "F", "f", "Female"]
    if gender in female:
        women = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        return int(women)
    elif gender in male:
         men = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age) 
         return int(men)
    else:
        print ("Enter valid details")
 
activity = input('''What is your activity level?
1)Sedentary that is little to no exercise.
2)Lightly active that is 1 - 3 days/week.
3)Moderately active that is 3 - 5 days/week.
4)Very active that is 6 - 7 days/week.
Enter 1,2,3 or 4.''')

# get maintainance calories on basis of activity level

def get_calories(activity,BMR):
    if activity == "1":
        cal = BMR * 1.2
        return cal
    elif activity == "2":
        cal = BMR * 1.375
        return cal
    elif activity == "3":
        cal = BMR * 1.55
        return cal
    elif activity == "4":
        cal = BMR * 1.725
        return cal
    else:
        print("Enter Valid Details!")

        

BMR = calculate_bmr(gender, weight, height, age)
main_calories = get_calories(activity,BMR)
print(f"you need to consume {main_calories} calories a day to maintain your current weight")
