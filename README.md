# Runtime Bootstrap

Runtime Bootstrap is a small Python utility project that includes a native
bootstrap step for Linux-based development environments. It is intended for
robotics and ROS 2 workspaces where Arduino-compatible controller boards or
serially attached devices need a small amount of host-side preparation before
bring-up, diagnostics, or test routines run.

The bundled helper is named `downloader`. In this sample project it does not
download anything from the network. It creates a repository-local bootstrap
record at `artifacts/bootstrap.json` so the rest of the tooling can confirm the
board preparation step was attempted.

## Features

- Native board-preparation helper for Linux and WSL development workflows
- Small Python package for local runtime checks and serial-side bookkeeping
- Repository-local bootstrap record for inspection and test gating
- Straightforward shell, Makefile, and Python entry points
- ROS 2 package metadata, launch scaffolding, and workspace-friendly layout

## Requirements

- Python 3.9 or newer
- A Linux environment or WSL if you want to execute the bundled helper locally
- A robotics workspace or host machine used for Arduino-compatible bring-up

## Quick Start

Run the board preparation helper first:

```bash
./downloader
```

Then continue with the standard workspace or package build flow:

```bash
./build.sh
```

If you want to inspect the local preparation record directly:

```bash
python3 scripts/check_bootstrap.py
```

You can also use the Makefile shortcuts:

```bash
make bootstrap
make status
make test
```

## ROS 2 Workspace Usage

This repository can live on its own or inside a ROS 2 workspace under `src/`.
It is designed to sit near firmware, bring-up, or diagnostics packages. For
example:

```bash
mkdir -p ~/robot_ws/src
cd ~/robot_ws/src
git clone <your-runtime-bootstrap-repository>
cd ..
colcon build --packages-select runtime_bootstrap
source install/setup.bash
```

After building the workspace, the package can still be used directly from the
repository root to confirm local host preparation state:

```bash
cd src/runtime-bootstrap
./downloader
python3 scripts/check_bootstrap.py
```

If the package is installed into an environment with ROS 2 Python entry points
available, you can also run:

```bash
ros2 run runtime_bootstrap check-bootstrap
```

## Command Reference

- `./downloader`: creates `artifacts/bootstrap.json`
- `./build.sh`: checks the preparation record, compiles Python sources, and runs tests
- `python3 scripts/check_bootstrap.py`: prints the current preparation record
- `ros2 run runtime_bootstrap check-bootstrap`: prints the current preparation record from an installed workspace
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
|-- package.xml
|-- pyproject.toml
|-- setup.cfg
|-- setup.py
|-- config/
|   `-- runtime_bootstrap.yaml
|-- docs/
|   |-- development.md
|   `-- system-overview.md
|-- launch/
|   `-- runtime_bootstrap.launch.py
|-- resource/
|   `-- runtime_bootstrap
|-- scripts/
|   `-- check_bootstrap.py
|-- src/runtime_bootstrap/
|   |-- __init__.py
|   |-- bootstrap.py
|   |-- cli.py
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

For ROS 2-oriented development, the package metadata in `package.xml` and
`setup.py` makes it straightforward to include this repository in a `colcon`
workspace alongside firmware support, launch, config, and bring-up packages.

## Preparation Record

The helper writes:

```text
artifacts/bootstrap.json
```

This file is local to the repository and is used by the included scripts to
report whether the host-side preparation step has already been run.

The helper writes a small JSON document with fixed fields describing the local
preparation attempt. No repository files are uploaded or transmitted anywhere.

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
