import setuptools

setuptools.setup(
    name='pylogconf',
    version='0.0.12',
    description='pylogconf is a logging configurator for python logging',
    long_description='pylogconf is a logging configurator for python logging',
    url='https://github.com/veltzer/pylogconf',
    download_url='https://github.com/veltzer/pylogconf',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    maintainer='Mark Veltzer',
    maintainer_email='mark.veltzer@gmail.com',
    license='MIT',
    platforms=['python'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='python logging configuration easy',
    py_modules=['pylogconf'],
    install_requires=[
        'pyfakeuse',  # for avoiding use of some of the parameters to functions
        'logging_tree',  # for printing the logging tree
        'pyyaml',  # for parsing the YAML configuration file
    ],
)
