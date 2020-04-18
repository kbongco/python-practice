#Found on CodingBat
#the parameter weekday is True if it is a weekday
#the parameter vacation is true if we are on vacation
#we sleep in on a weekday or we are on vacation 
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False