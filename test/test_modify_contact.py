from model.contact import Contact
import random
import allure


def test_modify_some_contact_name(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="First test"))
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
        new_contact = Contact(firstname="First mod name", lastname="Last mod name")
        new_contact.id = contact.id
    with allure.step('When I modify a contact %s' % contact):
        app.contact.modify_contact_by_id(contact.id, new_contact)
    with allure.step('Then the new contact list is equal to the old list with the modified contact'):
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact)
        old_contacts.append(new_contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            def clean(contact):
                return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
            db_contacts = map(clean, new_contacts)
            assert sorted(db_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


# def test_modify_first_contact_name(app, db, check_ui):
#     if len(db.get_contact_list()) == 0:
#         app.contact.create(Contact(firstname="First test"))
#     old_contacts = db.get_contact_list()
#     contact = random.choice(old_contacts[0:1])
#     new_contact = Contact(firstname="First new name", lastname="Last new name")
#     new_contact.id = contact.id
#     app.contact.modify_contact_by_id(contact.id, new_contact)
#     new_contacts = db.get_contact_list()
#     old_contacts.remove(contact)
#     old_contacts.append(new_contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#     if check_ui:
#         def clean(contact):
#             return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
#         db_contacts = map(clean, new_contacts)
#         assert sorted(db_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
#
#
# def test_modify_first_contact_dates(app, db, check_ui):
#     if len(db.get_contact_list()) == 0:
#         app.contact.create(Contact(firstname="First test"))
#     old_contacts = db.get_contact_list()
#     contact = random.choice(old_contacts[0:1])
#     new_contact = Contact(bday="30", bmonth="May", byear="2005",
#                       aday="14", amonth="June", ayear="1980")
#     new_contact.id = contact.id
#     app.contact.modify_contact_by_id(contact.id, new_contact)
#     new_contacts = db.get_contact_list()
#     old_contacts.remove(contact)
#     old_contacts.append(new_contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#     if check_ui:
#         def clean(contact):
#             return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
#         db_contacts = map(clean, new_contacts)
#         assert sorted(db_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
