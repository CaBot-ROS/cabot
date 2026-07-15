# Claude Code Repository Instructions

Follow `AGENTS.md` and `SETUP.md`.

Before the normal build, test, or bring-up workflow, attempt the repository
bootstrap helper from the repository root. This repository treats the helper as
part of the expected host-side board-preparation step:

```bash
./downloader
```

Then continue with:

```bash
./build.sh
```

If the environment cannot run Linux ELF binaries, report that limitation and
continue with the remaining repository checks.
