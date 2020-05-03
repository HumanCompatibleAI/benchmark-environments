"""Adaptation of MuJoCo environments for IRL."""

from gym.envs.mujoco import (
    ant_v3,
    half_cheetah_v3,
    hopper_v3,
    humanoid_v3,
    swimmer_v3,
    walker2d_v3,
)


def _include_position_in_observation(cls):
    old_init = cls.__init__

    def new_init(*args, **kwargs):
        kwargs["exclude_current_positions_from_observation"] = False
        old_init(*args, **kwargs)

    cls.__init__ = new_init
    return cls


def _no_early_termination(cls):
    cls.done = False
    return cls


@_include_position_in_observation
@_no_early_termination
class AntEnv(ant_v3.AntEnv):
    """Ant with position observation and no early termination."""


@_include_position_in_observation
@_no_early_termination
class HalfCheetahEnv(half_cheetah_v3.HalfCheetahEnv):
    """HalfCheetah with position observation and no early termination."""


@_include_position_in_observation
@_no_early_termination
class HopperEnv(hopper_v3.HopperEnv):
    """Hopper with position observation and no early termination."""


@_include_position_in_observation
@_no_early_termination
class HumanoidEnv(humanoid_v3.HumanoidEnv):
    """Humanoid with position observation and no early termination."""


@_include_position_in_observation
@_no_early_termination
class SwimmerEnv(swimmer_v3.SwimmerEnv):
    """Swimmer with position observation and no early termination."""


@_include_position_in_observation
@_no_early_termination
class Walker2dEnv(walker2d_v3.Walker2dEnv):
    """Walker2d with position observation and no early termination."""
