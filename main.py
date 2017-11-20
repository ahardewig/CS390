import random
first = raw_input("What is your first name? ")
last = raw_input("What is your last name? ")
major = raw_input("What is your major? ")
age = raw_input("What is your age? ")
print
print
print "________________________________________________"
print "Name: " _+ first + " " + last
print "Major: " + major
print "Age: " + age
print "Email: " + first[0:1].lower() + last.lower() + "@purdue.edu"
print "PUID: 00" + str(random.randrange(10000000,99999999))
print "________________________________________________"
