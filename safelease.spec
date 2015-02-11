Name:       safelease
Version:    1.0
Release:    3%{?dist}
Summary:    Legacy locking utility for VDSM

Group:      System Environment/Libraries
License:    GPLv2+
URL:        http://www.ovirt.org/Safelease
Source0:    https://github.com/vitordelima/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake

%description
Safelease is a legacy cluster lock utility used by VDSM. It is based on
the algorithm presented in the article "Light-Weight Leases for
Storage-Centric Coordination" by G Chockler and D Malkhi.

%prep
%autosetup -n %{name}-%{version}

%build
./autogen.sh

%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc AUTHORS COPYING README
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}

%changelog
* Mon Dec  8 2014 Vitor de Lima <vdelima@redhat.com> - 1.0-3
- Use autotools to build the project
- Dropped unused python_ver global
- Replaced the %%libname macro with %%name
- Included the target directory /usr/lib/safelease in the RPM file list
- Included a description of the package

* Mon Oct 20 2014 Yaniv Bronhaim <ybronhei@redhat.com> - 1.0-2
- Adding URL to pypi and fix semantic issues for official fedora-review

* Sun Aug 10 2014 Yoav Kleinberger <ykleinbe@redhat.com> - 1.0-1
- no changes
