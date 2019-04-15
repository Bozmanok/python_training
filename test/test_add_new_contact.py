# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="First 111 test", middlename="Middle test", lastname="Last test",
                               path_to_photo="C:\\Users\\Asus\\Desktop\\test_image.jpg",
                               nickname="Nick test", title="Title test", company="Company test",
                               address="Address test", homephone="12345", mobilephone="67890", workphone="54321",
                               fax="09876", email="test@test.tu", email2="test2@test.tu",
                               email3="test3@test.tu", homepage="www.test.tu", bday="15", bmonth="January",
                               byear="1990", aday="30", amonth="September", ayear="2000", new_group="[none]",
                               address2="Address test", secondaryphone="34567", notes="Notes test")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_new_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", path_to_photo=None, nickname="",
                               title="", company="", address="", homephone="", mobilephone="", workphone="", fax="",
                               email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="",
                               aday="", amonth="-", ayear="", new_group=None, address2="", secondaryphone="",
                               notes="")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
