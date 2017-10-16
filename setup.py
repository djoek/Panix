from setuptools import setup

setup(
    name='panix',
    author='djoek',
    author_email='github@djoek.net',
    version='1.0',
    url='https://github.com/djoek/Panix',
    description='Panix is a python3 library providing convenient access to NXAPI',
    packages=[
        'panix',
        'panix.helpers'
    ],
    install_requires=[
        'requests',
    ],
    include_package_data=True,
)
