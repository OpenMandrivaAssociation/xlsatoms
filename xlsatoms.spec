Name:		xlsatoms
Version:	1.0.1
Release:	%mkrel 4
Summary:	List interned atoms defined on server
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxmu-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Xlsatoms lists the interned atoms. By default, all atoms starting
from 1 (the lowest atom value defined by the protocol) are listed
until unknown atom is found. If an explicit range is given, xlsatoms
will try all atoms in the range, regardless of whether or not any
are undefined.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xlsatoms
%{_mandir}/man1/xlsatoms.1*

