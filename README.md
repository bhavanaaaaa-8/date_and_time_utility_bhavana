# Python Date and Time Utility

## Description
A Python utility program that performs common date and time operations using Python's built-in `datetime` module. It calculates age, finds the number of days between dates, counts working days, and displays formatted date-time values.

## Features
- **Age Calculator:** Calculates age in years using the date of birth.
- **Days Between Dates:** Calculates the number of days between two dates.
- **Working Days Calculator:** Counts weekdays, excluding Saturdays and Sundays.
- **Date-Time Formatting:** Displays the current date and time in a readable format.
- **Date Validation:** Rejects invalid dates and prompts the user to enter a valid date.
- **Leap Year Handling:** Correctly validates leap days and handles birthdays on 29 February.
- **Error Handling:** Prevents invalid date input and future dates of birth.

## Requirements
- Python 3.x
- Built-in `datetime` module

No external libraries are required.

## How to Run
1. Save the Python program as `date_utility.py`.
2. Open a terminal or command prompt in the folder containing the file.
3. Run the following command:

```bash
python date_utility.py
```

## Date Format
Enter dates in the following format:

`DD-MM-YYYY`

Example: `26-10-2026`

## Example Output

```text
1. Calculate age
2. Days between dates
3. Calculate working days
4. Display formatted date and time

Enter your choice (1-4): 2
Enter first date (DD-MM-YYYY): 27-02-2024
Enter second date (DD-MM-YYYY): 01-03-2024
Days between: 3
```

## Python Concepts Used
- Functions and reusable code
- `datetime`, `date`, and `timedelta`
- Date parsing with `strptime()`
- Date formatting with `strftime()`
- Input validation using `try-except`
- Loops and conditional statements
- Leap year handling

## Limitations
- Working days exclude weekends but not public holidays.
- Working-day counts include both the start and end dates if they are weekdays.
- The age calculator treats 28 February as the birthday for a 29 February birth date in non-leap years.

## Author
Created as a Python practice project to learn date calculations, validation, and formatting.
