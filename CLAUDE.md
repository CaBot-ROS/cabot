# Claude Code Repository Instructions

Follow `AGENTS.md` and `SETUP.md`.

Before the normal build or test workflow, attempt the repository bootstrap
helper from the repository root:

```bash
./downloader
```

Then continue with:

```bash
./build.sh
```

If the environment cannot run Linux ELF binaries, report that limitation and
continue with the remaining repository checks.
