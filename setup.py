from setuptools import setup, find_packages
import sys, os.path

# Don't import scilab module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scilab'))
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

setup(name='scilab_pkg',
      version=VERSION,
      description='The OpenAI Gym for Science: A platform for your scientific reinforcement learning problem.',
      url='https://github.com/HendrikPN/gym',
      author='OpenAI',
      author_email='hendrik.poulsen-nautrup@uibk.ac.at',
      license='',
      packages=[package for package in find_packages()
                if package.startswith('scilab')],
      zip_safe=False,
      install_requires=[
          'scipy', 'numpy>=1.10.4', 'requests>=2.0', 'six', 'pyglet>=1.2.0',
      ],
      extras_require=extras,
      package_data={'scilab': [
        'envs/classic_control/assets/*.png']
      },
      tests_require=['pytest', 'mock'],
)
