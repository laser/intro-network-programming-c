#!/bin/sh

mkdir -p cmake-build-debug
pushd cmake-build-debug
cmake ..
make lab1-tests
