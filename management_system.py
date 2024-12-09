#YOUTUBE LINK: https://youtu.be/Y239F809wHc
#GITHUB LINK: https://github.com/launchland/Alberta_Heath_Management

#DOCTOR
class Doctor:
  #constructor
  def __init__(self, id, name, specilist, timing, qualification, roomNb):
    self.id = id
    self.name = name
    self.specilist = specilist
    self.timing = timing
    self.qualification = qualification
    self.roomNb = roomNb

  #getters
  def get_id(self):
    return self.id
  def get_name(self):
    return self.name
  def get_specilist(self):
    return self.specilist
  def get_timing(self):
    return self.timing
  def get_qualification(self):
    return self.qualification
  def get_roomNb(self):
    return self.roomNb

  #setters
  def set_id(self, id):
    self.id = id
  def set_name(self, name):
    self.name = name
  def set_specilist(self, specilist):
    self.specilist = specilist
  def set_timing(self, timing):
    self.timing = timing
  def set_qualification(self, qualification):
    self.qualification = qualification
  def set_roomNb(self, roomNb):
    self.roomNb = roomNb

  #string
  def __str__(self):
    return f"{self.id}_{self.name}_{self.specilist}_{self.timing}_{self.qualification}_{self.roomNb}"

#DOCTOR MANAGER
class DoctorManager:
  def __init__(self):
    self.doctor_list = []
    self.read_doctors_file()

  def format_dr_info(self, doctor):
    return f"{doctor.get_id()}_{doctor.get_name()}_{doctor.get_specilist()}_{doctor.get_timing()}_{doctor.get_qualification()}_{doctor.get_roomNb()}"

  def enter_doctor_info(self):
    id = input("Enter doctor id: ")
    name = input("Enter doctor name: ")
    specilist = input("Enter doctor specialty: ")
    timing = input("Enter doctor timing (e.g., 7am-10pm): ")
    qualification = input("Enter doctor qualification: ")
    roomNb = input("Enter doctor room number: ")
    print(f"Doctor whose ID is {id} has been added.")
    return Doctor(id, name, specilist, timing, qualification, roomNb)

  def read_doctors_file(self):
    with open("doctors.txt", "r") as file:
      next(file)
      for line in file:
        id, name, specilist, timing, qualification, roomNb = line.strip().split("_")
        doctor = Doctor(id, name, specilist, timing, qualification, roomNb)
        self.doctor_list.append(doctor)

  def search_doctor_by_id(self):
    doctor_id = input("Enter doctor ID: ")
    for doctor in self.doctor_list:
      if doctor.get_id() == doctor_id:
        print(f"{'ID':<5} {'Name':<23} {'Specialty':<16} {'Timing':<16} {'Qualification':<16} {'Room Number'}\n")
        print(self.display_doctor_info(doctor))
        break
    else:
      print("Can’t find the doctor with the same ID.")

  def search_doctor_by_name(self):
    doctor_name = input("Enter Doctor name: ")
    for doctor in self.doctor_list:
      if doctor.get_name() == doctor_name:
        print(f"{'ID':<5} {'Name':<23} {'Specialty':<16} {'Timing':<16} {'Qualification':<16} {'Room Number'}\n")
        print(self.display_doctor_info(doctor))
        break
    else:
      print("Can’t find the doctor with the same name.")

  def display_doctor_info(self, doctor):
    return f"{doctor.get_id():<5} {doctor.get_name():<23} {doctor.get_specilist():<16} {doctor.get_timing():<16} {doctor.get_qualification():<16} {doctor.get_roomNb()}\n"
  
  def edit_doctor_info(self):
        doctor_id = input("Enter doctor ID to edit: ")
        for doctor in self.doctor_list:
            if doctor.get_id() == doctor_id:
                doctor.name = input("Enter new name: ") or doctor.name
                doctor.specialty = input("Enter new specialty: ") or doctor.specialty
                doctor.timing = input("Enter new timing: ") or doctor.timing
                doctor.qualification = input("Enter new qualification: ") or doctor.qualification
                doctor.roomNb = input("Enter new room number: ") or doctor.roomNb
                self.write_list_of_doctors_to_file()
                print(f"Doctor whose ID is {doctor_id} has been edited.")
                return
        else:
          print("Cannot find the doctor with the provided ID.")

  def display_doctors_list(self):
    print(f"{'ID':<5} {'Name':<23} {'Specialty':<16} {'Timing':<16} {'Qualification':<16} {'Room Number'}\n")  # Add header
    for doctor in self.doctor_list:
      print(f"{doctor.get_id():<5} {doctor.get_name():<23} {doctor.get_specilist():<16} {doctor.get_timing():<16} {doctor.get_qualification():<16} {doctor.get_roomNb()}") # Print information for each doctor

  def write_list_of_doctors_to_file(self):
        with open("doctors.txt", "w") as file:
            for doctor in self.doctor_list:
              doctor_info = self.format_dr_info(doctor)
              file.write("\n" + self.format_dr_info(doctor))

  def add_dr_to_file(self):
        doctor = self.enter_doctor_info()
        self.doctor_list.append(doctor)
        doctor_info = self.format_dr_info(doctor)
        with open("doctors.txt", "a") as file:
            file.write("\n" + self.format_dr_info(doctor))

#PATIENT
class Patient:
  #constructor
  def __init__(self, id, name, disease, gender, age):
    self.id = id
    self.name = name
    self.disease = disease
    self.gender = gender
    self.age = age

  #getters
  def get_id(self):
    return self.id
  def get_name(self):
    return self.name
  def get_disease(self):
    return self.disease
  def get_gender(self):
    return self.gender
  def get_age(self):
    return self.age

  #setters
  def set_id(self, new_id):
    self.id = new_id
  def set_name(self, new_name):
    self.name = new_name
  def set_disease(self, new_disease):
    self.disease = new_disease
  def set_gender(self, new_gender):
    self.gender = new_gender
  def set_age(self, new_age):
    self.age = new_age

  #string
  def __str__(self):
    return f"{self.id}_{self.name}_{self.disease}_{self.gender}_{self.age}"

#PATIENT MANAGER
class PatientManager:
  def __init__(self):
    self.patient_list = []
    self.read_patients_file()

  def format_patient_info_for_file(self, patient):
    return f"{patient.get_id()}_{patient.get_name()}_{patient.get_disease()}_{patient.get_gender()}_{patient.get_age()}"

  def enter_patient_info(self):
    id = input("Enter patient id: ")
    name = input("Enter patient name: ")
    disease = input("Enter patient disease: ")
    gender = input("Enter patient gender: ")
    age = input("Enter patient age: ")
    print(f"Patient whose ID is {id} has been added.")
    patient = Patient(id, name, disease, gender, age)
    return patient

  def read_patients_file(self):
    with open("patients.txt", "r") as file:
        next(file)  # Skip the first line
        for line in file:
          # Split the line by underscore, limiting the number of splits to 5
          parts = line.strip().split("_", 5)
          # Assign the first 5 parts to the respective variables
          id, name, disease, gender, age = parts[:5]
          patient = Patient(id, name, disease, gender, age)
          self.patient_list.append(patient)

  def search_patients_by_id(self):
    patient_id = input("Enter patient id: ")
    for patient in self.patient_list:
      if patient.get_id() == patient_id:
        print(f"{'ID':<5} {'Name':<24} {'Disease':<16} {'Gender':<16} {'Age':<3}\n")
        print(self.display_patient_info(patient))
        break
    else:
      print("Patient not found")

  def display_patient_info(self, patient):
    return f"{patient.get_id():<5} {patient.get_name():<24} {patient.get_disease():<16} {patient.get_gender():<16} {patient.get_age():<3}\n"


  def edit_patient_info_by_id(self):
    patient_id = input("Please enter the id of the Patient that you want to edit their information: ")
    for patient in self.patient_list:
      if patient.get_id() == patient_id:
        new_name = input("Enter new name: ")
        new_disease = input("Enter new disease: ")
        new_gender = input("Enter new gender: ")
        new_age = input("Enter new age: ")
        patient.set_name(new_name)
        patient.set_disease(new_disease)
        patient.set_gender(new_gender)
        patient.set_age(new_age)
        self.write_list_of_patients_to_file()
        print(f"Patient whose ID is {patient_id} has been edited.")
        break
    else:
      print("Patient not found")

  def display_patients_list(self):
    print(f"{'ID':<5} {'Name':<24} {'Disease':<16} {'Gender':<16} {'Age':<3}\n")
    for patient in self.patient_list:
      print(self.display_patient_info(patient))  # Call display_patient_info for each patient

  def write_list_of_patients_to_file(self):
    with open("patients.txt", "w") as file:
      for patient in self.patient_list:
        patient_info = self.format_patient_info_for_file(patient)
        file.write("\n" + patient_info)

  def add_patient_to_file(self):
    patient = self.enter_patient_info()
    self.patient_list.append(patient)
    patient_info = self.format_patient_info_for_file(patient)
    with open("patients.txt", "a") as file:
      file.write("\n" + patient_info)

#MANAGEMENT
class Management:
  #MENU
  def display_menu(self):
    while True:
      print("\nWelcome to Alberta Hospital (AH) Managment System")
      pages = input("""Select from the following options, or select 3 to stop:
1 -     Doctors
2 -     Patients
3 -     Exit Program
>>> """)

      #DOCTORS MENU
      if pages == "1":
        while True:
          doctor_page = input("""\nDoctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu
>>> """)
          if doctor_page == "1": #list doctors
            DoctorManager().display_doctors_list()

          elif doctor_page == "2": #search id
            DoctorManager().search_doctor_by_id()

          elif doctor_page == "3": #search name
            DoctorManager().search_doctor_by_name()

          elif doctor_page == "4": #add doctor
            DoctorManager().add_dr_to_file()

          elif doctor_page == "5": #edit doctor
            DoctorManager().edit_doctor_info()

          elif doctor_page == "6": #return to main menu
            break

      #PATIENTS MENU
      elif pages == "2":
        while True:
          patient_page = input("""\nPatients Menu
1 - Display Patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu
>>> """)
          if patient_page == "1": #patient list
            PatientManager().display_patients_list()

          elif patient_page == "2": #search id
            PatientManager().search_patients_by_id()

          elif patient_page == "3": #add patient
            PatientManager().add_patient_to_file()

          elif patient_page == "4": #edit patient
            PatientManager().edit_patient_info_by_id()

          elif patient_page == "5": #return to main menu
            break
          else:
            print("Invalid input. Please try again.\n")

      #EXIT PROGRAM
      elif pages == "3":
        print("Thanks for using the program. Bye!")
        break #ends program
      else:
        print("Invalid input. Please try again.\n")


#TESTING
if __name__ == "__main__":
  Management().display_menu()
