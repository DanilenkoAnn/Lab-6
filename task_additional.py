class Employee:
    def __init__(self, hours_worked, hourly_rate, bonus_coefficient):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.bonus_coefficient = bonus_coefficient


    def __add__(self, other):
 
        if isinstance(other, Employee):
             
            total_hours = self.hours_worked + other.hours_worked
            total_hourly_rate = (self.hourly_rate + other.hourly_rate) / 2   
            total_bonus_coefficient = (self.bonus_coefficient + other.bonus_coefficient) / 2   
            return Employee(total_hours, total_hourly_rate, total_bonus_coefficient)
        return NotImplemented


class SeniorEmployee(Employee):
    def __init__(self, hours_worked, hourly_rate, bonus_coefficient, additional_experience):
        super().__init__(hours_worked, hourly_rate, bonus_coefficient)
        self.additional_experience = additional_experience


class Director(Employee):
    def __init__(self, hours_worked, hourly_rate, bonus_coefficient, department):
        super().__init__(hours_worked, hourly_rate, bonus_coefficient)
        self.department = department

 
if __name__ == "__main__":
    senior_employee = SeniorEmployee(hours_worked=160, hourly_rate=30, bonus_coefficient=0.15, additional_experience=5)
    director = Director(hours_worked=170, hourly_rate=40, bonus_coefficient=0.20, department='IT')

    combined_employee = senior_employee + director

    print(f"Общее количество часов: {combined_employee.hours_worked}")
    print(f"Средняя ставка: {combined_employee.hourly_rate:.2f} рублей")
    print(f"Средний коэффициент премии: {combined_employee.bonus_coefficient:.2f}")
 