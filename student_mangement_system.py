students = {
    "Ali": {
        "age": 20,
        "city": "Lahore",
        "marks": {
            "Math": 90,
            "English": 80,
            "Science": 85
        }
    },
    "Ahmed": {
        "age": 21,
        "city": "Karachi",
        "marks": {
            "Math": 75,
            "English": 88,
            "Science": 70
        }
    },
    "Hassan": {
        "age": 19,
        "city": "Islamabad",
        "marks": {
            "Math": 95,
            "English": 90,
            "Science": 92
        }
    },
    "Hannan": {
        "age":18,
        "city":"Lahore",
        "marks":{
            "Math":98,
            "English":97,
            "Science":99
        }
    },
    "Humaira": {
        "age":19,
        "city":"Lahore",
        "marks":{
            "Math":97,
            "English":98,
            "Science":96
        }
    }
}
def show_allstudents():
    for key , value in students.items():
        print("Student :",key)
        print("Age :",value["age"])
        print("City :",value["city"])
        for subject , marks in value["marks"].items():
            print(subject,":",marks)
        print("-------------------")    
def search_student():
    search = input("Enter Student to Search :").title()
    if search in students:
        details = students[search]
        print("Student :",search)
        print("Age :",details["age"])
        print("City :",details["city"])
        for subject , marks in details["marks"].items():
            print(subject,":",marks)
        print("-------------------")
def add_student():
    name = input("Enter Student to Add :").title() 
    if name in students:
        print("Student Already Exists :")
        return 
    else:
        age = int(input("Enter Age :"))
        city = input("Enter City :")
        math = int(input("Enter Marks Of maths :"))
        english = int(input("Enter Marks Of English :"))
        science = int(input("Enter Marks of Science :"))

        students.update({
            name:{
                "age":age,
                "city":city,
                "marks":{
                    "Math":math,
                    "English":english,
                    "Science":science
                }
            }
        })
        print("Student Added Successfully..!")
def update_student():
    name = input("Enter Student Name To Update :")
    if name in students:
        subject = input("Enter Subject Name To Update Marks :")
        if subject in students[name]["marks"]:
            new_marks = int(input("Enter New Marks :"))
            students[name]["marks"][subject]=new_marks
            print("Marks Updated Successfully..!")
        else:
            print("Subject Not Found...!")
    else:
        print("Student Not Found...!")  
def delete_student():
    name = input("Enter Student Name :")
    if name in students:
        students.pop(name)
        print("Student Deleted Successfully..!")
    else:
        print("Student Not Found...!")
def calculate_results():
    for name , details in students.items():
        total = 0
        for subject , marks in details["marks"].items():
            total+=marks
        average = total / len(details["marks"])
        print("\nStudent :",name)
        print("Total :",total)
        print("Average :",round(average,2))
        if average>=40:
            print("Result = Pass")
        else:
            print("Result = Fail")   
        print("------------------")     
def final_results():
    for name , details in students.items():
        total = 0
        for subject , marks in details["marks"].items():
            total+=marks
        average = total/len(details["marks"])
        if average>=40:
            result = "Pass"
        else:
            result = "Fail"
        print(
            name,"->","Total = ",total,"->","Average = ",round(average,2),"->","Result",result
        )    
def student_management():
    while True:
        print("===== STUDENT MANAGEMENT =====\n1. Show All Students\n2. Search Student\n3. Add Student\n4. Update Marks\n5. Delete Student\n6. Calculate Results\n7. Show Final Results\n8. Exit")   
        choice = input("Enter Your Choice :")
        if choice == "1":
            show_allstudents()
        elif choice == "2":
            search_student()
        elif choice == "3":
            add_student()
        elif choice == "4":
            update_student()                 
        elif choice == "5":
            delete_student()
        elif choice == "6":
            calculate_results()
        elif choice == "7":
            final_results()
        elif choice == "8":
            print("Exiting.....!\nThanks For Using Your Marks Portal")
            break
        else:
            print("Inavlid Choice..!\nTryAgin :")
student_management()            
               

        













                         


