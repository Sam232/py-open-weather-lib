from setuptools import find_packages, setup

setup(
    name='openweather',
    packages=find_packages(include=['openweather']),
    version='0.1.0',
    description='This library is used to get the current and forecast weather data from the Open Weather Library',
    author='Samuel Fiatse',
    license='MIT',
    install_requires=['requests', 'flask'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.0.1'],
    test_suite='tests',
)
