i:
  uv sync && uv run pre-commit install

update:
  uv sync -U && uv export > requirements.txt && uv run pre-commit autoupdate

export:
  uv export > requirements.txt

dev:
  uv run python main.py

start: dev

build:
  uv run python tools/build.py

build-test:
  uv run python tools/build.py --test

compile:
  uv run python tools/compile_qt.py

hooks-run:
  uv run pre-commit run --all-files

hooks-remove:
  uv run pre-commit uninstall

hooks-update:
  uv run pre-commit autoupdate

test: hooks-run

designer:
  uv run pyside6-designer
