# ------------------ CLASSES ------------------

class Patient:
    def __init__(self, patient_id, name, age, gender, phone, disease, blood_group):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.disease = disease
        self.blood_group = blood_group

    def display(self):
        print(f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, "
              f"Gender: {self.gender}, Phone: {self.phone}, Disease: {self.disease}, "
              f"Blood Group: {self.blood_group}")


class Doctor:
    def __init__(self, doctor_id, name, specialization, experience, consultation_fee):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.experience = experience
        self.consultation_fee = consultation_fee

    def display(self):
        print(f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}, "
              f"Experience: {self.experience} years, Fee: ₹{self.consultation_fee}")


class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def display(self):
        print(f"Appointment: Patient {self.patient.name} with Dr. {self.doctor.name} "
              f"on {self.date} at {self.time}")


# ------------------ BILLING (Abstraction + Polymorphism) ------------------

class Bill:
    def __init__(self, appointment, medicine_charge, lab_charge, room_charge=0):
        self.appointment = appointment
        self.medicine_charge = medicine_charge
        self.lab_charge = lab_charge
        self.room_charge = room_charge

    def calculate_total(self):
        total = (self.appointment.doctor.consultation_fee +
                 self.medicine_charge + self.lab_charge + self.room_charge)

        if total >= 10000:
            discount = total * 0.10
        elif total >= 5000:
            discount = total * 0.05
        else:
            discount = 0

        return total, discount, total - discount

    def display(self):
        total, discount, final_amount = self.calculate_total()
        print("\n----------- BILL -----------")
        print(f"Patient: {self.appointment.patient.name}")
        print(f"Doctor: {self.appointment.doctor.name}")
        print(f"Consultation Fee: ₹{self.appointment.doctor.consultation_fee}")
        print(f"Medicine Charges: ₹{self.medicine_charge}")
        print(f"Lab Charges: ₹{self.lab_charge}")
        print(f"Room Charges: ₹{self.room_charge}")
        print(f"Total Amount: ₹{total}")
        print(f"Discount: ₹{discount}")
        print(f"Final Payable: ₹{final_amount}")
        print("----------------------------")


# ------------------ INHERITANCE ------------------

class InPatient(Patient):
    def __init__(self, patient_id, name, age, gender, phone, disease, blood_group, room_number):
        super().__init__(patient_id, name, age, gender, phone, disease, blood_group)
        self.room_number = room_number


class OutPatient(Patient):
    def __init__(self, patient_id, name, age, gender, phone, disease, blood_group):
        super().__init__(patient_id, name, age, gender, phone, disease, blood_group)


# ------------------ HOSPITAL CLASS (Encapsulation) ------------------

class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print("✅ Patient added successfully!")

    def display_patients(self):
        if not self.patients:
            print("No registered patients")
        else:
            print("------------Patients List-------------")
            for p in self.patients:
                p.display()

    def search_patient(self, patient_id):
        for p in self.patients:
            if p.patient_id == patient_id:
                print("Patient Found! ✅")
                p.display()
                return p
        print("Patient Not Found! 👎🏻")
        return None

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print("✅ Doctor added successfully!")

    def display_doctors(self):
        if not self.doctors:
            print("No registered doctors")
        else:
            print("------------Doctors List-------------")
            for d in self.doctors:
                d.display()

    def search_doctor(self, doctor_id):
        for d in self.doctors:
            if d.doctor_id == doctor_id:
                print("Doctor Found! ✅")
                d.display()
                return d
        print("Doctor Not Found! 👎🏻")
        return None

    def book_appointment(self, patient_id, doctor_id, date, time):
        patient = next((p for p in self.patients if p.patient_id == patient_id), None)
        doctor = next((d for d in self.doctors if d.doctor_id == doctor_id), None)
        if patient and doctor:
            appt = Appointment(patient, doctor, date, time)
            self.appointments.append(appt)
            print("✅ Appointment booked successfully!")
            appt.display()
            return appt
        else:
            print("❌ Patient or Doctor not found.")
            return None

    def view_appointments(self):
        if not self.appointments:
            print("No appointments booked yet.")
        else:
            print("------------Appointments List-------------")
            for appt in self.appointments:
                appt.display()

    def generate_bill(self, appointment):
        try:
            medicine_charge = float(input("Enter Medicine Charges: "))
            lab_charge = float(input("Enter Lab Charges: "))
            room_charge = float(input("Enter Room Charges: "))
            bill = Bill(appointment, medicine_charge, lab_charge, room_charge)
            bill.display()
        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")


# ------------------ MAIN MENU ------------------

hospital = Hospital("Peace Hospital")

while True:
    print("\nWELCOME TO PEACE HOSPITAL")
    print("1. Register Patient")
    print("2. Display Patients")
    print("3. Search Patient")
    print("4. Add Doctor")
    print("5. Display Doctors")
    print("6. Search Doctor")
    print("7. Book Appointment")
    print("8. View Appointments")
    print("9. Generate Bill (for last appointment)")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            pid = int(input("Enter Patient ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            gender = input("Enter Gender: ")
            phone = input("Enter Phone Number: ")
            disease = input("Enter Disease: ")
            blood_group = input("Enter Blood Group: ")
            patient = Patient(pid, name, age, gender, phone, disease, blood_group)
            hospital.add_patient(patient)
        except ValueError:
            print("❌ Invalid input.")

    elif choice == "2":
        hospital.display_patients()

    elif choice == "3":
        try:
            pid = int(input("Enter Patient ID to search: "))
            hospital.search_patient(pid)
        except ValueError:
            print("❌ Invalid input.")

    elif choice == "4":
        try:
            did = int(input("Enter Doctor ID: "))
            name = input("Enter Doctor Name: ")
            specialization = input("Enter Specialization: ")
            exp = int(input("Enter Years of Experience: "))
            fee = float(input("Enter Consultation Fee: "))
            doctor = Doctor(did, name, specialization, exp, fee)
            hospital.add_doctor(doctor)
        except ValueError:
            print("❌ Invalid input.")

    elif choice == "5":
        hospital.display_doctors()

    elif choice == "6":
        try:
            did = int(input("Enter Doctor ID to search: "))
            hospital.search_doctor(did)
        except ValueError:
            print("❌ Invalid input.")

    elif choice == "7":
        try:
            pid = int(input("Enter Patient ID: "))
            did = int(input("Enter Doctor ID: "))
            date = input("Enter Appointment Date (DD/MM/YYYY): ")
            time = input("Enter Appointment Time (HH:MM): ")
            appt = hospital.book_appointment(pid, did, date, time)
            if appt:
                hospital.generate_bill(appt)  # auto generate bill after appointment
        except ValueError:
            print("❌ Invalid input.")

    elif choice == "8":
        hospital.view_appointments()

    elif choice == "9":
        if hospital.appointments:
            hospital.generate_bill(hospital.appointments[-1])  # last appointment
        else:
            print("❌ No appointments found.")

    elif choice == "10":
        print("Exiting system... Goodbye!")
        break
    else:
        print("❌ Invalid choice, please try again.")