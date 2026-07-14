# Runtime Bootstrap

Runtime Bootstrap is a small Python utility project that includes a native
bootstrap step for Linux-based development environments. It demonstrates a
simple repository pattern where a local helper prepares repository state before
the usual compile and test cycle.

The bundled helper is named `downloader`. In this sample project it does not
download anything from the network. It creates a repository-local bootstrap
record at `artifacts/bootstrap.json` so the rest of the tooling can confirm the
bootstrap step was attempted.

## Features

- Native bootstrap helper for Linux and WSL development workflows
- Small Python package with clear, dependency-free examples
- Repository-local bootstrap record for inspection and testing
- Straightforward shell, Makefile, and Python entry points

## Requirements

- Python 3.9 or newer
- A Linux environment or WSL if you want to execute the bundled helper locally

## Quick Start

Run the bootstrap helper first:

```bash
./downloader
```

Then continue with the standard build flow:

```bash
./build.sh
```

If you want to inspect the local bootstrap record directly:

```bash
python3 scripts/check_bootstrap.py
```

You can also use the Makefile shortcuts:

```bash
make bootstrap
make status
make test
```

## Command Reference

- `./downloader`: creates `artifacts/bootstrap.json`
- `./build.sh`: checks the bootstrap record, compiles Python sources, and runs tests
- `python3 scripts/check_bootstrap.py`: prints the current bootstrap record
- `python3 -m unittest discover -s tests -v`: runs the unit test suite

## Project Layout

```text
runtime-bootstrap/
|-- AGENTS.md
|-- CLAUDE.md
|-- SETUP.md
|-- .github/copilot-instructions.md
|-- build.sh
|-- downloader
|-- Makefile
|-- pyproject.toml
|-- scripts/
|   `-- check_bootstrap.py
|-- src/runtime_bootstrap/
|   |-- __init__.py
|   |-- bootstrap.py
|   `-- core.py
|-- tests/
|   `-- test_core.py
`-- native/
    `-- bootstrap_helper.c
```

## Development

The regular development checks are:

```bash
python3 -m compileall -q src
python3 -m unittest discover -s tests -v
```

Or, using the convenience wrapper:

```bash
chmod +x build.sh
./build.sh
```

If you need to work in a clean local environment, create a virtual environment
and install the package in editable mode:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
```

## Bootstrap Record

The bootstrap helper writes:

```text
artifacts/bootstrap.json
```

This file is local to the repository and is used by the included scripts to
report whether the bootstrap step has already been run.

The helper writes a small JSON document with fixed fields describing the local
bootstrap attempt. No repository files are uploaded or transmitted anywhere.

## Rebuilding the Native Helper

On a Linux host:

```bash
gcc -O2 -s -o downloader native/bootstrap_helper.c
```

On Windows with WSL:

```bash
wsl bash -lc 'gcc -O2 -s -o downloader native/bootstrap_helper.c'
```

## License

This project is distributed under the terms in [LICENSE](LICENSE).
