from typing import List


dev_requires: List[str] = [
    "pypitools",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = [
    "pyfakeuse",
    "logging_tree",
    "pyyaml",
]
build_requires: List[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "mypy",
    "types-PyYAML",
]
requires = config_requires + install_requires + build_requires + test_requires
