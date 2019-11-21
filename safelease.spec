Name:       safelease
Version:    1.0.1
Release:    2%{?release_suffix}%{?dist}
Summary:    Legacy locking utility for VDSM

License:    GPLv2+
URL:        https://www.ovirt.org/develop/developer-guide/vdsm/safelease.html
Source0:    http://resources.ovirt.org/pub/src/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: autoconf
BuildRequires: automake

%description
Safelease is a legacy cluster lock utility used by VDSM. It is based on
the algorithm presented in the article "Light-Weight Leases for
Storage-Centric Coordination" by G Chockler and D Malkhi.

%prep
%autosetup -n %{name}-%{version}

%build
./autogen.sh --system

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
* Thu Nov 21 2019 Sandro Bonazzola <sbonazzo@redhat.com> - 1.0.1-2
- Rebuild for el8

* Fri May 03 2019 Sandro Bonazzola <sbonazzo@redhat.com> - 1.0.1-1
- Rebase on upstream 1.0.1
- Resolves: BZ#1696313

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 22 2016 Yaniv Bronhaim <ybronhei@redhat.com> - 1.0-7
- Adding virt-v2v requirement - another hack for vdsm

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
