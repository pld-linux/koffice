%define	ver	1.1-beta1
Summary:	KOffice - powerful office suite for KDE
Summary(pl):	KOffice - pot�ny pakiet biurowy dla KDE
Name:		koffice
Version:	%(echo %{ver} | sed -e "s#-##g")
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://ftp.kde.org/pub/kde/unstable/%{name}-%{ver}/src/%{name}-%{ver}.tar.bz2
Source1:	http://ftp.kde.org/pub/kde/unstable/%{name}-%{ver}src/%{name}-i18n-%{ver}.tar.bz2
URL:		http://www.koffice.org
BuildRequires:	kdelibs-devel >= 2.1.1
BuildRequires:	libstdc++-devel
BuildRequires:	XFree86-devel
BuildRequires:	qt-devel >= 2.3.0
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	%{_docdir}/kde/HTML
%define         _sharedir       %{_prefix}/share
%define         _htmldir        %{_sharedir}/doc/kde/HTML
%define         _pixmapsdir     %{_sharedir}/icons

%description
KOffice is an integrated office suite for K Desktop Environment.
KOffice contains:
- KWord - word processor
- KSpread - spreadsheet
- KPresenter - presentations
- Kivio - A Visio(R)-style flowcharting application
- KChart - diagram generator
- KIllustrator - vector drawing
- Krayon - A pixel-based image manipulation program like The GIMP or
  Adobe(c) Photoshop(R)
- Kugar - A tool for generating business quality reports

%description -l pl
KOffice jest zintegrowanym pakietem biurowym dla �rodowiska KDE.
Pakiet mi�dzy innymi zawiera:
- KWord - procesor tekstu
- KSpread - arkusz kalkulacyjny
- KPresenter - tworzenie prezentacji
- Kivio - aplikacja wzorowana na Visio(R)
- KChart - generator wykres�w
- KIllustrator - grafika wektorowa
- Krayon - bazuj�cy na pikselach program typu GIMP czy Adobe(c)
  Photoshop(R)
- Kugar - narz�dzie do generowania raport�w jako�ci biznesowej

################################# # koffice-devel
#################################
%package devel
Summary:	KOffice - header files
Summary(pl):	KOffice - pliki nag��wkowe
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-common = %{version}

%description devel
Contains header files for KOffice.

%description -l pl devel
Zawiera pliki nag��wkowe dla KOffice.

################################# # koffice-common
#################################
%package common
Summary:	KOffice - common files and libraries
Summary(pl):	KOffice - wsp�dzielone pliki i biblioteki
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs = %{version}

%description common
Package contains common files and libraries needs by KOffice
applications.

%description -l pl common
Pakiet zawiera wsp�lne pliki i biblioteki wymagane przez aplikacje
KOffoce.

################################# # koffice-kchart
#################################
%package kchart
Summary:	KOffice - KChart
Summary(pl):	KOffice - KChart
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name}-common = %{version}

%description kchart
KChart is KOffice part for generating diagrams from data, e.g. pie and
bar charts.

%description -l pl kchart
KChart jest aplikacj� s�u��c� do generowania wykres�w.

################################# # koffice-killustrator
#################################
%package killustrator
Summary:	KOffice - KIllustrator
Summary(pl):	KOffice - KIllustrator
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name}-common = %{version}

%description killustrator
KIllustrator is the vector drawing program for the K Desktop
Environment. The aim of the KIllustrator project is the development of
a freely available vector-based drawing application similar to Corel
Draw or Adobe Illustrator.

%description -l pl killustrator
Killustrator jest programem do tworzenia grafiki wektorowej dla
�rodowiska KDE. Celem przy�wiecaj�cym programistom jest stworzenie w
pe�ni funkcjonalnego programu do grafiki wektorowej podobnego do Corel
Draw lub Adobe Illustrator.

################################# # koffice-kpresenter
#################################
%package kpresenter
Summary:	KOffice - KPresenter
Summary(pl):	KOffice - KPresenter
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name}-common = %{version}

%description kpresenter
KPresenter is a presentation application of the KOffice, similar to MS
PowerPoint in the windows world. You can use it for doing screen
presentations or transparencies.

%description -l pl kpresenter
KPresenter jest aplikacj� KOffice do tworzenia prezentacji, podobn� do
MS PowerPoint. Mo�esz u�y� jej do tworzenia wizualnych prezentacji.

################################# # koffice-kspread
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

################################# # koffice-kword
#################################
%package kword
Summary:	KOffice - KWord
Summary(pl):	KOffice - KWord
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name}-common = %{version}

%description kword
KWord is a FrameMaker-like wordprocessor application for KOffice. So
it can be used for DTP, but also for "normal" wordprocessing (like
writing letters, reports, etc.).

%description -l pl kword
KWord jest ramkowym procesorem tekstu. Mo�e by� u�yty do DTP, ale
r�wnie� do zwyk�ej edycji tekstu (jak pisanie list�w, raport�w, itp.).

################################# # koffice-ivio
#################################
%package kivio
Summary:	KOffice - ivio
Summary(pl):	KOffice - ivio
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name}-common = %{version}

%description kivio
Kivio on the surface is your everyday flowcharting program. Underneath
this skin, however, lies much more. Kivio will offer basic
flowcharting abilities, but with a twist. Objects are scriptable, and
a backend plugin system will offer the ability to make objects do just
about anything. Feed it a directory of C++ header files, or even Java
files, and let it generate a graphical class map for you. Give it a
network and let it explore and map out the network for you. All this
is possible through the scripting/plugin architecture Kivio will
possess.

%description -l pl kivio
Kivio jest programem typu flowcharting. Kivio dostarcza
najpotrzebniejsze funkcje ale wszystkie obiekty mo�na rozszerza� za
pomoc� j�zyka skryptowego.

################################# # koffice-krayon
#################################
%package krayon
Summary:	KOffice - KRayon
Summary(pl):	KOffice - KRayon
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name}-common = %{version}

%description krayon
Krayon, also known as Kimageshop, is a painting and image editing
application for KOffice.

%description -l pl krayon
Krayon r�wnie� znany jako Kimageshop jest programem do rysowania i
edycji obrazk�w dla KOffice.

################################# # koffice-kugar
#################################
%package kugar
Summary:	KOffice - KUgar
Summary(pl):	KOffice - KUgar
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name}-common = %{version}

%description kugar
Kugar is a KDE tool for generating business quality reports which can
be viewed and printed. It includes a standalone report application can
embed the report viewing functionality and that reports can be viewed
using the Konqueror browser.

%description -l pl kugar
Kugar jest narz�dziem KDE do generowania raport�w o jako�ci
biznesowej, kt�re mog� by� przegl�dane oraz drukowane. Dodatkowo
do��czony jest program kt�ry mo�e by� do��czony do raportu
umo�liwiaj�c ogl�danie raportu w przegl�darce Konqueror.

######################## end descriptions ########################

%prep
%setup -q -n %{name}-%{ver} -a1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--enable-final

%{__make} 

cd %{name}-i18n-%{ver}
%configure

# broken languages
echo -ne "all:\ninstall:\n" > {ja,zh_TW.Big5}/Makefile

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	install

rm -rf $RPM_BUILD_ROOT%{_applnkdir}

install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/{Wordprocessors,Spreadsheets}
install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/{Presentations,Misc}
install -d $RPM_BUILD_ROOT%{_applnkdir}/Graphics

install killustrator/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Graphics
install kpresenter/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Presentations
install kspread/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Spreadsheets
install kword/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Wordprocessors
install kivio/kiviopart/k*.desktop	$RPM_BUILD_ROOT%{_applnkdir}/Office/Misc
install kimageshop/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Graphics
install kugar/part/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Presentations
install kchart/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Misc

install kformula/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Misc
install koshell/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office

cd %{name}-i18n-%{ver}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

%find_lang killustrator --with-kde
%find_lang kpresenter --with-kde
%find_lang kspread --with-kde
%find_lang kword --with-kde
%find_lang kivio --with-kde
%find_lang krayon --with-kde
%find_lang kugar --with-kde
%find_lang kchart --with-kde

%find_lang koffice --with-kde
cat koffice.lang > common.lang

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
%attr(755,root,root) %{_bindir}/kformula
%attr(755,root,root) %{_libdir}/koshell.??
%attr(755,root,root) %{_libdir}/kformulamain.??
%attr(755,root,root) %{_libdir}/kde2/libkformulapart.??
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libkwmf.??
%attr(755,root,root) %{_libdir}/kde2/lib*export*.??
%attr(755,root,root) %{_libdir}/kde2/lib*import*.??
%attr(755,root,root) %{_libdir}/kde2/lib*filter*.??
%attr(755,root,root) %{_libdir}/kde2/libkprkword.??
%{_applnkdir}/Office/koshell.desktop
%{_applnkdir}/Office/Misc/kformula.desktop
%{_datadir}/servicetypes/*
%{_datadir}/templates/*.desktop
%{_datadir}/templates/.source/*
%{_pixmapsdir}/*color/*x*/actions/abs.png
%{_pixmapsdir}/*color/*x*/actions/brac*.png
%{_pixmapsdir}/*color/*x*/actions/frac.png
%{_pixmapsdir}/*color/*x*/actions/int.png
%{_pixmapsdir}/*color/*x*/actions/[lr]su[bp].png
%{_pixmapsdir}/*color/*x*/actions/matrix.png
%{_pixmapsdir}/*color/*x*/actions/paren.png
%{_pixmapsdir}/*color/*x*/actions/prod.png
%{_pixmapsdir}/*color/*x*/actions/sqrt.png
%{_pixmapsdir}/*color/*x*/actions/sum.png
%{_datadir}/apps/koffice
%{_datadir}/apps/kformula
%{_datadir}/services/kodocinfopropspage.desktop
%{_datadir}/mimelnk/application/x-kformula.desktop

#################################
# koffice-devel
#################################
%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/libkformul*.??
%attr(755,root,root) %{_libdir}/libkodocinfopropspage.??
%attr(755,root,root) %{_libdir}/libkochart.??
%attr(755,root,root) %{_libdir}/libkofficecore.??
%attr(755,root,root) %{_libdir}/libkofficeui.??
%attr(755,root,root) %{_libdir}/libkoscript.??
%attr(755,root,root) %{_libdir}/libkstore.??

#################################
# koffice-kchart
#################################
%files kchart
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kchart
%attr(755,root,root) %{_libdir}/kchart.??
%attr(755,root,root) %{_libdir}/kde2/libkchartpart.??
%{_datadir}/apps/kchart
%{_datadir}/mimelnk/application/x-kchart.desktop
%{_applnkdir}/Office/Misc/kchart.desktop
%{_pixmapsdir}/*color/*x*/apps/kchart.png

#################################
# koffice-killustrator
#################################
%files -f killustrator.lang killustrator
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/killustrator
%attr(755,root,root) %{_libdir}/killustrator.??
%attr(755,root,root) %{_libdir}/kde2/libkillustratorpart.??
%{_datadir}/apps/killustrator
%{_datadir}/mimelnk/application/x-killustrator.desktop
%{_applnkdir}/Graphics/killustrator.desktop
%{_pixmapsdir}/*color/*x*/apps/killustrator.png

#################################
# koffice-kpresenter
#################################
%files -f kpresenter.lang kpresenter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpresenter
%attr(755,root,root) %{_bindir}/kprconverter.pl
%attr(755,root,root) %{_libdir}/kpresenter.??
%attr(755,root,root) %{_libdir}/kde2/libkpresenterpart.??
%{_datadir}/apps/kpresenter
%{_datadir}/mimelnk/application/x-kpresenter.desktop
%{_datadir}/services/ole_powerpoint97_import.desktop
%{_applnkdir}/Office/Presentations/kpresenter.desktop
%{_pixmapsdir}/*color/*x*/apps/kpresenter.png

#################################
# koffice-kspread
#################################
%files -f kspread.lang kspread
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kspread
%attr(755,root,root) %{_libdir}/kspread.??
%attr(755,root,root) %{_libdir}/kde2/libkspread*.??
%{_datadir}/apps/kspread
%{_datadir}/mimelnk/application/x-kspread.desktop
%{_datadir}/services/kspread*.desktop
%{_datadir}/services/ole_excel97_import.desktop
%{_applnkdir}/Office/Spreadsheets/kspread.desktop
%{_pixmapsdir}/*color/*x*/apps/kspread.png
%{_pixmapsdir}/*color/*x*/apps/kspreadcalc.png

#################################
# koffice-kword
#################################
%files -f kword.lang kword
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kword
%attr(755,root,root) %{_libdir}/kword.??
%attr(755,root,root) %{_libdir}/kde2/libkwordpart.??
# TODO
#%attr(755,root,root) %{_libdir}/libasciiexport.??
#%attr(755,root,root) %{_libdir}/libasciiimport.??
#%attr(755,root,root) %{_libdir}/libhtmlexport.??
#%attr(755,root,root) %{_libdir}/libhtmlimport.??
%attr(755,root,root) %{_libdir}/kde2/libkspelltool.??
%{_datadir}/apps/kword
%{_datadir}/mimelnk/application/x-kword.desktop
%{_datadir}/services/kspelltool.desktop
%{_datadir}/services/kword*.desktop
%{_datadir}/services/ole_winword97_import.desktop
%{_applnkdir}/Office/Wordprocessors/kword.desktop
%{_pixmapsdir}/*color/*x*/apps/kword.png

#################################
# koffice-kivio
#################################
%files -f kivio.lang kivio
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kivio
%attr(755,root,root) %{_libdir}/*kivio*.??
%attr(755,root,root) %{_libdir}/kde2/*kivio*.??
%{_applnkdir}/Office/Misc/kivio.desktop
%{_datadir}/apps/kivio
%{_pixmapsdir}/*color/*x*/apps/kivio.png
%{_datadir}/mimelnk/application/x-kivio.desktop
%{_datadir}/services/kivio*.desktop

#################################
# koffice-krayon
#################################
%files -f krayon.lang krayon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krayon
%attr(755,root,root) %{_libdir}/krayon.??
%attr(755,root,root) %{_libdir}/libkisp_example.??
%attr(755,root,root) %{_libdir}/kde2/libkrayon*.??
%{_applnkdir}/Graphics/krayon.desktop
%{_datadir}/apps/krayon
%{_pixmapsdir}/*color/*x*/apps/krayon.png
%{_datadir}/mimelnk/application/x-krayon.desktop

#################################
# koffice-kugar
#################################
%files -f kugar.lang kugar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kugar
%attr(755,root,root) %{_libdir}/libkugarpart.??
%{_applnkdir}/Office/Presentations/kugar.desktop
%{_datadir}/apps/kugar
%{_pixmapsdir}/*color/*x*/apps/kugar.png
%{_datadir}/mimelnk/application/x-kugar.desktop
