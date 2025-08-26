PERCENTAGE = 100

principal_amount = float(input('Input your Principal Amount : '))

rate_of_interest = float(input('Input the Rate of Interest as percentage (without a percentage symbol): '))

time = float(input('Input the Time in years : '))

simple_interest = (principal_amount * rate_of_interest * time) / PERCENTAGE

print('The simple interest(%), based on the values you inputted will be: ', simple_interest)

