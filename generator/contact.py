# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", path_to_photo=None, nickname="",
                               title="", company="", address="", homephone="", mobilephone="", workphone="", fax="",
                               email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="",
                               aday="", amonth="-", ayear="", new_group=None, address2="", secondaryphone="",
                               notes="")] + [
    Contact(firstname=random_string("firstname", 20), middlename=random_string("middlename", 20),
            lastname=random_string("lastname", 20), path_to_photo=None, nickname=random_string("nickname", 20),
            title=random_string("title", 10), company=random_string("company", 10), address=random_string("address", 10),
            homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10),
            workphone=random_string("workphone", 10), fax=random_string("fax", 10), email=random_string("email", 10),
            email2=random_string("email2", 10), email3=random_string("email3", 10), homepage=random_string("homepage", 10),
            bday="15", bmonth="January", byear=random_string("byear", 5), aday="30", amonth="September",
            ayear=random_string("ayear", 5), new_group=None, address2=random_string("address2", 20),
            secondaryphone=random_string("secondaryphone", 10), notes=random_string("notes", 10))
    for i in range(3)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
