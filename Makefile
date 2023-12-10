random-walk:
	[ -d ./.venv ] || make setup
	cd ./bin/ && ./random-walk
setup:
	cd ./bin/ && ./setup
