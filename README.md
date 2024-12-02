# Movie Decider Algorithm
### Overview
This Python script determines who among a predefined group of people gets to decide the movie for a given Saturday. It
operates based on an initial configuration and calculates the decision schedule dynamically. The program identifies if
today is Saturday or not and outputs the relevant decision-maker or the next upcoming decision day.

### Features
- Dynamic Saturday Check: Determines if the current date is Saturday and outputs the decision for the day.
- Next Decision Forecast: If it’s not Saturday, the script calculates the next Saturday and shows who will decide then.
- Customizable Configuration: Allows you to define:
  - The list of people in rotation.
  - The starting date of the decision schedule.
  - Ascending or descending order for decision rotation.
  - Optional day offset from the start date for testing.
  - Initial Configuration
### Variables
- people: A list of decision-makers (e.g., ["1", "2", "3", "4"]).
- start_date: The initial date the rotation begins (format: DD/MM/YYYY).
- ascending: Determines if the order of decision rotates forward (True) or backward (False).
- delta_days: A day offset to simulate different dates without changing the system clock.
### How It Works
- Input Date: The script calculates the current date based on the start_date and delta_days.
- Calculate Rotation: The person deciding is calculated based on the days elapsed since the start_date.
- Check Saturday: If the current date is Saturday:
  - Prints the name of the person deciding that day.
- Not Saturday:
  - Calculates the next Saturday.
  Prints the person who will decide on the next Saturday and its date.
### Example Output
- Scenario 1: Current Date is a Saturday
  ```
  Today is Saturday!
  1 decides the movie this Saturday.
  ```
- Scenario 2: Current Date is not a Saturday
  ```
  Today is not Saturday! :(
  The next person to decide is 2 on 07/12/2024.
  ```
### Usage
  Run the script using Python 3:

```bash
python main.py
```

You can adjust the configuration variables (people, start_date, ascending, and delta_days) within the script to test different scenarios.

Enjoy scheduling your movie nights! 🎬