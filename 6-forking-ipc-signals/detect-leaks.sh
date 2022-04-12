#!/bin/sh

target_dir=$(pwd | sed -e "s;.*\/;;")

pushd ..

/bin/bash ./detect-leaks.sh "${target_dir}"
