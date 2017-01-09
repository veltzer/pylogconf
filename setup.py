import setuptools

import sys
if not sys.version_info[0] == 3:
    sys.exit("Sorry, only python version 3 is supported")

setuptools.setup(
    name='pylogconf',
    version='0.0.1',
    description='pylogconf is a logging configurator for python logging',
    long_description='pylogconf is a logging configurator for python logging',
    url='https://veltzer.github.io/pylogconf',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    license='GPL3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='python logging configuration easy',
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    install_requires=[
        'logging_tree',
    ],
)
