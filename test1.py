class Person(object):
    def __init__(self,name,age,phone,gender):
        self.name = name
        self.age = age
        self.phone = phone
        self.gender = gender

# check if student's id is valid
# in this case if it is too old, it is not valid
# take 0 as an example
def check(id):
    if id[1]==  "0":
        return "not valid\n"
    else :
        return "valid"

# Boy > 18 valid
# Girl > 20 valid
def check_age_gender(gender,age):
    if gender=="boy" and age > 18:
        return True
    elif gender =="girl" and age > 20:
        return True
    else:
        return False

def check_age(age):
    if age>a:
        return "valid\n"
    else:
        return "not valid"
f = open(r"/Users/waller/ruiqin/test.txt")
lines = f.readlines()

people = []
for line in lines:
    words = line.split()
    people.append(Person(words[0],int(words[1]),words[2],words[3]))
#people = [p1,p2,p3,p4.......]

for person in people:

    print "Name: {} gender: {} age: {} phone: {} verification: {}".format(person.name, person.age, person.phone,person.gender, check_age_gender(person.gender,person.age))


