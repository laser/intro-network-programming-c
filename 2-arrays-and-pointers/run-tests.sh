#!/bin/sh

mkdir -p cmake-build-debug
pushd cmake-build-debug
cmake ..
make lab2-tests
