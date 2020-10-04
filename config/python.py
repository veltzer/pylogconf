import config.project

package_name = config.project.project_name

console_scripts = [
]

setup_requires = [
]

test_requires = [
    "pylint",  # to check for lint errors
    "pytest",  # for testing
    "pytest-cov",  # for testing
    "flake8",  # for linting
    "pymakehelper",  # for make
]

install_requires = [
    'pyfakeuse',  # for avoiding use of some of the parameters to functions
    'logging_tree',  # for printing the logging tree
    'pyyaml',  # for parsing the YAML configuration file
    # 'systemd',  # for systemd interface
]

dev_requires = [
    'pypitools',  # for upload and registration
    'pydmt',  # for building
    'pyclassifiers',  # for specifying classifications
    'scrapy',  # for developing the scrapy support
]

python_requires = ">=3.6"

extras_require = {
    # ':python_version == "2.7"': ['futures'],  # for python2.7 backport of concurrent.futures
}
