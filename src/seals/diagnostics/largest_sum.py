"""Environment testing scalability to high-dimensionality."""

from gym import spaces
import numpy as np

from seals import base_envs


class LargestSumEnv(base_envs.ResettableMDP):
    """High-dimensional linear classification problem.

    This environment evaluates how algorithms scale with increasing
    dimensionality.  It is a classification task with binary actions
    and uniformly sampled states s in [0, 1]**L.  The agent is
    rewarded for taking action 1 if the sum of the first half x[:L//2]
    is greater than the sum of the second half x[L//2:], and otherwise
    is rewarded for taking action 0.
    """

    def __init__(self, length: int = 50):
        """Build environment.

        Args:
            length: dimensionality of state space vector.
        """
        self._length = length
        state_space = spaces.Box(low=0.0, high=1.0, shape=(length,))
        super().__init__(
            state_space=state_space, action_space=spaces.Discrete(2),
        )

    def terminal(self, state: np.ndarray, n_actions_taken: int) -> bool:
        """Always returns False."""
        return False

    def initial_state(self) -> np.ndarray:
        """Returns vector sampled uniformly in [0, 1]**L."""
        return self.rand_state.rand(self._length)

    def reward(self, state: np.ndarray, act: int, next_state: np.ndarray) -> float:
        """Returns positive reward for action being the right label."""
        n = self._length
        label = np.sum(state[: n // 2]) > np.sum(state[n // 2 :])
        return float(act == label)

    def transition(self, state: np.ndarray, action: int) -> np.ndarray:
        """Returns same state."""
        return state
