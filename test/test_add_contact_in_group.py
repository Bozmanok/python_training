from model.contact import Contact
import random


def test_add_contact_in_group(app, db):
    groups = db.get_group_list()
    group = random.choice(groups)
    contact = Contact(firstname="first test", lastname="last test", new_group=group.name)
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
