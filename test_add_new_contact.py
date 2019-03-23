# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from contact import Contact


class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_new_contact(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_new_contact(wd, Contact(firstname="First test", middlename="Middle test", lastname="Last test",
                                            path_to_photo="C:\\Users\\Asus\\Desktop\\test_image.jpg",
                                            nickname="Nick test", title="Title test", company="Company test",
                                            address="Address test", home="12345", mobile="67890", work="54321",
                                            fax="09876", email="test@test.tu", email2="test2@test.tu",
                                            email3="test3@test.tu", homepage="www.test.tu", bday="15", bmonth="January",
                                            byear="1990", aday="15", amonth="January", ayear="1990", new_group="[none]",
                                            address2="Address test", phone2="34567", notes="Notes test"))
        self.logout(wd)

    def test_add_new_empty_contact(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_new_contact(wd, Contact(firstname="", middlename="", lastname="", path_to_photo="", nickname="",
                                            title="", company="", address="", home="", mobile="", work="", fax="",
                                            email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="",
                                            aday="", amonth="-", ayear="", new_group="", address2="", phone2="",
                                            notes=""))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_list_contacts_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_new_contact(self, wd, contact):
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        # fill new contact main form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        if contact.path_to_photo != "":
            wd.find_element_by_name("photo").send_keys(contact.path_to_photo)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_xpath("//option[@value='" + contact.bday + "']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_xpath("//option[@value='" + contact.bmonth + "']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_xpath("(//option[@value='" + contact.aday + "'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_xpath("(//option[@value='" + contact.amonth + "'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_xpath("//option[@value='" + contact.new_group + "']").click()
        # fill new contact secondary form
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # create new contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_list_contacts_page(wd)

    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
