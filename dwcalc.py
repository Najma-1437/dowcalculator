class DateCalculator:
    def _init_(self, year, month, day):
        self.original_year = year
        self.day = day
        if month < 3:
            self.month = month + 12
            self.year = year - 1
        else:
            self.month = month
            self.year = year

    def calculate_day_of_week(self):
        q = self.day
        m = self.month
        K = self.year % 100
        J = self.year // 100

        h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

        days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        return days[h]

    def print_result(self):
        weekday = self.calculate_day_of_week()
        print(f"{self.original_year}-{self.month if self.month <= 12 else self.month - 12}-{self.day} was a {weekday}.")


# Example usage:
date = DateCalculator(1589, 9, 15)
date.print_result()