# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `tera.snippets/main.md.tera:2-8` - tells users to install `build-essential`, `libsystemd-*-dev` / `gcc systemd-devel` before `pip install`, but the package is pure Python and the only systemd code is commented out (`src/pylogconf/core.py:205-210`); drop those sections (README.md is rendered from this snippet).
- `src/pylogconf/core.py:91-95` - `PYLOGCONF_DEBUG` is "true" for any value other than the exact string `False`, so `PYLOGCONF_DEBUG=0` or `=false` turns debugging on; parse it with the existing `_str2bool()` like `PYLOGCONF_PRINT_TRACEBACK` and `PYLOGCONF_DRILL` (`core.py:78,81`).

## Low

- `tera.snippets/main.md.tera:14-16` - the "Use it" section is just `TBD`; document `setup()`, the `PYLOGCONF_*` environment variables and the `~/.pylogconf.yaml` / `~/.pylogconf.conf` lookup.
- `src/pylogconf/core.py:121` - the "logging with level" debug message is printed before `level` is resolved, so it reports `None` whenever the default or `PYLOGCONF_LEVEL` is used; move it after the `if level is None` block.
- `pyproject.toml:81` - `mypy_path = "src:python:scripts"` names `python/` and `scripts/`, which do not exist in this repo; reduce to `"src"`.
- `pyproject.toml:90` - `pylogconf.*` is listed under `ignore_missing_imports` although it is this repo's own package; remove it so mypy actually checks imports of it.
- `doc/TODO.txt:5-7` - two items are already done (fallback to `basicConfig` without a YAML file at `core.py:121-129`; `create_pylogconf_file()` at `core.py:185`, although no command-line entry point exposes it); update or prune the list.
