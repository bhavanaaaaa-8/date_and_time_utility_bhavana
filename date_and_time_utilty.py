from datetime import datetime, date
def get_valid_date(prompt):
    while True:
        user_input = input(prompt).strip()

        try:
            return datetime.strptime(
                user_input, "%d-%m-%Y"
            ).date()

        except ValueError:
            print(
                "Invalid date! Enter a real date "
                "in DD-MM-YYYY format."
            )
def calculate_age(dob):
    today = date.today()

    if dob > today:
        raise ValueError("Date of birth cannot be in the future.")

    age = today.year - dob.year

    # Handle birthdays that have not occurred this year
    try:
        birthday_this_year = dob.replace(year=today.year)
    except ValueError:
        # February 29 in a non-leap year
        birthday_this_year = date(today.year, 2, 28)

    if today < birthday_this_year:
        age -= 1
    return age
