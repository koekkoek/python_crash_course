from employee import Employee
import pytest


@pytest.fixture
def person():
    return Employee("Jan", "de Jong", 20000)


def test_give_default_raise(person):
    person.give_raise()
    assert person.salary == 25000


def test_give_custom_raise(person):
    person.give_raise(50000)
    assert person.salary == 70000
