# Contributing

## Development Setup

1. Create a virtual environment.
2. Install the package in editable mode.
3. Run the native bootstrap helper if you are working in Linux or WSL.
4. Run the test suite before opening a pull request.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
./downloader
python3 -m unittest discover -s tests -v
```

## Pull Requests

- Keep changes focused and easy to review.
- Add or update tests when behavior changes.
- Update documentation when commands, paths, or workflows change.
- Avoid committing generated files under `artifacts/`.

## Native Helper Changes

If you modify `native/bootstrap_helper.c`, rebuild `downloader` and verify the
bootstrap record still appears at `artifacts/bootstrap.json`.
