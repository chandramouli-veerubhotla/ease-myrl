import typing as t
import numpy as np
from collections import Counter


def random_method(Qt_a: np.ndarray, actions: t.List[int] | None = None, probabilities: t.List[float] | None = None) -> t.Tuple[int, float]:
    """
    Selects an action randomly from the possible actions.

    :params
    Qt_a: Numpy Array (1D) - Expected maximum reward computed for each action (index of the list).
    actions: List[int] (optional) - If provided, only those actions are considered for selection, else, all the actions are considered.
    probabilities: List[float] (optional) - If provided, selection of action will be based on probabilities, else, equally probable.

    :return
    action (index of the list) [int], expected maximum reward [float]
    """
    if actions is None:
        actions = list(range(0, len(Qt_a)))  # all actions available
    
    assert len(probabilities) == len(actions), f"Expecting probabilites provided should be same as actions available. Expected {len(actions)} but got {len(probabilities)}"
    action = np.random.choice(actions, p=probabilities)
    return action, Qt_a[action]


def greedy_method(Qt_a: np.ndarray, actions: t.List[int] | None = None) -> t.Tuple[int, float]:
    """
    Exploits the knowledge of expected rewards.

    Greedy method picks the action that has maximum expected reward.
    If two or more actions have maximum expected reward, then action is selected randomly (all actions have equal probability).

    :params
    Qt_a: Numpy Array (1D) - Expected maximum reward computed for each action (index of the list).
    actions: List[int] (optional) - If provided, only those actions are considered for selection, else, all the actions are considered.

    :return
    action (index of the list) [int], expected maximum reward [float] 
    """
    if actions is None:
        actions = list(range(0, len(Qt_a)))  # all actions available
    
    # Count and find if maximum expected reward is available for 2 or more actions
    reward_counter = Counter(Qt_a[actions])
    action = np.argmax(Qt_a)

    if reward_counter[Qt_a[action]] > 1:
        return random_method(Qt_a, actions=actions, probabilities=None)
    
    return action, Qt_a[action]


def epsilon_greedy_method(Qt_a: np.ndarray, actions: t.List[int] | None = None, epsilon: float = 0.1) -> t.Tuple[int, float]:
    """
    Trades off between exploration and exploitation.

    Epsilon helps to managing tradeoff between exploration and exploitation.
    This approach applies probablity `epsilon` for exploitation and `1-epsilon` probability equally distributed for all possible actions.

    :params
    Qt_a: Numpy Array (1D) - Expected maximum reward computed for each action (index of the list).
    actions: List[int] (optional) - If provided, only those actions are considered for selection, else, all the actions are considered.
    epsilon: float (defaults 0.1, range [0-1]) - Applies probability for exploitation.

    :return
    action (index of the list) [int], expected maximum reward [float] 
    """
    if actions is None:
        actions = list(range(0, len(Qt_a)))  # all actions available
    
    probabilities = [(1-epsilon)/len(actions)] * len(actions)

    # Greedy selection
    action, _ = greedy_method(Qt_a, actions=actions)
    probabilities[action] += epsilon  # increase probability for greedy action with `epsilon` more probability

    # Apply random selection with computed probabilities
    return random_method(Qt_a, actions=actions, probabilities=probabilities)


def ucb_method():
    pass

