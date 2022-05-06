import config.project

package_name = config.project.project_name

test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "pymakehelper",
]
install_requires = [
    "pyfakeuse",
    "logging_tree",
    "pyyaml",
]
dev_requires = [
    "pypitools",
    "pydmt",
    "pyclassifiers",
    "scrapy",
]

python_requires = ">=3.9"
test_os = ["ubuntu-20.04"]
test_python = ["3.9"]
