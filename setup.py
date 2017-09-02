

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
# requirements = [pkg.split('=')[0] for pkg in open('requirements.txt').readlines()]

# description = "Commandline tool to listen all radio stations of Nepal"

# long_description = open("README.rst").read()

classifiers = ['Environment :: Console',
               'Programming Language :: Python :: 3'
               ]

# version = open('CHANGES.txt').readlines()[0][1:].strip()

setup(name='lock-pass',
      version= '1.0',
      description= "To save username and password",
      author='Shital Babu Luitel',
      author_email='ctalluitel@gmail.com',
      url='https://github.com/shitalluitel/',
      scripts=['src/lock-pass',],
      packages=['lock_pass'],
      package_dir = {'lock_pass': 'src/lock_pass'},
      classifiers=classifiers
    )