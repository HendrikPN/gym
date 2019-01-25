from setuptools import setup, find_packages
import sys, os.path

# Don't import scigym module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scigym'))
from version import VERSION

# Environment-specific dependencies.
extras = {
  'classic_control': ['PyOpenGL'],
}

# Meta dependency groups.
all_deps = []
for group_name in extras:
    all_deps += extras[group_name]
extras['all'] = all_deps

setup(name='scigym_pkg',
      version=VERSION,
      description='SciGym -- The OpenAI Gym for Science: A platform for your scientific reinforcement learning problem.',
      url='https://github.com/HendrikPN/scigym',
      author='OpenAI',
      author_email='hendrik.poulsen-nautrup@uibk.ac.at',
      license='',
      packages=[package for package in find_packages()
                if package.startswith('scigym')],
      zip_safe=False,
      install_requires=[
          'scipy', 'numpy>=1.10.4', 'requests>=2.0', 'six', 'pyglet>=1.2.0',
      ],
      extras_require=extras,
      package_data={'scigym': [
        'envs/classic_control/assets/*.png']
      },
      tests_require=['pytest', 'mock'],
)
