Summary:	KOffice - powerful office suite for KDE
Summary(pl):	KOffice - potê¿ny pakiet biurowy dla KDE
Name:		koffice
Version:	1.94
Release:	1
License:	GPL
Group:		X11/KDE/Applications
Group(pl):	X11/KDE/Aplikacje
Source0:	ftp://ftp.kde.org/pub/kde/unstable/%{name}-%{version}.tar.bz2
Patch0:		%{name}-applnkdir.patch
URL:		http://koffice.kde.org/
BuildPrereq:	kdelibs-devel = %{version}
BuildPrereq:	libstdc++-devel

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

#################################
# koffice-devel
#################################
%package devel
Summary:	KOffice - header files
Summary(pl):	KOffice - pliki nag³ówkowe
Group:		X11/KDE/Development
Group(pl):	X11/KDE/Programowanie
Requires:	%{name}-common = %{version}

%description devel
Contains header files for KOffice.

%description -l pl devel
Zawiera pliki nag³ówkowe dla KOffice.

#################################
# koffice-common
#################################
%package common
Summary:	KOffice - common files and libraries
Summary(pl):	KOffice - wspó³dzielone pliki i biblioteki
Group:		X11/KDE/Applications
Group(pl):	X11/KDE/Aplikacje
Requires:	kdelibs = %{version}

%description common
Package contains common files and libraries needs by KOffice applications.

%description -l pl common
Pakiet zawiera wspólne pliki i biblioteki wymagane przez aplikacje KOffoce.

#################################
# koffice-kchart
#################################
%package kchart
Summary:	KOffice - KChart
Summary(pl):	KOffice - KChart
Group:		X11/KDE/Applications
Group(pl):	X11/KDE/Aplikacje
Requires:	%{name}-common = %{version}

%description kchart
KChart is KOffice part for generating diagrams from data, e.g. pie and bar
charts.

%description -l pl kchart
KChart jest aplikacj± s³u¿±c± do generowania wykresów.

#################################
# koffice-killustrator
#################################
%package killustrator
Summary:	KOffice - KIllustrator
Summary(pl):	KOffice - KIllustrator
Group:		X11/KDE/Applications
Group(pl):	X11/KDE/Aplikacje
Requires:	%{name}-common = %{version}

%description killustrator
KIllustrator is the vector drawing program for the K Desktop Environment. The
aim of the KIllustrator project is the development of a freely available 
vector-based drawing application similar to Corel Draw or Adobe Illustrator.

%description -l pl killustrator
Killustrator jest programem do tworzenia grafiki wektorowej dla ¶rodowiska KDE.
Celem przy¶wiecaj±cym programistom jest stworzenie w pe³ni funkcjonalnego
programu do grafiki wektorowej podobnego do Corel Draw lub Adobe Illustrator.

#################################
# koffice-kpresenter
#################################
%package kpresenter
Summary:	KOffice - KPresenter
Summary(pl):	KOffice - KPresenter
Group:		X11/KDE/Applications
Group(pl):	X11/KDE/Aplikacje
Requires:	%{name}-common = %{version}

%description kpresenter
KPresenter is a presentation application of the KOffice, similar to 
MS PowerPoint in the windows world. You can use it for doing screen 
presentations or transparencies.

%description -l pl kpresenter
KPresenter jest aplikacj± KOffice do tworzenia prezentacji, podobn± do
MS PowerPoint. Mo¿esz u¿yæ jej do tworzenia wizualnych prezentacji.

#################################
# koffice-kspread
#################################
%package kspread
Summary:	KOffice - KSpread
Summary(pl):	KOffice - KSpread
Group:		X11/KDE/Applications
Group(pl):	X11/KDE/Aplikacje
Requires:	%{name}-common = %{version}

%description kspread
KSpread is the spread sheet of the KOffice, similar to MS Excel.

%description -l pl kspread
KSpread jest arkuszem kalkulacyjnym, podobnym do MS Excel.

#################################
# koffice-kword
#################################
%package kword
Summary:	KOffice - KWord
Summary(pl):	KOffice - KWord
Group:		X11/KDE/Applications
Group(pl):	X11/KDE/Aplikacje
Requires:	%{name}-common = %{version}

%description kword
KWord is a FrameMaker-like wordprocessor application for KOffice. So it can
be used for DTP, but also for "normal" wordprocessing (like writing letters,
reports, etc.).

%description -l pl kword
KWord jest ramkowym procesorem tekstu. Mo¿e byæ u¿yty do DTP, ale równie¿
do zwyk³ej edycji tekstu (jak pisanie listów, raportów, itp.).

######################## end descriptions ########################

%prep
%setup -q
%patch0 -p1

%build
%{__make} -f Makefile.cvs
%configure \
	--disable-path-check

%{__make} LD_LIBRARY_PATH="/usr/X11R6/lib"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_icondir=%{_pixmapsdir} \
	kchartdir=%{_applnkdir}/Office/Misc \
	killustratordir=%{_applnkdir}/Graphics \
	koshelldir=%{_applnkdir}/Office/Misc \
	kpresenterdir=%{_applnkdir}/Office/Presentations \
	kspreaddir=%{_applnkdir}/Office/Spreadsheets \
	kworddir=%{_applnkdir}/Office/Wordprocessors \
	install

# workaround (this files contains kdelib)
rm -rf $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/16x16/actions/{bottom,rotate,top,wizard}.png

%clean
rm -rf $RPM_BUILD_ROOT

%post common	-p /sbin/ldconfig
%postun common	-p /sbin/ldconfig

%post kchart	-p /sbin/ldconfig
%postun kchart	-p /sbin/ldconfig

%post killustrator	-p /sbin/ldconfig
%postun killustrator	-p /sbin/ldconfig

%post kpresenter	-p /sbin/ldconfig
%postun kpresenter	-p /sbin/ldconfig

%post kspread	-p /sbin/ldconfig
%postun kspread	-p /sbin/ldconfig

%post kword	-p /sbin/ldconfig
%postun kword	-p /sbin/ldconfig

#################################
# koffice-common
#################################
%files common
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/koscript
%attr(755,root,root) %{_bindir}/koshell
%attr(755,root,root) %{_bindir}/kprconverter.pl
%attr(755,root,root) %{_libdir}/koshell.so
%{_libdir}/koshell.la
%attr(755,root,root) %{_libdir}/libolefilter.so
%{_libdir}/libolefilter.la
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/apps/koffice
%{_htmldir}/en/doc/*
%{_htmldir}/en/koffice
%{_datadir}/servicetypes/*
%{_datadir}/services/kodocinfopropspage.desktop
%{_pixmapsdir}/locolor/*x*/actions/*
%{_pixmapsdir}/hicolor/*x*/actions/*

#################################
# koffice-devel
#################################
%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_libdir}/libkformula.la
%{_libdir}/libkodocinfopropspage.la
%{_libdir}/libkofficecore.la
%{_libdir}/libkofficeui.la
%{_libdir}/libkoml.la
%{_libdir}/libkoscript.la
%{_libdir}/libkstore.la
%{_libdir}/libkformula.so
%{_libdir}/libkodocinfopropspage.so
%{_libdir}/libkofficecore.so
%{_libdir}/libkofficeui.so
%{_libdir}/libkoml.so
%{_libdir}/libkoscript.so
%{_libdir}/libkstore.so

#################################
# koffice-kchart
#################################
%files kchart
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kchart
%attr(755,root,root) %{_libdir}/kchart.so
%{_libdir}/kchart.la
%attr(755,root,root) %{_libdir}/libkchartpart.so
%{_libdir}/libkchartpart.la
%{_datadir}/apps/kchart
%{_applnkdir}/Office/Misc/kchart.desktop
%{_datadir}/mimelnk/application/x-kchart.desktop
%{_pixmapsdir}/locolor/*x*/apps/kchart.png
%{_pixmapsdir}/hicolor/*x*/apps/kchart.png

#################################
# koffice-killustrator
#################################
%files killustrator
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/killustrator
%attr(755,root,root) %{_libdir}/killustrator.so
%{_libdir}/killustrator.la
%attr(755,root,root) %{_libdir}/libkillustratorpart.so
%{_libdir}/libkillustratorpart.la
%{_datadir}/apps/killustrator
%{_htmldir}/en/killustrator
%{_applnkdir}/Graphics/killustrator.desktop
%{_datadir}/mimelnk/application/x-killustrator.desktop
%{_pixmapsdir}/locolor/*x*/apps/killustrator.png
%{_pixmapsdir}/hicolor/*x*/apps/killustrator.png

#################################
# koffice-kpresenter
#################################
%files kpresenter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpresenter
%attr(755,root,root) %{_libdir}/kpresenter.so
%{_libdir}/kpresenter.la
%attr(755,root,root) %{_libdir}/libkpresenterpart.so
%{_libdir}/libkpresenterpart.la
%{_datadir}/apps/kpresenter
%{_htmldir}/en/kpresenter
%{_applnkdir}/Office/Presentations/kpresenter.desktop
%{_datadir}/mimelnk/application/x-kpresenter.desktop
%{_datadir}/services/ole_powerpoint97_import.desktop
%{_pixmapsdir}/locolor/*x*/apps/kpresenter.png
%{_pixmapsdir}/hicolor/*x*/apps/kpresenter.png

#################################
# koffice-kspread
#################################
%files kspread
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kspread
%attr(755,root,root) %{_libdir}/kspread.so
%{_libdir}/kspread.la
%attr(755,root,root) %{_libdir}/libkspreadpart.so
%{_libdir}/libkspreadpart.la
%attr(755,root,root) %{_libdir}/libkspreadcalc.so
%{_libdir}/libkspreadcalc.la
%{_datadir}/apps/kspread
%{_applnkdir}/Office/Spreadsheets/kspread.desktop
%{_datadir}/mimelnk/application/x-kspread.desktop
%{_datadir}/services/kspread*.desktop
%{_datadir}/services/ole_excel97_import.desktop
%{_pixmapsdir}/locolor/*x*/apps/kspread.png
%{_pixmapsdir}/hicolor/*x*/apps/kspread.png
%{_pixmapsdir}/locolor/*x*/apps/kspreadcalc.png

#################################
# koffice-kword
#################################
%files kword
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kword
%attr(755,root,root) %{_libdir}/kword.so
%{_libdir}/kword.la
%attr(755,root,root) %{_libdir}/libkwordpart.so
%{_libdir}/libkwordpart.la
%attr(755,root,root) %{_libdir}/libasciiexport.so
%{_libdir}/libasciiexport.la
%attr(755,root,root) %{_libdir}/libasciiimport.so
%{_libdir}/libasciiimport.la
%attr(755,root,root) %{_libdir}/libcsvexport.so
%{_libdir}/libcsvexport.la
%attr(755,root,root) %{_libdir}/libcsvimport.so
%{_libdir}/libcsvimport.la
%attr(755,root,root) %{_libdir}/libcsvfilterdia.so
%{_libdir}/libcsvfilterdia.la
%attr(755,root,root) %{_libdir}/libhtmlexport.so
%{_libdir}/libhtmlexport.la
%attr(755,root,root) %{_libdir}/libhtmlimport.so
%{_libdir}/libhtmlimport.la
%attr(755,root,root) %{_libdir}/libkspelltool.so
%{_libdir}/libkspelltool.la
%{_datadir}/apps/kword
%{_htmldir}/en/kword
%{_applnkdir}/Office/Wordprocessors/kword.desktop
%{_datadir}/mimelnk/application/x-kword.desktop
%{_datadir}/services/kspelltool.desktop
%{_datadir}/services/kword*.desktop
%{_datadir}/services/ole_winword97_import.desktop
%{_pixmapsdir}/locolor/*x*/apps/kword.png
%{_pixmapsdir}/hicolor/*x*/apps/kword.png
