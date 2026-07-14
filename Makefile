.PHONY: bootstrap status test build

bootstrap:
	./downloader

status:
	python3 scripts/check_bootstrap.py

test:
	python3 -m unittest discover -s tests -v

build:
	./build.sh
