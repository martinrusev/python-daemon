from setuptools import setup
import os

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()
 
version = '0.1.0'
 
setup(
    name='python_daemon',
    version=version,
    description="A simple python daemon that daemonizes python applications",
    long_description=read('README.rst'),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='python, daemon,',
    author='Martin Rusev',
    author_email='martinrusev@live.com',
    url='https://github.com/martinrusev/python-daemon',
    license='MIT',
    py_modules=['daemon'],
    zip_safe=False,
    install_requires=[],
    include_package_data=True,
) 
