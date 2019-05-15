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
    old_contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.del_contact_in_group(contact.id, group.id, group.name)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    assert len(old_contacts_in_group) - 1 == len(new_contacts_in_group)
    old_contacts_in_group.remove(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
