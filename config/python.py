import config.project

package_name = config.project.project_name

console_scripts = [
]

setup_requires = [
]

test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "pymakehelper",
]

install_requires = [
    'pyfakeuse',
    'logging_tree',
    'pyyaml',
  
]

dev_requires = [
    'pypitools',
    'pydmt',
    'pyclassifiers',
    'scrapy',
]

python_requires = ">=3.6"

extras_require = {
}
