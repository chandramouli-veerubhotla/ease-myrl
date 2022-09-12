import typing as t
import numpy as np


class QtA:
    """
    Estimates action values. 

    Maintains expected rewards for the given action in an efficient way.    
    """
    
    def __init__(self, total_actions:int, initail_qn: float = 0) -> None:
        self._qn = np.zeros((total_actions,)) + initail_qn
        self.n = np.zeros((total_actions, ))
        self._total_actions = total_actions
    
    def __call__(self, action: int, reward: float, alpha: float | None = None):
        qn = self._qn[action]

        if alpha is None:
            alpha = 1/ (self.n[action])

        # Incremental approach of updating Qn
        self._qn[action] += alpha * (reward - qn)
    
    def __len__(self):
        return self._total_actions

    def get_estimates(self, actions: t.List[int]):
        return self._qn[actions]
