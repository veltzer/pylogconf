import setuptools

import sys
if not sys.version_info[0] == 3:
    sys.exit("Sorry, only python version 3 is supported")

setuptools.setup(
    name='pylogconf',
    version='0.0.4',
    description='pylogconf is a logging configurator for python logging',
    long_description='pylogconf is a logging configurator for python logging',
    url='https://veltzer.github.io/pylogconf',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License'
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='python logging configuration easy',
    py_modules=['pylogconf'],
    install_requires=[
        'logging_tree',
        'pyfakeuse',
    ],
)
