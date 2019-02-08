from scigym import envs, logger
import os

def should_skip_env_spec_for_tests(spec):
    # We skip tests for envs that require dependencies or are otherwise
    # troublesome to run frequently
    ep = spec._entry_point
    # Skip mujoco tests for pull request CI
    # skip_mujoco = not (os.environ.get('MUJOCO_KEY'))
    # if skip_mujoco and (ep.startswith('scigym.envs.mujoco:') or ep.startswith('scigym.envs.robotics:')):
    #     return True
    if (    'GoEnv' in ep or
            'HexEnv' in ep # or
            # (ep.startswith("scigym.envs.atari") and not spec.id.startswith("Pong") and not spec.id.startswith("Seaquest"))
    ):
        logger.warn("Skipping tests for env {}".format(ep))
        return True
    return False

spec_list = [spec for spec in sorted(envs.registry.all(), key=lambda x: x.id) if spec._entry_point is not None and not should_skip_env_spec_for_tests(spec)]