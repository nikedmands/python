from employee import Employee

Nik = Employee("Nik", 100, "Engineer")
Nik.getInfo()

Serene = Employee("Serene", 200000, "Virtual Engineer")
Serene.getInfo()

Melissa = Employee("Melissa", 3000000000000000, "Customer Service Advisor")
Melissa.showSalary()
Melissa.uplift(1)
Melissa.showSalary()
print('')

Nik.showSalary()
Nik.salaryDeduction(89)
Nik.showSalary()
Nik.updateSalary(10000)
Nik.showSalary()