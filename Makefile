DESTDIR?=/usr/local/bin
VERSION=1.0
PACKAGE_DIR=safelease-$(VERSION)

safelease:
	gcc -o safelease safelease.c

all: safelease

clean:
	rm -f safelease
	rm -fr $(PACKAGE_DIR)
	rm -fr dist

dist: safelease
	mkdir -p dist
	mkdir -p $(PACKAGE_DIR)
	cp safelease Makefile safelease.spec $(PACKAGE_DIR)
	tar -zcf dist/$(PACKAGE_DIR).tar.gz $(PACKAGE_DIR)

install: safelease
	mkdir -p $(DESTDIR)
	cp safelease $(DESTDIR)

rpm: dist
	rpmbuild -ta dist/$(PACKAGE_DIR).tar.gz
