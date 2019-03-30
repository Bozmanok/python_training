from model.contact import Contact


def test_update_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="First update", middlename="Middle update", lastname="Last update",
                                             path_to_photo="", nickname="Nick update", title="Title update", company="Company update",
                                             address="Address update", home="home update", mobile="mobile update", work="work update",
                                             fax="fax update", email="update@update.tu", email2="update2@update.tu",
                                             email3="update3@update.tu", homepage="www.update.tu", bday="30", bmonth="May",
                                             byear="2005", aday="14", amonth="June", ayear="1980", new_group="",
                                             address2="Address update", phone2="phone2 update", notes="Notes update"))
    app.session.logout()
