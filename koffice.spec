%define	ver	1.1
Summary:	KOffice - powerful office suite for KDE
Summary(pl):	KOffice - potê¿ny pakiet biurowy dla KDE
Name:		koffice
Version:	1.1
Release:	0.1
Epoch:		2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://ftp.kde.org/pub/kde/unstable/%{name}-%{ver}/src/%{name}-%{ver}.tar.bz2
Source1:	http://ftp.kde.org/pub/kde/unstable/%{name}-%{ver}/src/%{name}-i18n-%{ver}.tar.bz2
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
BuildRequires:	python-devel >= 2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	%{_docdir}/kde/HTML
%define         _htmldir        %{_datadir}/doc/kde/HTML

%description
KOffice is an integrated office suite for K Desktop Environment.
KOffice contains:
- KWord - word processor
- KFormula - formula editor
- KSpread - spreadsheet
- KPresenter - presentations
- Kivio - A Visio(R)-style flowcharting application
- KChart - diagram generator
- KIllustrator - vector drawing
- Krayon - A pixel-based image manipulation program like The GIMP or
  Adobe(c) Photoshop(R)
- Kugar - A tool for generating business quality reports

%description -l pl
KOffice jest zintegrowanym pakietem biurowym dla ¶rodowiska KDE.
Pakiet miêdzy innymi zawiera:
- KWord - procesor tekstu
- KFormula - edytor równañ
- KSpread - arkusz kalkulacyjny
- KPresenter - tworzenie prezentacji
- Kivio - aplikacja wzorowana na Visio(R)
- KChart - generator wykresów
- KIllustrator - grafika wektorowa
- Krayon - bazuj±cy na pikselach program typu GIMP czy Adobe(c)
  Photoshop(R)
- Kugar - narzêdzie do generowania raportów jako¶ci biznesowej

# koffice-devel
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

# koffice-common
%package common
Summary:	KOffice - common files and libraries
Summary(pl):	KOffice - wspó³dzielone pliki i biblioteki
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= 2.1.1

%description common
KOffice is an integrated office suite for K Desktop Environment.
KOffice contains:
- KWord - word processor
- KFormula - formula editor
- KSpread - spreadsheet
- KPresenter - presentations
- Kivio - A Visio(R)-style flowcharting application
- KChart - diagram generator
- KIllustrator - vector drawing
- Krayon - A pixel-based image manipulation program like The GIMP or
  Adobe(c) Photoshop(R)
- Kugar - A tool for generating business quality reports

Package contains common files and libraries needs by KOffice
applications.

%description -l pl common
KOffice jest zintegrowanym pakietem biurowym dla ¶rodowiska KDE.
Pakiet miêdzy innymi zawiera:
- KWord - procesor tekstu
- KFormula - edytor równañ
- KSpread - arkusz kalkulacyjny
- KPresenter - tworzenie prezentacji
- Kivio - aplikacja wzorowana na Visio(R)
- KChart - generator wykresów
- KIllustrator - grafika wektorowa
- Krayon - bazuj±cy na pikselach program typu GIMP czy Adobe(c)
  Photoshop(R)
- Kugar - narzêdzie do generowania raportów jako¶ci biznesowej

Pakiet zawiera wspólne pliki i biblioteki wymagane przez aplikacje
KOffoce.

# koffice-kchart
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
KChart jest aplikacj± s³u¿±c± do generowania wykresów.

# koffice-kontour (f. k. a. koffice-killustrator)
%package kontour
Summary:	KOffice - Kontour
Summary(pl):	KOffice - Kontour
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name}-common = %{version}

%description kontour
Kontour is the vector drawing program for the K Desktop Environment. The
aim of the Kontour project is the development of a freely available
vector-based drawing application similar to Corel Draw or Adobe
Illustrator.

Kontour was formerly known as KIllustrator but due to blackmail made by
Adobe lawyers it has to be renamed.

%description -l pl kontour
Kontour jest programem do tworzenia grafiki wektorowej dla
¶rodowiska KDE. Celem przy¶wiecaj±cym programistom jest stworzenie w
pe³ni funkcjonalnego programu do grafiki wektorowej podobnego do Corel
Draw lub Adobe Illustrator.

Kontour wczesniej by³ znany jako KIlustrator ale developerzy zostali
zmuszeni szantarzem przez prawników Adobe do zmiany nazwy.

# koffice-kpresenter
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
KPresenter jest aplikacj± KOffice do tworzenia prezentacji, podobn± do
MS PowerPoint. Mo¿esz u¿yæ jej do tworzenia wizualnych prezentacji.

# koffice-kspread
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

# koffice-kword
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
KWord jest ramkowym procesorem tekstu. Mo¿e byæ u¿yty do DTP, ale
równie¿ do zwyk³ej edycji tekstu (jak pisanie listów, raportów, itp.).

# koffice-ivio
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
najpotrzebniejsze funkcje ale wszystkie obiekty mo¿na rozszerzaæ za
pomoc± jêzyka skryptowego.

# koffice-krayon
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
Krayon równie¿ znany jako Kimageshop jest programem do rysowania i
edycji obrazków dla KOffice.

# koffice-kugar
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
Kugar jest narzêdziem KDE do generowania raportów o jako¶ci
biznesowej, które mog± byæ przegl±dane oraz drukowane. Dodatkowo
do³±czony jest program który mo¿e byæ do³±czony do raportu
umo¿liwiaj±c ogl±danie raportu w przegl±darce Konqueror.

######################## end descriptions ########################

%prep
%setup -q -n %{name}-%{ver} -a1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure2_13 \
	%{!?debug:--disable-debug} \
	--enable-final

%{__make} 

cd %{name}-i18n-%{ver}
%configure2_13

# broken languages
#for lang in ja zh_TW.Big5; do
#	echo -ne "all:\ninstall:\n" > ${lang}/Makefile
#done

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

install kontour/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Graphics
install kpresenter/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Presentations
install kspread/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Spreadsheets
install kword/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Wordprocessors
install kivio/kiviopart/k*.desktop	$RPM_BUILD_ROOT%{_applnkdir}/Office/Misc
#install kimageshop/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Graphics
install kugar/part/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Presentations
install kchart/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Misc

install kformula/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Misc
install koshell/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office

cd %{name}-i18n-%{ver}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

%find_lang kontour --with-kde
%find_lang kpresenter --with-kde
%find_lang kspread --with-kde
%find_lang kspreadcalc_calc --with-kde
cat kspreadcalc_calc.lang >> kspread.lang
%find_lang kword --with-kde
%find_lang kivio --with-kde
#%find_lang krayon --with-kde
%find_lang kugar --with-kde
%find_lang kchart --with-kde
%find_lang koshell --with-kde
%find_lang koffice --with-kde
%find_lang graphite --with-kde
%find_lang kformula --with-kde
cat koshell.lang graphite.lang koffice.lang kformula.lang > common.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post common	-p /sbin/ldconfig
%postun common	-p /sbin/ldconfig

%post kchart	-p /sbin/ldconfig
%postun kchart	-p /sbin/ldconfig

%post kontour	-p /sbin/ldconfig
%postun kontour	-p /sbin/ldconfig

%post kpresenter	-p /sbin/ldconfig
%postun kpresenter	-p /sbin/ldconfig

%post kspread	-p /sbin/ldconfig
%postun kspread	-p /sbin/ldconfig

%post kword	-p /sbin/ldconfig
%postun kword	-p /sbin/ldconfig

%post kivio	-p /sbin/ldconfig
%postun kivio	-p /sbin/ldconfig

%post krayon	-p /sbin/ldconfig
%postun krayon	-p /sbin/ldconfig

%post kugar	-p /sbin/ldconfig
%postun kugar	-p /sbin/ldconfig

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
%attr(755,root,root) %{_libdir}/kde2/libolefilter.??
%attr(755,root,root) %{_libdir}/libkwmf.??
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_applnkdir}/Office/koshell.desktop
%{_applnkdir}/Office/Misc/kformula.desktop
%{_datadir}/servicetypes/*
%{_datadir}/templates/*.desktop
%{_datadir}/templates/.source/*
%{_pixmapsdir}/*color/*x*/actions/abs.png
%{_pixmapsdir}/*color/*x*/actions/brac*.png
%{_pixmapsdir}/*color/*x*/actions/frac.png
#%{_pixmapsdir}/*color/*x*/actions/funct.png
%{_pixmapsdir}/*color/*x*/actions/int.png
%{_pixmapsdir}/*color/*x*/actions/[lr]su[bp].png
%{_pixmapsdir}/*color/*x*/actions/matrix.png
%{_pixmapsdir}/*color/*x*/actions/paren.png
%{_pixmapsdir}/*color/*x*/actions/prod.png
#%{_pixmapsdir}/*color/*x*/actions/percent.png
#%{_pixmapsdir}/*color/*x*/actions/prec_*.png
%{_pixmapsdir}/*color/*x*/actions/sqrt.png
%{_pixmapsdir}/*color/*x*/actions/sum.png
#%{_pixmapsdir}/*color/*x*/actions/border_*.png
%{_datadir}/apps/koffice
%{_datadir}/apps/kformula
%{_datadir}/services/kodocinfopropspage.desktop
%{_datadir}/services/ole_*.desktop
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
%files -f kchart.lang kchart
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kchart
%attr(755,root,root) %{_libdir}/kchart.??
%attr(755,root,root) %{_libdir}/kde2/libkchartpart.??
%{_datadir}/apps/kchart
%{_datadir}/mimelnk/application/x-kchart.desktop
#%{_applnkdir}/Office/Misc/kchart.desktop
%{_pixmapsdir}/*color/*x*/apps/kchart.png

#################################
# koffice-kontour
#################################
%files -f kontour.lang kontour
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kontour
%attr(755,root,root) %{_libdir}/kontour.??
%attr(755,root,root) %{_libdir}/kde2/libkontourpart.??
%attr(755,root,root) %{_libdir}/kde2/libapplixgraphicimport.??
%attr(755,root,root) %{_libdir}/kde2/libmsodimport.??
%attr(755,root,root) %{_libdir}/kde2/libwmfimport.??
%attr(755,root,root) %{_libdir}/kde2/libkprkword.??
%{_datadir}/apps/kontour
#%{_datadir}/services/kontour_*.desktop
%{_datadir}/services/kprkword.desktop
%{_datadir}/mimelnk/application/x-kontour.desktop
%{_datadir}/mimelnk/image/x-msod.desktop
%{_datadir}/mimelnk/image/x-wmf.desktop
%{_applnkdir}/Graphics/kontour.desktop
%{_pixmapsdir}/*color/*x*/apps/kontour.png

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
%attr(755,root,root) %{_libdir}/kde2/libcsv*.??
%attr(755,root,root) %{_libdir}/kde2/libapplixspreadimport.??
%{_datadir}/apps/kspread
%{_datadir}/mimelnk/application/x-kspread.desktop
%{_datadir}/mimelnk/text/x-csv.desktop
%{_datadir}/services/kspread*.desktop
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
%attr(755,root,root) %{_libdir}/kde2/libabiword*port.??
%attr(755,root,root) %{_libdir}/kde2/libapplixwordimport.??
%attr(755,root,root) %{_libdir}/kde2/libascii*port.??
%attr(755,root,root) %{_libdir}/kde2/libdocbookexport.??
%attr(755,root,root) %{_libdir}/kde2/libhtml*port.??
#%attr(755,root,root) %{_libdir}/kde2/libhtml*portdia.??
%attr(755,root,root) %{_libdir}/kde2/liblatexexport.??
%attr(755,root,root) %{_libdir}/kde2/librtf*port.??
%attr(755,root,root) %{_libdir}/kde2/libkspelltool.??
%{_datadir}/apps/kword
%{_datadir}/mimelnk/application/x-kword.desktop
%{_datadir}/mimelnk/application/x-abiword.desktop
%{_datadir}/services/kspelltool.desktop
%{_datadir}/services/kword*.desktop
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
#%attr(755,root,root) %{_bindir}/krayon
#%attr(755,root,root) %{_libdir}/krayon.??
#%attr(755,root,root) %{_libdir}/libkisp_example.??
#%attr(755,root,root) %{_libdir}/kde2/libkrayon*.??
#%{_applnkdir}/Graphics/krayon.desktop
#%{_datadir}/apps/krayon
#%{_pixmapsdir}/*color/*x*/apps/krayon.png
#%{_datadir}/mimelnk/application/x-krayon.desktop

#################################
# koffice-kugar
#################################
%files -f kugar.lang kugar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kugar
%attr(755,root,root) %{_libdir}/libkugarpart.??
#%{_applnkdir}/Office/Presentations/kugar.desktop
%{_datadir}/apps/kugar
%{_pixmapsdir}/*color/*x*/apps/kugar.png
%{_datadir}/mimelnk/application/x-kugar.desktop
