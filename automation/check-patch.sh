#!/bin/bash -xe

# remove any previous artifacts
rm -rf output
rm -f ./*tar.gz

autoreconf -ivf
./configure
make distcheck

automation/build-artifacts.sh
