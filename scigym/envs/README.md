# Envs

These are the core integrated environments. Note that we may later
restructure any of the files, but will keep the environments available
at the relevant package's top-level. So for example, you should access
`CartPoleEnv` as follows:

```
# Will be supported in future releases
from scigym.envs import classic_control
classic_control.cartpole
```

Rather than:

```
# May break in future releases
from scigym.envs.classic_control import cartpole
cartpole.CartPoleEnv
```

## How to create new environments for SciGym

* Create a new repo called gym-foo, which should also be a PIP package. A simple template can be found [here](https://github.com/HendrikPN/gym-template).

* It should have at least the following files:
  ```sh
  gym-foo/
    README.md
    setup.py
    gym_foo/
      __init__.py
      envs/
        __init__.py
        foo_env.py
        foo_extrahard_env.py
  ```

* `gym-foo/setup.py` should have:

  ```python
  from setuptools import setup

  setup(name='gym_foo',
        version='0.0.1',
        install_requires=['scigym']  # And any other dependencies foo needs
  )  
  ```

* `gym-foo/gym_foo/__init__.py` should have:
  ```python
  from scigym.envs.registration import register

  register(
      id='foo-v0',
      entry_point='gym_foo.envs:FooEnv',
  )
  register(
      id='foo-extrahard-v0',
      entry_point='gym_foo.envs:FooExtraHardEnv',
  )
  ```

* `gym-foo/gym_foo/envs/__init__.py` should have:
  ```python
  from gym_foo.envs.foo_env import FooEnv
  from gym_foo.envs.foo_extrahard_env import FooExtraHardEnv
  ```

* `gym-foo/gym_foo/envs/foo_env.py` should look something like:
  ```python
  import scigym
  from scigym import error, spaces, utils
  from scigym.utils import seeding

  class FooEnv(scigym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
      ...
    def step(self, action):
      ...
    def reset(self):
      ...
    def render(self, mode='human', close=False):
      ...
  ```

## How to add new environments to Gym, within this repo (not recommended for new environments)

1. Write your environment in an existing collection or a new collection. All collections are subfolders of `/scigym/envs'.
2. Import your environment into the `__init__.py` file of the collection. This file will be located at `/scigym/envs/my_collection/__init__.py`. Add `from scigym.envs.my_collection.my_awesome_env import MyEnv` to this file.
3. Register your env in `/scigym/envs/__init__.py`:

 ```
register(
		id='MyEnv-v0',
		entry_point='scigym.envs.my_collection:MyEnv',
)
```
