class ClinicAppointment:
    def __init__(self):
       
        self.time_slots = ["10am", "11am", "12pm", "2pm", "3pm"]
        self.appointments = {}  
        
        self.patient_lookup = {}


    def book_appointment(self, name, age, mobile, doctor):
        
        if mobile in self.patient_lookup:
            return f"Mobile {mobile} already has an appointment booked."

        
        if doctor not in self.appointments:
            self.appointments[doctor] = {slot: [] for slot in self.time_slots}

    
        available = [slot for slot in self.time_slots 
                     if len(self.appointments[doctor][slot]) < 3]

        if not available:
            return f"No available slots for Dr. {doctor}."

        print(f"\nAvailable slots for Dr. {doctor}: {available}")
        chosen = input("Enter desired slot: ")

        if chosen not in available:
            return "Invalid or unavailable time slot."

        
        patient_data = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "doctor": doctor,
            "slot": chosen
        }

        self.appointments[doctor][chosen].append(patient_data)
        self.patient_lookup[mobile] = (doctor, chosen, patient_data)

        return f"Appointment booked at {chosen} with Dr. {doctor}."

    
    def view_appointment(self, mobile):
        if mobile not in self.patient_lookup:
            return "No appointment found for this mobile number."

        doctor, slot, patient_data = self.patient_lookup[mobile]

        return (f"Appointment Details:\n"
                f"Name: {patient_data['name']}\n"
                f"Age: {patient_data['age']}\n"
                f"Doctor: {doctor}\n"
                f"Time Slot: {slot}")

    def cancel_appointment(self, mobile):
        if mobile not in self.patient_lookup:
            return "No appointment found to cancel."

        doctor, slot, patient_data = self.patient_lookup[mobile]

        
        self.appointments[doctor][slot] = [
            p for p in self.appointments[doctor][slot] 
            if p["mobile"] != mobile
        ]

        
        del self.patient_lookup[mobile]

        return f"Appointment for mobile {mobile} has been cancelled."

    def doctor_availability(self, doctor):
        if doctor not in self.appointments:
            return f"No appointments yet for Dr. {doctor}."

        result = "\nDoctor Availability:\n"
        for slot in self.time_slots:
            booked = len(self.appointments[doctor][slot])
            result += f"{slot}: {booked}/3 booked\n"

        return result
