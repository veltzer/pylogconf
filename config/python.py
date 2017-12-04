import config.project

package_name = config.project.project_name

console_scripts = [
]

setup_requires = [
]

install_requires = [
    'pyfakeuse',  # for avoiding use of some of the parameters to functions
    'logging_tree',  # for printing the logging tree
    'pyyaml',  # for parsing the YAML configuration file
]

dev_requires = [
    'pypitools',  # for upload and registration
    'pydmt',  # for building
    'pyclassifiers',  # for specifying classifications
]

python_requires = ">=3"
