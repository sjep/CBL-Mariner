Summary:	cifs client utils
Name:		cifs-utils
Version:	6.8
Release:	4%{?dist}
License:	GPLv3
URL:		http://wiki.samba.org/index.php/LinuxCIFS_utils
Group:		Applications/Nfs-utils-client
Source0:        https://ftp.samba.org/pub/linux-cifs/cifs-utils/cifs-utils-%{version}.tar.bz2

Patch0:         CVE-2020-14342.patch

Vendor:         Microsoft Corporation
Distribution:   Mariner
BuildRequires:  libcap-ng-devel
BuildRequires:  libtalloc-devel
Requires:       libcap-ng

%description
Cifs-utils, a package of utilities for doing and managing mounts of the Linux CIFS filesystem.


%package devel
Summary:    The libraries and header files needed for Cifs-Utils development.
Group:      Development/Libraries
Requires:   cifs-utils = %{version}-%{release}

%description devel
Provides header files needed for Cifs-Utils development.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fiv &&./configure --prefix=%{_prefix}
make

%install
make DESTDIR=%{buildroot} install

%check
make %{?_smp_mflags} check

%files
%defattr(-,root,root)
%license COPYING
/sbin/mount.cifs

%files devel
%defattr(-,root,root)
%{_includedir}/cifsidmap.h

%changelog
*   Wed Sep 30 2020 Henry Beberman <henry.beberman@microsoft.com> - 6.8-4
-   Add patch for CVE-2020-14342
*   Sat May 09 00:20:52 PST 2020 Nick Samson <nisamson@microsoft.com> - 6.8-3
-   Added %%license line automatically
*   Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 6.8-2
-   Initial CBL-Mariner import from Photon (license: Apache2).
*       Fri Sep 07 2017 Ajay Kaher <akaher@vmware.com> 6.8-1
-       Upgraded to version 6.8
*       Thu Apr 06 2017 Anish Swaminathan <anishs@vmware.com> 6.7-1
-       Upgraded to version 6.7
*	Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 6.4-2
-	GA - Bump release of all rpms
*	Mon Jan 25 2016 Divya Thaluru <dthaluru@vmware.com> 6.4-1
-	Initial build.	First version
