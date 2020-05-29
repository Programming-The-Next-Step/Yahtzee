from setuptools import setup

setup(
       name = 'dr_yahtzee',
       version = '0.0.1',
       author = 'Dana Ravestein',
       author_email = 'dana.ravestein94@gmail.com',
       python_requires = '>= 3.6',
       license = 'MIT',
       packages = ['dr_yahtzee'],
       # import images and text
       include_package_data = True,
       test_suite = 'nose.collector',
       tests_require = ['nose']
)