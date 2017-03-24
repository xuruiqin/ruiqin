class Person(object):
    def __init__(self,name,studentid,phone,gender):
        self.name = name
        self.studentid = studentid
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



f = open(r"/home/ruiqin/ruiqin/test.txt")
lines = f.readlines()


people = []
for line in lines:
    words = line.split()
    people.append(Person(words[0],words[3],words[2],words[1]))
#people = [p1,p2,p3,p4.......]


for person in people:
    print "Name: {} gender: {} age: {} phone: {} verification: {}".format(person.name, person.studentid, person.gender,person.phone,check(person.studentid))


