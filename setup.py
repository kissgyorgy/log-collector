from setuptools import setup, find_packages


setup(
    name = 'logcollector',
    version = '0.1.0',
    author = 'Kiss György',
    description = 'Log collector task for Job application',
    modules = find_packages(),
    entry_points = {'console_scripts': ['logcollector = logcollector.commands:logcollector']},
    install_requires = ['flask', 'sqlalchemy', 'flask-sqlalchemy', 'click']
)
