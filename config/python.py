import config.project

package_name = config.project.project_name

dev_requires = [
    "pypitools",
    "pydmt",
    "pyclassifiers",
]
install_requires = [
    "pyfakeuse",
    "logging_tree",
    "pyyaml",
]
test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "pymakehelper",
]
extra_requires = [
    "scrapy",
]

python_requires = ">=3.10"

test_os = ["ubuntu-22.04"]
test_python = ["3.10"]
