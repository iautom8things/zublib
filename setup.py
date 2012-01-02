from distutils.core import setup

setup(
    name='ZubLib',
    version='0.1.0',
    author='Manuel Zubieta',
    author_email='Manuel Zubieta',
    packages=['zublib'],
    url='http://github.com/mazubieta/zublib',
    license='LICENSE-MIT.txt',
    description='miscellaneous helper funcs',
    long_description=open('README.txt').read(),
    install_requires=[
        "BeautifulSoup >= 3.2.0",
        ],
)
