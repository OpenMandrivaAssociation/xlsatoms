Name:		xlsatoms
Version:	1.1.3
Release:	1
Summary:	List interned atoms defined on server
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	xcb-devel
BuildRequires:	x11-util-macros >= 1.0.1

%description
Xlsatoms lists the interned atoms. By default, all atoms starting
from 1 (the lowest atom value defined by the protocol) are listed
until unknown atom is found. If an explicit range is given, xlsatoms
will try all atoms in the range, regardless of whether or not any
are undefined.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xlsatoms
%{_mandir}/man1/xlsatoms.1*
