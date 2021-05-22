#!/bin/bash
cd src/
catkin create $1
cd ../
make
source source.sh
