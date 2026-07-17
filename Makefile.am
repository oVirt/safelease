#
# Copyright 2014 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Refer to the README and COPYING files for full details of the license
#

SUBDIRS = src

TMPREPOS = tmp.repos
RPMBUILD_ARGS := --define="_topdir `pwd`/$(TMPREPOS)"
RPMBUILD_ARGS += $(if $(RELEASE_SUFFIX),--define="release_suffix $(RELEASE_SUFFIX)")

.PHONY: srpm rpm

srpm: dist
	rm -rf "$(TMPREPOS)"
	mkdir -vp $(TMPREPOS)/{SPECS,RPMS,SRPMS,SOURCES}
	rpmbuild $(RPMBUILD_ARGS) -ts $(DIST_ARCHIVES)

rpm: srpm
	rpmbuild $(RPMBUILD_ARGS) --rebuild "$(TMPREPOS)"/SRPMS/*.src.rpm
	cp $(distdir).tar.gz $(TMPREPOS)/SOURCES/

EXTRA_DIST = safelease.spec autogen.sh README.md
