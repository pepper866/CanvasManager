from datetime import timedelta

# helper method for date range
# All credit goes to this source:
# https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


# helper method to get abbreviation for the day
def getDay(x):
  if x == 0:
    return "M"
  elif x == 1:
    return "T"
  elif x == 2:
    return "W"
  elif x == 3:
    return "R"
  elif x == 4:
    return "F"
