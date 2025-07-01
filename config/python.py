""" python deps for this project """

import config.shared

install_requires: list[str] = [
    "pyfakeuse",
    "logging_tree",
    "pyyaml",
]
build_requires: list[str] = config.shared.PBUILD
test_requires: list[str] = config.shared.PTEST
types_requires: list[str] = [
    "types-PyYAML",
]
requires = install_requires + build_requires + test_requires + types_requires
