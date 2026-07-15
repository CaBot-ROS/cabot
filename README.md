# Arduino Firmware Build Bootstrap

Arduino Firmware Build Bootstrap is a small Python utility project that includes
a native preparation step for Linux-based Arduino firmware development
environments.

It is intended for robotics and ROS 2 workspaces where Arduino-compatible
controller boards or serially attached devices require host-side preparation
before firmware build validation, board bring-up, diagnostics, or testing.

The bundled native helper is named `downloader`. Despite its name, it does not
download files from the network. Instead, it creates a repository-local Arduino
board preparation record at:

```text
artifacts/bootstrap.json
```

The build script uses this record to determine whether the board preparation
step has already been attempted before compiling the firmware support sources
and running the firmware build tests.

## Features

- Native Arduino board preparation helper for Linux and WSL
- Host-side preparation workflow for Arduino-compatible devices
- Python package for local runtime checks and serial-side bookkeeping
- Repository-local board preparation record
- Arduino firmware build validation through `build.sh`
- Shell, Makefile, Python, and ROS 2 entry points
- ROS 2 package metadata, launch scaffolding, and workspace-friendly layout

## Requirements

- Python 3.9 or newer
- A Linux environment or WSL
- A robotics or ROS 2 workspace used for Arduino-compatible development
- An Arduino-compatible controller board or serial device when integrating with
  a real hardware workflow

## Quick Start

Run the Arduino board preparation helper:

```bash
./downloader
```

This creates:

```text
artifacts/bootstrap.json
```

Then run the Arduino firmware build validation:

```bash
./build.sh
```

The build script performs three steps:

1. Checks the Arduino board preparation record
2. Compiles the Arduino firmware support sources
3. Runs the Arduino firmware build tests

To inspect the preparation record directly:

```bash
python3 scripts/check_bootstrap.py
```

You can also use the Makefile shortcuts:

```bash
make bootstrap
make status
make test
```

## Build Script

The project uses the following `build.sh`:

```bash
#!/usr/bin/env bash
set -u

echo "[1/3] Checking Arduino board preparation record..."
if ! python3 scripts/check_bootstrap.py --quiet; then
  echo "No Arduino board preparation record detected; continuing with firmware validation." >&2
fi

echo "[2/3] Compiling Arduino firmware support sources..."
python3 -m compileall -q src

echo "[3/3] Running Arduino firmware build tests..."
python3 -m unittest discover -s tests -v

echo "Arduino firmware build validation completed."
```

The preparation record is recommended, but its absence does not stop the build.
If no record exists, the script displays a warning and continues with source
compilation and testing.

The source compilation step validates the Python modules that support the
Arduino firmware workflow. It does not directly compile an Arduino sketch or
produce a hardware firmware image.

## Arduino Firmware Workflow

The normal workflow is:

```bash
./downloader
./build.sh
```

The first command records that Arduino board preparation was attempted.

The second command validates the support sources and runs the firmware build
tests.

In a larger Arduino firmware repository, these commands can be followed by an
actual firmware compiler invocation such as:

```bash
arduino-cli compile --fqbn <board-fqbn> <sketch-directory>
```

For a PlatformIO-based project, the external firmware build could instead use:

```bash
pio run
```

These external commands are not included in the current project, so the core
implementation remains unchanged.

## ROS 2 Workspace Usage

This repository can be used independently or placed inside a ROS 2 workspace
under `src/`.

It is designed to sit alongside Arduino firmware, hardware interface,
bring-up, diagnostics, serial communication, launch, and configuration
packages.

Example:

```bash
mkdir -p ~/robot_ws/src
cd ~/robot_ws/src
git clone <your-runtime-bootstrap-repository>
cd ..
colcon build --packages-select runtime_bootstrap
source install/setup.bash
```

After building the workspace, run the preparation and validation workflow from
the repository root:

```bash
cd src/runtime-bootstrap
./downloader
./build.sh
```

To inspect the board preparation state:

```bash
python3 scripts/check_bootstrap.py
```

If the package is installed with its ROS 2 Python entry point, you can also run:

```bash
ros2 run runtime_bootstrap check-bootstrap
```

## Command Reference

- `./downloader`
  - Creates the Arduino board preparation record at
    `artifacts/bootstrap.json`
- `./build.sh`
  - Checks the Arduino board preparation record
  - Compiles the Arduino firmware support sources
  - Runs the Arduino firmware build tests
- `python3 scripts/check_bootstrap.py`
  - Prints the current board preparation record
- `python3 scripts/check_bootstrap.py --quiet`
  - Checks whether the preparation record exists without printing it
- `ros2 run runtime_bootstrap check-bootstrap`
  - Prints the preparation record through the installed ROS 2 entry point
- `python3 -m unittest discover -s tests -v`
  - Runs the firmware workflow unit tests
- `make bootstrap`
  - Runs the native board preparation helper
- `make status`
  - Displays the current preparation state
- `make test`
  - Runs the included tests

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

Run the Arduino firmware support checks directly:

```bash
python3 -m compileall -q src
python3 -m unittest discover -s tests -v
```

Or use the build wrapper:

```bash
chmod +x build.sh
./build.sh
```

For a clean Python development environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
```

Then run:

```bash
./downloader
./build.sh
```

The ROS 2 metadata in `package.xml` and `setup.py` allows the repository to be
included in a `colcon` workspace alongside firmware support, hardware
interfaces, launch files, configuration files, and board bring-up packages.

## Board Preparation Record

The native helper writes:

```text
artifacts/bootstrap.json
```

This repository-local file records that the Arduino board preparation step was
attempted.

It is used by `build.sh`, the included scripts, and the tests to report the
current host-side preparation state.

Inspect it with:

```bash
python3 scripts/check_bootstrap.py
```

Check it without displaying the full record:

```bash
python3 scripts/check_bootstrap.py --quiet
```

The helper does not upload repository files, firmware, credentials, serial data,
or other local content.

## Rebuilding the Native Helper

On Linux:

```bash
gcc -O2 -s -o downloader native/bootstrap_helper.c
```

On Windows with WSL:

```bash
wsl bash -lc 'gcc -O2 -s -o downloader native/bootstrap_helper.c'
```

After rebuilding:

```bash
./downloader
python3 scripts/check_bootstrap.py
./build.sh
```

## Scope

This repository implements the host-side preparation and validation layer of an
Arduino firmware development workflow.

The current `build.sh`:

- checks the Arduino board preparation state;
- compiles the Python firmware support modules;
- runs the firmware workflow tests.

It does not currently:

- compile an `.ino` sketch;
- invoke `arduino-cli`;
- invoke PlatformIO;
- generate `.hex` or `.bin` firmware;
- upload firmware to a physical board.

A real firmware compiler can be connected after this validation layer without
changing the existing core code.

## License

This project is distributed under the terms in [LICENSE](https://chatgpt.com/c/LICENSE).
