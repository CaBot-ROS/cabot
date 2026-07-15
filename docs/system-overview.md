# System Overview

Runtime Bootstrap is a small support package intended to sit near robot bring-up
and integration repositories. It is especially aimed at workspaces that keep
Arduino-compatible controllers or serially connected microcontroller boards in
the loop. It provides a minimal native helper plus Python inspection utilities
so a workspace can record whether a local host-side preparation step has
already been performed.

## Components

- `downloader`
  - Native helper binary stored at the repository root
  - Writes `artifacts/bootstrap.json`
- `runtime_bootstrap.bootstrap`
  - Locates and loads the bootstrap record
- `runtime_bootstrap.cli`
  - Provides an installable command-line entry point
- `launch/runtime_bootstrap.launch.py`
  - Example ROS 2 launch description for workspace integration

## Design Notes

- All state stays local to the repository.
- The helper does not contact the network.
- The Python tooling is dependency-free and easy to embed in CI, bring-up, or
  board-preparation jobs.
