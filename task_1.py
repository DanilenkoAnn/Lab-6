class Employee:
    def __init__(self, hours_worked, hourly_rate, bonus_coefficient):
        
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.bonus_coefficient = bonus_coefficient


    def calculate_salary(self):
        
        base_salary = self.hours_worked * self.hourly_rate
        bonus = base_salary * self.bonus_coefficient
        total_salary = base_salary + bonus
        return total_salary

# Пример использования класса
if __name__ == "__main__":
    # Создаем объект сотрудника
    employee = Employee(hours_worked=160, hourly_rate=20, bonus_coefficient=0.1)
    
    # Рассчитываем зарплату
    total_salary = employee.calculate_salary()
    
    print(f"Общая зарплата сотрудника: {total_salary:.2f} рублей")