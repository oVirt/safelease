# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>. */

DESTDIR = /usr/local/bin
VERSION = 1.0
PACKAGE_DIR = safelease-$(VERSION)
CFLAGS = -g -O2 -Wall
INSTALL = $(shell which install)
FILES = safelease Makefile safelease.spec 

safelease:

check:

clean:
	rm -f safelease
	rm -fr $(PACKAGE_DIR)
	rm -fr dist

dist: safelease
	mkdir -p dist
	mkdir -p $(PACKAGE_DIR)
	cp $(FILES) $(PACKAGE_DIR)
	tar -zcf dist/$(PACKAGE_DIR).tar.gz $(PACKAGE_DIR)

install: safelease
	$(INSTALL) -d $(DESTDIR)
	$(INSTALL) -c -m 755 safelease $(DESTDIR)

rpm: dist
	rpmbuild -ta dist/$(PACKAGE_DIR).tar.gz
