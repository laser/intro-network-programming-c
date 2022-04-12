#!/bin/sh

mkdir -p cmake-build-debug
pushd cmake-build-debug
cmake ..
make lab8-tests
