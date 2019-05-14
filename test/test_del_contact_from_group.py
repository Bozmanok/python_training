from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random


def test_del_contact_in_group(app):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="First test"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contacts = orm.get_contact_list()
    groups = orm.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    if len(orm.get_contacts_in_group(group)) == 0:
        app.contact.add_contact_in_group(contact.id, group.name)
    app.contact.del_contact_in_group(contact.id, group.id, group.name)
    contacts_page = app.contact.get_contacts_list_with_group_from_page(group.id)
    contacts_db = orm.get_contacts_in_group(group)
    assert sorted(contacts_page, key=Contact.id_or_max) == sorted(contacts_db, key=Contact.id_or_max)
