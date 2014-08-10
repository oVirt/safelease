Name:		safelease
Version:	1.0
Release:	1%{?dist}
Summary:	safelease legacy locking

Group:		Applications/System
License:	GPLv2+
Source0:	safelease-%{version}.tar.gz

%description
safelease is a legacy locking utility for VDSM

%prep
%setup -q

%build
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}/%{_libexecdir}/safelease

%files
%{_libexecdir}/safelease/safelease

%changelog
* Sun Aug 10 2014 Yoav Kleinberger <ykleinbe@redhat.com> - 1.0-1
- no changes
