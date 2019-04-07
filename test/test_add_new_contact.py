# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="First test", middlename="Middle test", lastname="Last test",
                               path_to_photo="C:\\Users\\Asus\\Desktop\\test_image.jpg",
                               nickname="Nick test", title="Title test", company="Company test",
                               address="Address test", home="12345", mobile="67890", work="54321",
                               fax="09876", email="test@test.tu", email2="test2@test.tu",
                               email3="test3@test.tu", homepage="www.test.tu", bday="15", bmonth="January",
                               byear="1990", aday="30", amonth="September", ayear="2000", new_group="[none]",
                               address2="Address test", phone2="34567", notes="Notes test"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_new_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="", middlename="", lastname="", path_to_photo=None, nickname="",
                               title="", company="", address="", home="", mobile="", work="", fax="",
                               email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="",
                               aday="", amonth="-", ayear="", new_group=None, address2="", phone2="",
                               notes=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
