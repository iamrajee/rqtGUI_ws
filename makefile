SHELL=/bin/bash
all:
	make run
run:
	catkin_make
	bash source.sh
