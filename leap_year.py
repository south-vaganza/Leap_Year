year = int(input('Year: 1990')) in range(1900, 10**5+1)

if year % 4 == 0 and (year/4) % 2 == 0:
    is_leap = True
else:
    is_leap = False

print(is_leap)

# Don't know if this is correct.
