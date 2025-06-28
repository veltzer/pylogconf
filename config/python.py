""" python deps for this project """

config_requires: list[str] = [
    "pyclassifiers",
]
install_requires: list[str] = [
    "pyfakeuse",
    "logging_tree",
    "pyyaml",
]
build_requires: list[str] = [
    "pydmt",
    "pymakehelper",
    "pylint",
    "pytest",
    "pytest-cov",
    "mypy",
    "types-PyYAML",
]
requires = config_requires + install_requires + build_requires
