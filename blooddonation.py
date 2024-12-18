import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

# Global list to store registered donors
donors_list = []

def register_donor():
    name = entry_name.get()
    age = entry_age.get()
    gender = var_gender.get()
    address = entry_address.get()
    blood_type = entry_blood_type.get()
    weight = entry_weight.get()

    try:
        age = int(age)  #Convert age to integer
        weight = float(weight)  #Convert weight to float
        
        #Check if inputs are valid
        if not name or not blood_type or not address:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return
        
        # Eligibility check
        if age < 18 or age > 65:
            messagebox.showinfo("Eligibility", f"Sorry {name}, you must be between 18 and 65 years old to donate blood.")
            return
        
        if weight < 45:
            messagebox.showinfo("Eligibility", f"Sorry {name}, you must weigh at least 45kg to donate blood.")
            return
        
        if var_willing_to_donate.get() == 1:  # Willing to donate
            donor = {"Name": name, "Age": age, "Gender": gender, "Address": address, "Blood Type": blood_type, "Weight": weight}
            donors_list.append(donor)
            messagebox.showinfo("Registration Successful", f"Thank you, {name}, for registering to donate blood!")
            update_donor_list()
            clear_form()
        else:
            messagebox.showinfo("Eligibility", f"Thank you {name}, but you must be willing to donate blood to register.")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid age and weight.")

def update_donor_list():
    for row in treeview.get_children():
        treeview.delete(row)
    
    for donor in donors_list:
        treeview.insert("", "end", values=(donor["Name"], donor["Age"], donor["Gender"], donor["Address"], donor["Blood Type"], donor["Weight"]))

def update_donors():
    try:
        selected_item = treeview.selection()[0]
        update_donors = treeview.item(selected_item)['values'][0]
    except IndexError:
        messagebox.showwarning("Selection Error", "No donor selected!")
        return

    age = entry_age.get()
    address = entry_address.get()
    weight = entry_weight.get()

    if not (age and address and weight):
        messagebox.shorwwarning("Input Error", "All fields are required!")
        return

    update_donors(int(age), address, weight)
    clear_form()
    

def clear_form():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    var_gender.set("")
    entry_address.delete(0, tk.END)
    entry_blood_type.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    var_willing_to_donate.set(0)

def remove_donor():
    selected = treeview.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a donor to remove.")
        return
    donor_name = treeview.item(selected)["values"][0]
    donor_index = next((index for (index, donor) in enumerate(donors_list) if donor["Name"] == donor_name), None)
    if donor_index is not None:
        removed_donor = donors_list.pop(donor_index)
        messagebox.showinfo("Donor Removed", f"{removed_donor['Name']} has been removed from the list.")
        update_donor_list()

def sort_donors():
    sort_by = var_sort_by.get()
    if sort_by == "Name":
        donors_list.sort(key=lambda donor: donor["Name"])
    elif sort_by == "Age":
        donors_list.sort(key=lambda donor: donor["Age"])
    update_donor_list()

root = tk.Tk()
root.title("Blood Donation Registration System")
root.config(bg="red")

label_name = tk.Label(root, text="Enter Full Name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_age = tk.Label(root, text="Enter Age:")
label_age.pack()

entry_age = tk.Entry(root)
entry_age.pack()

label_gender = tk.Label(root, text="Select Gender:")
label_gender.pack()

var_gender = tk.StringVar()
radio_male = tk.Radiobutton(root, text="Male", variable=var_gender, value="Male")
radio_male.pack()

radio_female = tk.Radiobutton(root, text="Female", variable=var_gender, value="Female")
radio_female.pack()

label_address= tk.Label(root, text="Enter your Address:")
label_address.pack()

entry_address= tk.Entry(root)
entry_address.pack()

label_blood_type = tk.Label(root, text="Enter Blood Type (A, B, AB, O):")
label_blood_type.pack()

entry_blood_type = tk.Entry(root)
entry_blood_type.pack()

label_weight = tk.Label(root, text="Enter Weight (in kg):")
label_weight.pack()

entry_weight = tk.Entry(root)
entry_weight.pack()

var_willing_to_donate = tk.IntVar()
label_willing = tk.Label(root, text="Are you willing to donate blood?")
label_willing.pack()

radio_yes = tk.Radiobutton(root, text="Yes", variable=var_willing_to_donate, value=1)
radio_yes.pack()

radio_no = tk.Radiobutton(root, text="No", variable=var_willing_to_donate, value=0)
radio_no.pack()

button_register = tk.Button(root, text="Register Donor", command=register_donor)
button_register.pack()

button_update_donors= tk.Button(root,text="Update Donor Information", command=update_donors)
button_update_donors.pack()

button_clear = tk.Button(root, text="Clear Form", command=clear_form)
button_clear.pack()

button_remove = tk.Button(root, text="Remove Selected Donor", command=remove_donor)
button_remove.pack()

label_sort = tk.Label(root, text="Sort Donors By:")
label_sort.pack()

var_sort_by = tk.StringVar(value="Name")
dropdown_sort = tk.OptionMenu(root, var_sort_by, "Name", "Age")
dropdown_sort.pack()

treeview = ttk.Treeview(root, columns=("Name", "Age", "Gender", "Address", "Blood Type", "Weight"), show="headings")
treeview.pack()

#Define the headings for the treeview columns
treeview.heading("Name", text="Name")
treeview.heading("Age", text="Age")
treeview.heading("Gender", text="Gender")
treeview.heading("Address", text="Address")
treeview.heading("Blood Type", text="Blood Type")
treeview.heading("Weight", text="Weight")

root.mainloop()

#Blood Registration System
class Donor:
    def _init_(self, name, age, gender, address):
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address

class BloodDonationSystems:
    def _init_(self):
        self.donors= {}
    
    def register_donor(self,name,age,gender,address):
        new_donor = Donor(name, age, gender,address)
        self.donors.append(new_donor)
        print("Donor register blood donation system successfully")

    def update_donor(self, age=None,address=None):
        if 0 <= self < len(self.donors) :
            donor = self.donors={self}
            if age:
                donor ("age")==age
            if address:
                donor ("address")==address
            print(f"donor{age, address + 1} updated successfully")

    def deleted_donor(self, age,address):
        if 0 <= self < len(self.donors):
            deleted_donor = self.donors.pop(self)
            print (f"donor {deleted_donor, age,address}")

    while True:
        print("Welcome to The Blood Donation System!")
        print("1. Register as a new donor")
        print("2. Check the eligibility of donor to donate")
        print("3. Update the donor's information")
        print("4. Delete information of donors")
        print("3. End")       

#The function of create donor's information
        name= input("Enter your name:")
        age = int (input("Enter your age:"))
        if age < 18:
            print("not eligible to donate")
        elif age >= 18 and age <= 65:
            print("eligible to donate")
        gender = input("Enter your gender(MALE/FEMALE):")
        address= input("Enter your address:")
           
#The information of health's donors
        blood_type = input("Enter your blood types(A, B, AB, O):")
        weight= int(input("Enter the weight, in kg"))
        if weight < 45:
            print ("not eligible to donate")
        else:
            print("eligible to donate")

#The update of information's donors
        age= int(input("Enter your new age:"))    
        address= input("Enter your new address:")
        weight= input("Enter your new weight,in kg:")

#The delete of data's donors
        age= int(input("Enter your old age to delete:"))
        address= input("Enter your old address to delete:")
        weight= input("Enter your old weight,in kg:")