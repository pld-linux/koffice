%define		REV	20000415
Summary:	KOffice - powerful office suite for KDE
Summary(pl):	KOffice - potê¿ny pakiet biurowy dla KDE
Name:		koffice
Version:	2.0pre_%{REV}
Release:	1
License:	GPL
Group:		X11/KDE/Applications
Group(pl):	X11/KDE/Aplikacje
Source:		ftp://ftp.kde.org/pub/kde/snapshots/current/%{name}-%{REV}.tar.bz2
URL:		http://kde.koffice.org/
BuildPrereq:	kdelibs-devel
BuildPrereq:	libstdc++-devel
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_pixmapsdir	%{_datadir}/pixmaps
%define		_htmldir	%{_datadir}/doc/HTML

%description
KOffice is an integrated office suite for K Desktop Environment 2.0.
KOffice contains:
* KWord - word processor
* KSpread - spreadsheet
* KPresenter - presentations
* KChart - diagram generator
* KIllustrator - vector drawing

%description -l pl
KOffice jest zintegrowanym pakietem biurowym dla ¶rodowiska KDE 2.0.
Pakiet miêdzy innymi zawiera:
* KWord - procesor tekstu
* KSpread - arkusz kalkulacyjny
* KPresenter - tworzenie prezentacji
* KChart - generator wykresów
* KIllustrator - grafika wektorowa

%package devel
Summary:	KOffice - header files
Summary(pl):	KOffice - pliki nag³ówkowe
Group:		X11/KDE/Development
Group(pl):	X11/KDE/Programowanie
Requires:	%{name} = %{version}

%description devel
Contains header files for KOffice.

%description -l pl devel
Zawiera pliki nag³ówkowe dla KOffice.

%prep
%setup -q -n %{name}

%build
make -f Makefile.cvs

CXXFLAGS="$RPM_OPT_FLAGS -Wall"
LDFLAGS="-s"
export LDFLAGS CXXFLAGS
%configure \
	--enable-final \
	--disable-path-check \
	--disable-closure

#make
make -i LD_LIBRARY_PATH="/usr/X11R6/lib"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

make -i install DESTDIR=$RPM_BUILD_ROOT kde_icondir=%{_pixmapsdir}

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/* || :
strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/*.so* || :

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libasciiexport.so
%attr(755,root,root) %{_libdir}/libasciiimport.so
%attr(755,root,root) %{_libdir}/libhtmlexport.so
%attr(755,root,root) %{_libdir}/libhtmlimport.so
%attr(755,root,root) %{_libdir}/libkchart.so
%attr(755,root,root) %{_libdir}/libkgraph.so
%attr(755,root,root) %{_libdir}/libkillustrator.so
%attr(755,root,root) %{_libdir}/libkimage.so
%attr(755,root,root) %{_libdir}/libkimageshop.so
%attr(755,root,root) %{_libdir}/libkpresenter.so
%attr(755,root,root) %{_libdir}/libkspelltool.so
%attr(755,root,root) %{_libdir}/libkword.so
%attr(755,root,root) %{_libdir}/libolefilter.so
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_applnkdir}/Applications/KOffice
%{_datadir}/apps/kchart
%{_datadir}/apps/kgraph
%{_datadir}/apps/killustrator
%{_datadir}/apps/kimage
%{_datadir}/apps/kimageshop
%{_datadir}/apps/koffice
%{_datadir}/apps/kpresenter
%{_datadir}/apps/kspread
%{_datadir}/apps/kword
%{_htmldir}/en/doc/*
%{_htmldir}/en/katabase
%{_htmldir}/en/killustrator
%{_htmldir}/en/koffice
%{_htmldir}/en/kpresenter
%{_htmldir}/en/kword
%{_pixmapsdir}/locolor/16x16/apps/*
%{_pixmapsdir}/locolor/32x32/apps/*
%{_pixmapsdir}/hicolor/32x32/apps/*
%{_pixmapsdir}/hicolor/48x48/apps/*
%{_datadir}/mimelnk/application/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_libdir}/*.la
%{_libdir}/libkofficecore.so
%{_libdir}/libkofficeui.so
%{_libdir}/libkoml.so
%{_libdir}/libkscript.so
%{_libdir}/libkstore.so
