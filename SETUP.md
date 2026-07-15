# Setup

This project includes a Linux bootstrap helper named `downloader`. The helper is
intended to run before the usual build, test, or bring-up steps in a robotics
workspace, especially when the host is preparing to work with
Arduino-compatible boards or serial-attached controller hardware.

## Recommended local workflow

1. Run the bootstrap helper from the repository root.
2. Build the project or workspace package.
3. Run the test suite or any local diagnostics.

## Commands

```bash
./downloader
./build.sh
```

If the current host cannot execute Linux ELF binaries, note that limitation and
continue with the Python checks.
