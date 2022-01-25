from setuptools import find_packages, setup

setup(
    name='exulercrawler',
    packages=find_packages(include=['src']),
    version='1.0.0',
    description='Exuler Crawler',
    author='Pranav Parge',
    license='MIT',
    install_requires=['requests~=2.27.0', 'beautifulsoup4~=4.10.0'],
)
