DESTDIR?=/usr/local/bin
VERSION=1.0

safelease:
	gcc -o safelease safelease.c

all: safelease

dist: safelease
	mkdir -p dist
	rm -fr safelease-$(VERSION)
	mkdir -p safelease-$(VERSION)
	cp safelease Makefile safelease.spec safelease-$(VERSION)
	tar -zcf dist/safelease-$(VERSION).tar.gz safelease-$(VERSION)

install: safelease
	mkdir -p $(DESTDIR)
	cp safelease $(DESTDIR)

rpm: dist
	rpmbuild -ta dist/safelease-$(VERSION).tar.gz		
