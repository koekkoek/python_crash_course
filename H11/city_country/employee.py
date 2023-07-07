class Employee:
    def __init__(self, first, last, salary) -> None:
        self.first_name = first
        self.last_name = last
        self.salary = salary

    def give_raise(self, give_raise=5000):
        self.salary += give_raise
