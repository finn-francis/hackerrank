# https://www.hackerrank.com/challenges/the-time-in-words/problem

# 1 - Filter on the hour times
# 2 - Find if it's 'past' or 'to'
# 3 - Find if it's quarter or half
# 4 - calculate minutes remaining (if relevent)

singles_and_tens = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
    9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
    16: "sixteen", 17: "seventeen", 18: 'eighteen', 19: "nineteen"
}

def time_in_words(hours, minutes):
    hour = singles_and_tens[hours]
    next_hour = hours + 1
    next_hour = "one" if next_hour == 13 else singles_and_tens[next_hour]

    if minutes == 0:
        return "{} o' clock".format(hour)

    past = minutes <= 30
    past_or_to = "past" if past else "to"
    hour = hour if past else next_hour

    if minutes == 30:
        minute = "half"
    elif minutes % 15 == 0:
        minute = "quarter"
    else:
        total_minutes = minutes if past else 60 - minutes
        if total_minutes < 19:
            number_string = singles_and_tens[total_minutes]
        else:
            lsd = int(str(total_minutes)[-1])
            number_string = "twenty {}".format(singles_and_tens[lsd])
        pluralize = "" if minutes == 1 else "s"
        minute = "{} minute{}".format(number_string, pluralize)

    return "{} {} {}".format(minute, past_or_to, hour)
