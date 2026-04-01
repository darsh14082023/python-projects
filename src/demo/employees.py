class employees:
    firstName = "";
    lastName = "";

    def getFirstName(self):
        return self.firstName;

    def getLastName(self):
        return self.lastName;

    def setFirstName(self, firstName):
        self.firstName = firstName;

    def setLastName(self, lastName):
        self.lastName = lastName;

employeesObj = employees();
employeesObj.setFirstName(input("Enter first name: "));
employeesObj.setLastName(input("Enter last name: "));
print("Hello " + employeesObj.getFirstName() + " " + employeesObj.getLastName());