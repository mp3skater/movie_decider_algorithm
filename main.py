from datetime import datetime, timedelta

# Initial configuration
people = ["1", "2", "3", "4"]
start_date = "30/11/2024"
ascending = True  # forward or backward
delta_days = 0  # DON'T PUT NEGATIVE
current_date = datetime.strptime(start_date, "%d/%m/%Y") + timedelta(days=delta_days)


def movie_decider(date):
    global ascending
    days_since_start = (date - datetime.strptime(start_date, "%d/%m/%Y")).days + 7
    total_people = len(people)

    if ascending:
        index = days_since_start % ((total_people - 1) * 2)
        if index >= total_people:
            index = (total_people - 1) * 2 - index
    else:
        index = (days_since_start % ((total_people - 1) * 2))
        if index >= total_people:
            index = (total_people - 1) * 2 - index

    if date.weekday() == 5:
        print("Today is Saturday!")
        print(f"{people[index]} decides the movie this Saturday.")
    else:
        days_until_saturday = (5 - date.weekday()) % 7
        next_saturday = date + timedelta(days=days_until_saturday)
        print("Today is not Saturday! :(")
        print(f"The next person to decide is {people[index]} on {next_saturday.strftime('%d/%m/%Y')}.")


if __name__ == '__main__':
    movie_decider(current_date)
