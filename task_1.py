class Employee:
    def __init__(self, hours_worked, hourly_rate, bonus_coefficient):
        self.hours_worked = hours_worked          
        self.hourly_rate = hourly_rate               
        self.bonus_coefficient = bonus_coefficient   

    def calculate_bonus(self):
        base_salary = self.hours_worked * self.hourly_rate   
        bonus = base_salary * self.bonus_coefficient         
        return bonus

 
if __name__ == "__main__":
    employee = Employee(hours_worked=160, hourly_rate=30, bonus_coefficient=0.15)
    
    bonus = employee.calculate_bonus()
    print(f"Размер премии: {bonus:.2f} рублей")