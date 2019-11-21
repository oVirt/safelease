#!/bin/bash -xe

REBUILD_TARBALL=1


# remove any previous artifacts
rm -rf output
rm -f ./*tar.gz

if [[ $REBUILD_TARBALL == 1 ]] ; then
    spectool -g ./safelease.spec
    rpmbuild \
        -D "_sourcedir $PWD" \
        -D "_srcrpmdir $PWD/output" \
        -D "_topmdir $PWD/rpmbuild" \
        -bs ./safelease.spec
 
    # install any build requirements
    dnf builddep output/*src.rpm

    # create the rpms
    rpmbuild \
        -D "_rpmdir $PWD/output" \
        -D "_topmdir $PWD/rpmbuild" \
        --rebuild output/*.src.rpm
else
    SUFFIX=".$(date -u +%Y%m%d%H%M%S).git$(git rev-parse --short HEAD)"

    autoreconf -ivf
    ./configure

    # Get the tarball
    make dist

    # create the src.rpm
    rpmbuild \
        -D "_srcrpmdir $PWD/output" \
        -D "_topmdir $PWD/rpmbuild" \
        -D "release_suffix ${SUFFIX}" \
        -ts ./*.gz

    # install any build requirements
    dnf builddep output/*src.rpm

    # create the rpms
    rpmbuild \
        -D "_rpmdir $PWD/output" \
        -D "_topmdir $PWD/rpmbuild" \
        -D "release_suffix ${SUFFIX}" \
        --rebuild output/*.src.rpm
fi


# Store any relevant artifacts in exported-artifacts for the ci system to
# archive
[[ -d exported-artifacts ]] || mkdir -p exported-artifacts
find output -iname \*rpm -exec mv "{}" exported-artifacts/ \;
mv ./*tar.gz exported-artifacts/
