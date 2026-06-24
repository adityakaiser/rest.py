grade_book={}
print("commands: 'add','grade','report', or 'exit'\n")

while True:
    command=input("enter command: ")

    if command=='add':
        name=input("enter student name: ").title()
        grade_book[name]=[]
        print(f"added {name}")

    elif command=="grade":
        name=input("enter student name:").title()
        if name in grade_book:
            score=float(input(f"enter score for name{name}:"))
            grade_book[name].append(score)
            print(f"recorded score{score}")
    else:
        print("student not found")
    if command=="report":
        print("____GRADE BOOK REPORT____")
        for name,grades in grade_book.items():
            print(f"{name}:no scores recorded yet")
        else:
            average=sum(grades) / len(grades)
            print(f"{name}: avg score=",{average})
        print("____________________")
    elif command=="exit":
        print("goodbye")
        break
    else:
        print("invalid command")
         