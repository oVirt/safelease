Name:       safelease
Version:    1.0
Release:    6%{?dist}
Summary:    Legacy locking utility for VDSM

Group:      System Environment/Libraries
License:    GPLv2+
URL:        http://www.ovirt.org/Safelease
Source0:    https://bronhaim.fedorapeople.org/%{name}-%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake

##
# The following requirements are necessary for VDSM to avoid
# platform dependencies. Those are not required by safelease code and should
# remove once vdsm will be able to provide those requirements otherwise.

# Numactl is not available on s390[x] and ARM
%ifnarch s390 s390x %{arm}
Requires: numactl
%endif

%ifarch x86_64
Requires: python-dmidecode
Requires: dmidecode
%endif

## hack end.

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
%doc AUTHORS README
%{!?_licensedir:%global license %%doc}
%license COPYING
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}

%changelog
* Thu Dec 24 2015 Yaniv Bronhaim <ybronhei@redhat.com> - 1.0-6
- Adding target for rpm and srpm to make file to ease build process

* Sun May 17 2015 Yaniv Bronhaim <ybronhei@redhat.com> - 1.0-5
- Adding vdsm hack to require platform depended packages which vdsm needs

* Sun Apr 12 2015 Yaniv Bronhaim <ybronhei@redhat.com> - 1.0-4
- Adding %%license macro for COPYING

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
