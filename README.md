# Safe Lease

[![Copr build status](https://copr.fedorainfracloud.org/coprs/ovirt/ovirt-master-snapshot/package/safelease/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/ovirt/ovirt-master-snapshot/package/safelease/)

Welcome to the Safe Lease source repository. This repository is hosted on [GitHub:ovirt-safelease](https://github.com/oVirt/safelease).

Safelease is a legacy cluster lock utility used by [VDSM](https://github.com/oVirt/vdsm).
It is based on the algorithm presented in the article
["Light-Weight Leases for Storage-Centric Coordination" by G. Chockler and D. Malkhi](https://dspace.mit.edu/handle/1721.1/30464).

## How to contribute

All contributions are welcome - patches, bug reports, and documentation issues.

### Submitting patches

Please submit patches to [GitHub:safelease](https://github.com/oVirt/safelease). If you are not familiar with the process, you can read about [collaborating with pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests) on the GitHub website.

### Found a bug or documentation issue?

To submit a bug or suggest an enhancement for oVirt Release please use [oVirt Bugzilla for safelease component within ovirt-distribution product](https://bugzilla.redhat.com/enter_bug.cgi?product=ovirt-distribution).

If you don't have a Bugzilla account, you can still report [issues](https://github.com/oVirt/safelease/issues). If you find a documentation issue on the oVirt website, please navigate to the page footer and click "Report an issue on GitHub".

## Still need help?

If you have any other questions or suggestions, you can join and contact us on the [oVirt Users forum / mailing list](https://lists.ovirt.org/admin/lists/users.ovirt.org/).


## Installation

Safelease can be used by following the standard autotools installation
process, documented in the INSTALL file. As a quick
start you can do

```bash
   ./configure --prefix=/usr --sysconfdir=/etc \
        --localstatedir=/var --libdir=/usr/lib
   make
   sudo make install
```

## Packaging

The `safelease.spec` file demonstrates how to distribute safelease as an RPM package.

'make rpm' generates rpm file for installation.


## Licensing

safelease is provided under the terms of the GNU General Public License,
version 2 or later. Please see the COPYING file for complete GPLv2+
license terms.

In addition, as a special exception, Red Hat, Inc. and its affiliates
give you permission to distribute this program, or a work based on it,
linked or combined with the OpenSSL project's OpenSSL library (or a
modified version of that library) to the extent that the library, or
modified version, is covered by the terms of the OpenSSL or SSLeay
licenses.  Corresponding source code for the object code form of such
a combination shall include source code for the parts of OpenSSL
contained in the combination.

If you modify this program, you may extend this exception to your
version, but you are not obligated to do so.  If you do not wish to do
so, delete this exception statement from your version.
