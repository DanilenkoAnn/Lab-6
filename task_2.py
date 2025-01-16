class Employee:
    def __init__(self, hours_worked, hourly_rate, bonus_coefficient):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.bonus_coefficient = bonus_coefficient


    def salary_to_hours_ratio(self):
        base_salary = self.hours_worked * self.hourly_rate  
        return base_salary / self.hours_worked if self.hours_worked != 0 else 0


class SeniorEmployee(Employee):
    def __init__(self, hours_worked, hourly_rate, bonus_coefficient, additional_experience):
        super().__init__(hours_worked, hourly_rate, bonus_coefficient)
        self.additional_experience = additional_experience   


class Director(Employee):
    def __init__(self, hours_worked, hourly_rate, bonus_coefficient, department):
        super().__init__(hours_worked, hourly_rate, bonus_coefficient)
        self.department = department   


if __name__ == "__main__":
    employee = Employee(hours_worked=160, hourly_rate=30, bonus_coefficient=0.10)
    senior_employee = SeniorEmployee(hours_worked=160, hourly_rate=30, bonus_coefficient=0.15, additional_experience=5)
    director = Director(hours_worked=170, hourly_rate=40, bonus_coefficient=0.20, department='IT')

    print(f"Соотношение зарплаты к рабочим часам (старший сотрудник): {senior_employee.salary_to_hours_ratio():.2f}")
    print(f"Соотношение зарплаты к рабочим часам (директор): {director.salary_to_hours_ratio():.2f}")
 