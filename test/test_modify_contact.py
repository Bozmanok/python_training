from model.contact import Contact


def test_modify_first_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="First new name", lastname="Last new name"))
    app.session.logout()


def test_modify_first_contact_dates(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(bday="30", bmonth="May", byear="2005",
                                             aday="14", amonth="June", ayear="1980"))
    app.session.logout()
