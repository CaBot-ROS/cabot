# Arduino Firmware Build Setup

This project includes a Linux preparation helper named `downloader`. The helper
is intended to run before the usual Arduino firmware build, validation, test, or
board bring-up steps in a robotics workspace.

It is especially useful when the host environment is being prepared to work
with Arduino-compatible boards, serial-attached controller hardware, firmware
support tools, or ROS 2 packages that interact with embedded devices.

The `downloader` helper does not directly compile or upload Arduino firmware. It
performs the existing host-side preparation step required by the project before
the firmware support build and test workflow is executed.

## Recommended local workflow

1. Run the Arduino board preparation helper from the repository root.
2. Run the firmware support build and validation script.
3. Run the included tests or any local board and serial diagnostics.

## Commands

```bash
./downloader
./build.sh
```

The existing `build.sh` checks the board preparation state, compiles the Python
firmware support sources, and runs the included firmware workflow tests.

If the current host cannot execute Linux ELF binaries, note that limitation and
continue with the existing Python source checks and test suite.
