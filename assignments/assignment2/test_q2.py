""" Tests for question 2 - Spreading Virus """
from hw2_q2 import Agent, Condition, meetup

data0 = (
    Agent("Adam", Condition.SICK),
    Agent("Cure0", Condition.CURE),
    Agent("Cure1", Condition.CURE),
    Agent("Bob", Condition.HEALTHY),
    Agent("Alice", Condition.DEAD),
    Agent("Charlie", Condition.DYING),
    Agent("Vaccine", Condition.SICK),
    Agent("Darlene", Condition.DYING),
    Agent("Emma", Condition.SICK),
    Agent("Cure2", Condition.CURE),
)

data1 = (Agent("Buddy", Condition.CURE), Agent("Holly", Condition.DEAD))

data2 = (
    Agent("Zelda0", Condition.SICK),
    Agent("Zelda1", Condition.SICK),
    Agent("Zelda2", Condition.SICK),
    Agent("Zelda3", Condition.SICK),
    Agent("Zelda4", Condition.DEAD),
    Agent("Zelda5", Condition.HEALTHY),
)

data3 = (
    Agent("Mark", Condition.SICK),
    Agent("Mork", Condition.HEALTHY),
    Agent("Harry", Condition.DYING),
    Agent("Cure", Condition.CURE),
    Agent("Lora", Condition.SICK),
    Agent("Monica", Condition.SICK),
)

data4 = (Agent("Robert", Condition.SICK),)

data5 = ()


def test_data0():
    code_result = set(meetup(data0))
    true_result = {
        Agent(name="Adam", category=Condition.HEALTHY),
        Agent(name="Alice", category=Condition.DEAD),
        Agent(name="Bob", category=Condition.HEALTHY),
        Agent(name="Charlie", category=Condition.SICK),
        Agent(name="Cure0", category=Condition.CURE),
        Agent(name="Cure1", category=Condition.CURE),
        Agent(name="Cure2", category=Condition.CURE),
        Agent(name="Darlene", category=Condition.DEAD),
        Agent(name="Emma", category=Condition.HEALTHY),
        Agent(name="Vaccine", category=Condition.DYING),
    }
    assert code_result == true_result


def test_data1():
    code_result = set(meetup(data1))
    true_result = set(data1)
    assert code_result == true_result


def test_data2():
    code_result = set(meetup(data2))
    true_result = {
        Agent("Zelda0", Condition.DYING),
        Agent("Zelda1", Condition.DYING),
        Agent("Zelda2", Condition.DYING),
        Agent("Zelda3", Condition.DYING),
        Agent("Zelda4", Condition.DEAD),
        Agent("Zelda5", Condition.HEALTHY),
    }
    assert code_result == true_result


def test_data3():
    code_result = set(meetup(data3))
    true_result = {
        Agent("Mark", Condition.DYING),
        Agent("Mork", Condition.HEALTHY),
        Agent("Harry", Condition.DEAD),
        Agent("Cure", Condition.CURE),
        Agent("Lora", Condition.HEALTHY),
        Agent("Monica", Condition.SICK),
    }
    assert code_result == true_result


def test_data4():
    code_result = set(meetup(data4))
    true_result = {Agent("Robert", Condition.SICK)}
    assert code_result == true_result


def test_data5():
    code_result = meetup(data5)
    true_result = []
    assert code_result == true_result


if __name__ == "__main__":
    methods = [f"test_data{num}" for num in range(6)]
    errors = []

    for method in methods:
        try:
            eval(method)()
        except AssertionError as e:
            errors.append(f"Failed when testing method 'test_{method}': {e}")

    if errors:
        raise AssertionError(errors)
    else:
        print("Tests pass successfully.")
