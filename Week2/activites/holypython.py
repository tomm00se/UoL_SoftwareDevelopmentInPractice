#Example 1
greek_island = "Santorini"

#Example 2
earth_age_bln = 4.4
univserse_age_bln = 14
earth_age_bln += 0.1 # += is a shorthand for earth_age_bln = earth_age_bln + 0.1

print("The age of the Earth is", earth_age_bln, "billion years old")

#Example 3
asia_wishlist = ["Japan", "China", "South Korea", "India", "Thailand"] # = is an assignment operator

#Example 4
msg = "Hello World"
if msg == "Hello World": # == is a comparison operator
    print("I'm a programmer")
else:
    print("I'm not a programmer")

#Example 5

"net_earnings" = 10000000
if "net_earnings" >= 10000000:
    print("You are rich")
else:
    print("You are less rich?")

#Example 6

lst = ["football", "basketball", "tennis", "golf", "rock climbing"]
if "basketball" not in lst:
    print("But I love basketball ;-;")

#Example 7

web_data = ["techresearch and computervision"]
if "@" in web_data:
    print("Email address")
elif "0123456789" in web_data:
    print("Phone number")
else:
    print("Neither email nor phone number")

#Example 8

a = 10 + 20
b = 100 - 1
c = 50 / 7
d = 50 // 7
e = 10 % 8
f = 5 ** 2

print(a, b, c, d, e, f, sep="\n")