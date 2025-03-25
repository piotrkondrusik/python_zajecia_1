

class Person:
    ALLOWED_GENDERS = ("MALE", "FEMALE")
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.check_and_assign_gender(gender)

    def check_and_assign_gender(self, gender):
        if gender in self.ALLOWED_GENDERS:
            self.gender = gender
        else:
            raise ValueError("bledna plec")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

grzesiu = Person("Grzegorz", "Tester", 20, "MALE")

print(grzesiu)