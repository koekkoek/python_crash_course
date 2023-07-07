from employee import Employee


@pytest.fixture
def person():
    person = Employee("Jan", "de Jong", 20000)


def test_give_default_raise(person):
    person = Employee("Jan", "de Jong", 15000)
    person.give_raise()
    assert person.salary == 20000


def test_give_custom_raise(person):
    person.give_raise(50000)
    assert person.salary == 65000
