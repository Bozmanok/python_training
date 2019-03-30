from model.contact import Contact


def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First test"))
    app.contact.modify_first_contact(Contact(firstname="First new name", lastname="Last new name"))


def test_modify_first_contact_dates(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First test"))
    app.contact.modify_first_contact(Contact(bday="30", bmonth="May", byear="2005",
                                             aday="14", amonth="June", ayear="1980"))
