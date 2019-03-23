# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="First test", middlename="Middle test", lastname="Last test",
                                        path_to_photo="C:\\Users\\Asus\\Desktop\\test_image.jpg",
                                        nickname="Nick test", title="Title test", company="Company test",
                                        address="Address test", home="12345", mobile="67890", work="54321",
                                        fax="09876", email="test@test.tu", email2="test2@test.tu",
                                        email3="test3@test.tu", homepage="www.test.tu", bday="15", bmonth="January",
                                        byear="1990", aday="15", amonth="January", ayear="1990", new_group="[none]",
                                        address2="Address test", phone2="34567", notes="Notes test"))
    app.logout()


def test_add_new_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="", middlename="", lastname="", path_to_photo="", nickname="",
                                        title="", company="", address="", home="", mobile="", work="", fax="",
                                        email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="",
                                        aday="", amonth="-", ayear="", new_group="", address2="", phone2="",
                                        notes=""))
    app.logout()
