from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Ez Pb',
    version='0.0.1',
    description='Simple python photo booth application',
    long_description=readme,
    author='Joshua Wu',
    author_email='jwu910@gmail.com',
    url='https://github.com/the-after-hours/ez-pb',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
