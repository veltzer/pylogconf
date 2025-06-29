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
    "hatch",
    "pydmt",
    "pymakehelper",
    "pycmdtools",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "mypy",
    "ruff",
    # types
    "types-PyYAML",
]
requires = config_requires + install_requires + build_requires + test_requires
