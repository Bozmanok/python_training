from model.group import Group


def test_update_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group(Group(name="test_2", header="test_2", footer="test_2"))
    app.session.logout()
