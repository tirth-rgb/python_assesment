class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.next_id = 1001  # Starting student ID

    def _validate_age(self, age):
        if 5 <= age <= 18:
            return True
        raise ValueError("Age must be between 5 and 18")

    def _validate_mobile(self, mobile):
        if mobile.isdigit() and len(mobile) == 10:
            return True
        raise ValueError("Mobile number must be 10 digits")

    def _validate_class(self, student_class):
        if 1 <= student_class <= 12:
            return True
        raise ValueError("Class must be between 1 and 12")

    # ➔ New Admission
    def new_admission(self, name, age, student_class, mobile):
        self._validate_age(age)
        self._validate_class(student_class)
        self._validate_mobile(mobile)

        student_id = self.next_id
        self.students[student_id] = {
            "name": name,
            "age": age,
            "class": student_class,
            "mobile": mobile
        }
        self.next_id += 1
        return f"Student admitted successfully. Student ID: {student_id}"

    # ➔ View Student Details
    def view_student(self, student_id):
        return self.students.get(student_id, "Student not found")

    # ➔ Update Student Info
    def update_student(self, student_id, student_class=None, mobile=None):
        if student_id not in self.students:
            return "Student not found"

        if student_class is not None:
            self._validate_class(student_class)
            self.students[student_id]["class"] = student_class

        if mobile is not None:
            self._validate_mobile(mobile)
            self.students[student_id]["mobile"] = mobile

        return "Student information updated successfully"

    # ➔ Remove Student Record
    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            return "Student record removed successfully"
        return "Student not found"
