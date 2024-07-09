from collections import namedtuple
from enum import Enum
from itertools import chain, zip_longest

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks.
    Taken directly from https://docs.python.org/3/library/itertools.html#itertools-recipes.

    Example
    -------
    grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def treat_cure(left, right):
    if right is None:
        return (left,)
    if right.category is Condition.CURE:
        return left, right
    elif right.category is Condition.SICK:
        return left, Agent(right.name, Condition.HEALTHY)
    elif right.category is Condition.DYING:
        return left, Agent(right.name, Condition.SICK)


def treat_sick(left, right):
    if right is None:
        return (left,)
    if right.category is Condition.CURE:
        return Agent(left.name, Condition.HEALTHY), right
    elif right.category is Condition.SICK:
        return Agent(left.name, Condition.DYING), Agent(right.name, Condition.DYING)
    elif right.category is Condition.DYING:
        return Agent(left.name, Condition.DYING), Agent(right.name, Condition.DEAD)


def treat_dying(left, right):
    if right is None:
        return (left,)
    if right.category is Condition.CURE:
        return Agent(left.name, Condition.SICK), right
    elif right.category is Condition.SICK:
        return Agent(left.name, Condition.DEAD), Agent(right.name, Condition.DYING)
    elif right.category is Condition.DYING:
        return Agent(left.name, Condition.DEAD), Agent(right.name, Condition.DEAD)


condition_to_function_switch = {
    Condition.CURE: treat_cure,
    Condition.SICK: treat_sick,
    Condition.DYING: treat_dying,
}


def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        Condition, containing a 'name' field and a 'category' field, with 'category' being
        of the condition Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """
    # First we filter our original agents listing - DEAD and HEALTHY ones
    # are immediately thrown to the "updated_listing" list which we'll
    # return, and the rest will be processed.
    relevant_agents = []
    updated_listing = []
    for agent in agent_listing:
        if (agent.category is Condition.DEAD) or (agent.category is Condition.HEALTHY):
            updated_listing.append((agent,))
        else:
            relevant_agents.append(agent)
    for inp in grouper(relevant_agents, 2):  # [[Agent, Agent], [Agent, None]]
        # inp = [Agent, Agent] or [Agent, None]
        updated_listing.append(
            condition_to_function_switch[inp[0].category](inp[0], inp[1])
        )
    updated_listing = chain.from_iterable(
        updated_listing
    )  # [(Agent,Agent), (Agent,)] -> [a,b,c,d]
    return list(updated_listing)


if __name__ == "__main__":
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
    meetup(data0)
