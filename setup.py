from setuptools import setup, find_packages

setup(
    name='podcast cli',
    version='0.1.0',
    description='Command line interface for podcast',
    author='bugsmaker',
    packages=find_packages(include=['podcast', 'podcast.*']),
    install_requires=[
        # example when define require package
        # 'PyYAML',
        # 'pandas==0.23.3',
        # 'numpy>=1.14.5'
        # 'matplotlib>=2.2.0,<3.0.0'
        'click',
        'colorama'

    ],
    # pip install "example[plotting]" or pip install -e ".[plotting]" if u want install extra requirements
    extras_require={'plotting': ['matplotlib>=2.2.0', 'jupyter']},

    # for lib use when code, setup, testing, not need in prod env
    # setup_requires=['pytest-runner', 'flake8'],
    # tests_require=['pytest'],

    entry_points={
        # execute function main() inside podcast/demo.py when you type podcast
        'console_scripts': ['podcast=podcast.demo:main']
    },
    # declare data to be packaged
    package_data={'exampleproject': ['data/schema.json']}
)