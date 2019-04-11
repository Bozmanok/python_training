from model.contact import Contact
from random import randrange


def test_modify_some_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="First mod name", lastname="Last mod name")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="First new name", lastname="Last new name")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_dates(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(bday="30", bmonth="May", byear="2005",
                      aday="14", amonth="June", ayear="1980")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
