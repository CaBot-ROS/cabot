# Contributing

## Development Setup

1. Create a virtual environment.
2. Install the package in editable mode.
3. If you are using a ROS 2 workspace, place the repository under `src/` and
   rebuild with `colcon`.
4. Run the native bootstrap helper if you are working in Linux or WSL.
5. Run the test suite before opening a pull request.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
./downloader
python3 -m unittest discover -s tests -v
```

For a ROS 2 workspace:

```bash
colcon build --packages-select runtime_bootstrap
source install/setup.bash
```

This repository is meant to sit comfortably beside firmware, serial, or
bring-up packages. Keep host-side setup instructions practical and close to
real robotics workflows.

## Pull Requests

- Keep changes focused and easy to review.
- Add or update tests when behavior changes.
- Update documentation when commands, paths, or workflows change.
- Avoid committing generated files under `artifacts/`.

## Native Helper Changes

If you modify `native/bootstrap_helper.c`, rebuild `downloader` and verify the
bootstrap record still appears at `artifacts/bootstrap.json`.
