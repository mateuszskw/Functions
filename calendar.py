months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def month(n):
  if n < 0 or n > 12:
    raise Exception("Month number out of range")
  return months[n - 1]
