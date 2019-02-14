from setuptools import setup

with open('README.rst') as README:
    long_description = README.read()
    long_description = long_description[long_description.index('Description'):]

setup(
    name='until_nonidle',
    version='0.4',
    description='Execute something as long as the user is idling.',
    long_description=long_description,
    install_requires=['psutil', 'xprintidle'],
    url='http://github.com/enricobacis/until_nonidle',
    author='Enrico Bacis',
    author_email='enrico.bacis@gmail.com',
    license='MIT',
    packages=['until_nonidle'],
    scripts=['scripts/until_nonidle'],
    keywords='idle lock lockscreen action'
)
