Summary:	KOffice - powerful office suite for KDE
Summary(pl):	KOffice - potê¿ny pakiet biurowy dla KDE
Name:		koffice
Version:	2.0.1
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.kde.org/pub/kde/stable/2.0.1/distribution/tar/generic/src/%{name}-%{version}.tar.bz2
URL:		http://koffice.kde.org/
BuildPreReq:	kdelibs-devel = %{version}
BuildPreReq:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	%{_docdir}/kde/HTML
%define         _sharedir       %{_prefix}/share
%define         _htmldir        %{_sharedir}/doc/kde/HTML
%define         _pixmapsdir     %{_sharedir}/icons

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
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
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
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
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
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
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
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
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
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
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
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
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
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
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

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	install

install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/{Wordprocessors,Spreadsheets} \
	$RPM_BUILD_ROOT%{_applnkdir}/{Office/{Presentations,Misc},Graphics}
	
install kchart/k*.desktop $RPM_BUILD_ROOT%{_applnkdir}/Office/Misc
install killustrator/koffice/k*.desktop $RPM_BUILD_ROOT%{_applnkdir}/Graphics
install kpresenter/k*.desktop $RPM_BUILD_ROOT%{_applnkdir}/Office/Presentations
install kspread/k*.desktop $RPM_BUILD_ROOT%{_applnkdir}/Office/Spreadsheets
install kword/k*.desktop $RPM_BUILD_ROOT%{_applnkdir}/Office/Wordprocessors
	
%find_lang killustrator --with-kde
%find_lang kpresenter --with-kde
%find_lang kspread --with-kde
%find_lang kword --with-kde

%find_lang doc --with-kde
%find_lang koffice --with-kde
cat doc.lang koffice.lang > common.lang

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
%files -f common.lang common
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/koscript
%attr(755,root,root) %{_bindir}/koshell
%attr(755,root,root) %{_bindir}/kprconverter.pl
%attr(755,root,root) %{_libdir}/koshell.??
%attr(755,root,root) %{_libdir}/libolefilter.??
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_applnkdir}/Office/koshell.desktop
%{_datadir}/apps/koffice
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
%attr(755,root,root) %{_libdir}/libkformula.??
%attr(755,root,root) %{_libdir}/libkodocinfopropspage.??
%attr(755,root,root) %{_libdir}/libkofficecore.??
%attr(755,root,root) %{_libdir}/libkofficeui.??
%attr(755,root,root) %{_libdir}/libkoml.??
%attr(755,root,root) %{_libdir}/libkoscript.??
%attr(755,root,root) %{_libdir}/libkstore.??

#################################
# koffice-kchart
#################################
%files kchart
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kchart
%attr(755,root,root) %{_libdir}/kchart.??
%attr(755,root,root) %{_libdir}/libkchartpart.??
%{_datadir}/apps/kchart
%{_datadir}/mimelnk/application/x-kchart.desktop
%{_applnkdir}/Office/Misc/kchart.desktop
%{_pixmapsdir}/locolor/*x*/apps/kchart.png
%{_pixmapsdir}/hicolor/*x*/apps/kchart.png

#################################
# koffice-killustrator
#################################
%files -f killustrator.lang killustrator
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/killustrator
%attr(755,root,root) %{_libdir}/killustrator.??
%attr(755,root,root) %{_libdir}/libkillustratorpart.??
%{_datadir}/apps/killustrator
%{_datadir}/mimelnk/application/x-killustrator.desktop
%{_applnkdir}/Graphics/killustrator.desktop
%{_pixmapsdir}/locolor/*x*/apps/killustrator.png
%{_pixmapsdir}/hicolor/*x*/apps/killustrator.png

#################################
# koffice-kpresenter
#################################
%files -f kpresenter.lang kpresenter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpresenter
%attr(755,root,root) %{_libdir}/kpresenter.??
%attr(755,root,root) %{_libdir}/libkpresenterpart.??
%{_datadir}/apps/kpresenter
%{_datadir}/mimelnk/application/x-kpresenter.desktop
%{_datadir}/services/ole_powerpoint97_import.desktop
%{_applnkdir}/Office/Presentations/kpresenter.desktop
%{_pixmapsdir}/locolor/*x*/apps/kpresenter.png
%{_pixmapsdir}/hicolor/*x*/apps/kpresenter.png

#################################
# koffice-kspread
#################################
%files -f kspread.lang kspread
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kspread
%attr(755,root,root) %{_libdir}/kspread.??
%attr(755,root,root) %{_libdir}/libkspreadpart.??
%attr(755,root,root) %{_libdir}/libkspreadcalc.??
%attr(755,root,root) %{_libdir}/libcsvexport.??
%attr(755,root,root) %{_libdir}/libcsvimport.??
%attr(755,root,root) %{_libdir}/libcsvfilterdia.??
%{_datadir}/apps/kspread
%{_datadir}/mimelnk/application/x-kspread.desktop
%{_datadir}/services/kspread*.desktop
%{_datadir}/services/ole_excel97_import.desktop
%{_applnkdir}/Office/Spreadsheets/kspread.desktop
%{_pixmapsdir}/locolor/*x*/apps/kspread.png
%{_pixmapsdir}/hicolor/*x*/apps/kspread.png
%{_pixmapsdir}/locolor/*x*/apps/kspreadcalc.png

#################################
# koffice-kword
#################################
%files -f kword.lang kword
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kword
%attr(755,root,root) %{_libdir}/kword.??
%attr(755,root,root) %{_libdir}/libkwordpart.??
%attr(755,root,root) %{_libdir}/libasciiexport.??
%attr(755,root,root) %{_libdir}/libasciiimport.??
%attr(755,root,root) %{_libdir}/libhtmlexport.??
%attr(755,root,root) %{_libdir}/libhtmlimport.??
%attr(755,root,root) %{_libdir}/libkspelltool.??
%{_datadir}/apps/kword
%{_datadir}/mimelnk/application/x-kword.desktop
%{_datadir}/services/kspelltool.desktop
%{_datadir}/services/kword*.desktop
%{_datadir}/services/ole_winword97_import.desktop
%{_applnkdir}/Office/Wordprocessors/kword.desktop
%{_pixmapsdir}/locolor/*x*/apps/kword.png
%{_pixmapsdir}/hicolor/*x*/apps/kword.png
