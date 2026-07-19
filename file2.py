student_records = {
    "S001": {"name": "Aditya", "subject": "Python", "grade": "A"},
    "S002": {"name": "Rahul", "subject": "Scratch", "grade": "B"},
    "S003": {"name": "Aditya", "subject": "Python", "grade": "A"},
    "S004": {"name": "Zara", "subject": "Data Science", "grade": "Pending"},
    "S005": {"name": "Sneha", "subject": "Web Dev", "grade": "A+"}
}

cleaned_records = {}
seen_students = set()

for student_id, details in student_records.items():
    name = details.get("name")
    subject = details.get("subject")
    grade = details.get("grade")
    
    if grade == "Pending":
        continue
        
    unique_id = (name, subject)
    if unique_id in seen_students:
        continue
        
    seen_students.add(unique_id)
    cleaned_records[student_id] = details

cleaned_records["S006"] = {"name": "Kabir", "subject": "Roblox", "grade": "A"}
cleaned_records["S002"]["grade"] = "A" 

print(f"Final record length: {len(cleaned_records)}\n")

for student_id, details in cleaned_records.items():
    print(f"ID: {student_id} | Name: {details['name']} | Subject: {details['subject']} | Grade: {details['grade']}")