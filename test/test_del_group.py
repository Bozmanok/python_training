from model.group import Group
import random
import allure


def test_delete_some_group(app, db, check_ui):
    with allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        group = random.choice(old_groups)
    with allure.step('When I delete a group %s from the list' % group):
        app.group.delete_group_by_id(group.id)
    with allure.step('Then the new group list is equal to the old list without the deleted group'):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_delete_first_group(app, db, check_ui):
#     if len(db.get_group_list()) == 0:
#         app.group.create(Group(name="test"))
#     old_groups = db.get_group_list()
#     group = random.choice(old_groups[0:1])
#     app.group.delete_group_by_id(group.id)
#     new_groups = db.get_group_list()
#     assert len(old_groups) - 1 == len(new_groups)
#     old_groups.remove(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#     if check_ui:
#         assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
