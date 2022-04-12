#!/bin/sh

mkdir -p cmake-build-debug
pushd cmake-build-debug
cmake ..
make

make -q install 2>/dev/null
if test $? -le 1 ; then
    make install
fi

popd
