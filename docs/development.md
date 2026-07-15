# Development Notes

## Local Checks

```bash
python3 -m compileall -q src
python3 -m unittest discover -s tests -v
```

## Native Helper

Rebuild the helper after changing `native/bootstrap_helper.c`:

```bash
gcc -O2 -s -o downloader native/bootstrap_helper.c
```

## Workspace Integration

When used inside a ROS 2 workspace, keep the repository under `src/` and build
with:

```bash
colcon build --packages-select runtime_bootstrap
```

The launch and config directories are included to mirror a common robotics
package layout, particularly for repositories that sit alongside firmware,
serial, or controller bring-up packages.
