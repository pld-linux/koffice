%define	ver	1.1
Summary:	KOffice - powerful office suite for KDE
Summary(pl):	KOffice - potê¿ny pakiet biurowy dla KDE
Summary(pt_BR):	Suíte de aplicativos office para o KDE
Name:		koffice
Version:	1.1
Release:	6
Epoch:		4
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}-%{ver}/src/%{name}-%{ver}.tar.bz2
Source1:	ftp://ftp.kde.org/pub/kde/stable/%{name}-%{ver}/src/%{name}-i18n-%{ver}.tar.bz2
URL:		http://www.koffice.org/
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
%define         _htmldir        /usr/share/doc/kde/HTML

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
Summary(es):	Header files for compiling applications that use koffice libraries.
Summary(pl):	KOffice - pliki nag³ówkowe
Summary(pt_BR):	Arquivos de inclusão necessários à compilação de aplicações que usem as bibliotecas do koffice
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-common = %{version}

%description devel
This package includes the header files you will need to compile
applications that use koffice libraries.

%description -l pl devel
Ten pakiet zawiera pliki nag³ówkowe, których bêdziesz potrzebowa³ aby
skompilowaæ programy u¿ywaj±ce bibliotek KOffice.

%description -l pt_BR devel
Arquivos de inclusão necessários à compilação de aplicações
que usem as bibliotecas do koffice.

# koffice-common
%package common
Summary:	KOffice - common files and libraries
Summary(pl):	KOffice - wspó³dzielone pliki i biblioteki
Summary(pt_BR):	Arquivos requeridos por todos os softwares koffice
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= 2.1.1
Obsoletes:	koffice-i18n-Azerbaijani
Obsoletes:	koffice-i18n-Bulgarian
Obsoletes:	koffice-i18n-Czech
Obsoletes:	koffice-i18n-Danish
Obsoletes:	koffice-i18n-German
Obsoletes:	koffice-i18n-British
Obsoletes:	koffice-i18n-Esperanto
Obsoletes:	koffice-i18n-Spanish
Obsoletes:	koffice-i18n-Estonian
Obsoletes:	koffice-i18n-French
Obsoletes:	koffice-i18n- Hebrew
Obsoletes:	koffice-i18n-Hungarian
Obsoletes:	koffice-i18n- Icelandic
Obsoletes:	koffice-i18n-Italian
Obsoletes:	koffice-i18n-Japanese
Obsoletes:	koffice-i18n-Lithuanian
Obsoletes:	koffice-i18n-Maltese
Obsoletes:	koffice-i18n-Dutch
Obsoletes:	koffice-i18n-Norwegian
Obsoletes:	koffice-i18n-Norwegian-Nynorsk
Obsoletes:	koffice-i18n-Polish
Obsoletes:	koffice-i18n-Portuguese
Obsoletes:	koffice-i18n-Brazil
Obsoletes:	koffice-i18n-Romanian
Obsoletes:	koffice-i18n-Russian
Obsoletes:	koffice-i18n-Slovak
Obsoletes:	koffice-i18n-Slovenian
Obsoletes:	koffice-i18n-Swedish
Obsoletes:	koffice-i18n-Tamil
Obsoletes:	koffice-i18n-Turkish

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

%description -l pt_BR common
Arquivos requeridos por todos os softwares koffice.

# koffice-kchart
%package kchart
Summary:	KOffice - KChart
Summary(pl):	KOffice - KChart
Summary(pt_BR):	Gerador de diagramas do KOffice
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name}-common = %{version}

%description kchart
KChart is KOffice part for generating diagrams from data, e.g. pie and
bar charts.

%description -l pl kchart
KChart jest aplikacj± s³u¿±c± do generowania wykresów.

%description -l pt_BR kchart
Gerador de diagramas do KOffice.

# koffice-kontour (f. k. a. koffice-killustrator)
%package kontour
Summary:	KOffice - Kontour
Summary(pl):	KOffice - Kontour
Summary(pt_BR):	Ferramenta de desenho vetorial do KOffice
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

%description -l pt_BR kontour
Ferramenta de desenho vetorial do KOffice.

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
Summary(pt_BR):	Planilha eletrônica do KOffice
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name}-common = %{version}

%description kspread
KSpread is the spread sheet of the KOffice, similar to MS Excel.

%description -l pl kspread
KSpread jest arkuszem kalkulacyjnym, podobnym do MS Excel.

%description -l pt_BR kspread
Planilha eletrônica do KOffice.

# koffice-kword
%package kword
Summary:	KOffice - KWord
Summary(pl):	KOffice - KWord
Summary(pt_BR):	Processador de texto do KOffice
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

%description -l pt_BR kword
Processador de texto do KOffice.

# koffice-ivio
%package kivio
Summary:	KOffice - ivio
Summary(pl):	KOffice - ivio
Summary(pt_BR):	Editor de fluxogramas do KOffice
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

%description -l pt_BR kivio
Editor de fluxogramas do KOffice.

# koffice-kugar
%package kugar
Summary:	KOffice - KUgar
Summary(pl):	KOffice - KUgar
Summary(pt_BR):	Gerador de relatórios do KOffice
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

%description -l pt_BR kugar
Gerador de relatórios do KOffice.

######################## end descriptions ########################

%prep
%setup -q -n %{name}-%{ver} -a1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
CFLAGS="-D_GNU_SOURCE $RPM_OPT_FLAGS"
CXXFLAGS="-D_GNU_SOURCE $RPM_OPT_FLAGS -fno-check-new"
%configure2_13 \
	%{!?debug:--disable-debug} \
	--enable-final \
	--with-xinerama \
	--disable-rpath

%{__make} 

cd %{name}-i18n-%{ver}
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_applnkdir}

install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/{Wordprocessors,Spreadsheets}
install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/{Presentations,Misc}
install -d $RPM_BUILD_ROOT%{_applnkdir}/Graphics

install kontour/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Graphics
install kpresenter/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Presentations
install kspread/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Spreadsheets
install kword/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Wordprocessors
install kivio/kiviopart/k*.desktop	$RPM_BUILD_ROOT%{_applnkdir}/Office/Misc
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
%find_lang csvfilter --with-kde
cat kspreadcalc_calc.lang csvfilter.lang >> kspread.lang
%find_lang kword --with-kde
%find_lang kivio --with-kde
%find_lang kugar --with-kde
%find_lang kchart --with-kde
%find_lang koshell --with-kde
%find_lang koffice --with-kde
%find_lang graphite --with-kde
%find_lang kformula --with-kde
%find_lang kscan_plugin --with-kde
# Not sure if it is the right place.
%find_lang example --with-kde
cat koshell.lang graphite.lang koffice.lang kformula.lang kscan_plugin.lang example.lang \
	> common.lang

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
%attr(755,root,root) %{_bindir}/filter_wrapper
%attr(755,root,root) %{_libdir}/koshell.??
%attr(755,root,root) %{_libdir}/kformulamain.??
%attr(755,root,root) %{_libdir}/kde2/libkformulapart.??
%attr(755,root,root) %{_libdir}/kde2/libolefilter.??
%attr(755,root,root) %{_libdir}/kde2/libkofficescan.??
%attr(755,root,root) %{_libdir}/libkwmf.??
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libkdchart.la
%{_applnkdir}/Office/koshell.desktop
%{_applnkdir}/Office/Misc/kformula.desktop
%{_datadir}/servicetypes/*
%dir %{_datadir}/templates
%dir %{_datadir}/templates/.source
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
%{_pixmapsdir}/*color/*x*/actions/onetwomatrix.png
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
%attr(755,root,root) %{_libdir}/libkdchart.so
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
%{_applnkdir}/Office/Misc/kchart.desktop
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
%attr(755,root,root) %{_libdir}/kde2/libsvgimport.??
%attr(755,root,root) %{_libdir}/kde2/libsvgexport.??
%attr(755,root,root) %{_libdir}/kde2/libxfigimport.??
%{_datadir}/apps/kontour
%{_datadir}/services/killustrator_*.desktop
%{_datadir}/services/kprkword.desktop
%{_datadir}/services/ki_rtf_export.desktop
%{_datadir}/mimelnk/application/x-kontour.desktop
%{_datadir}/mimelnk/application/x-killustrator.desktop
%{_datadir}/mimelnk/image/x-msod.desktop
%{_datadir}/mimelnk/image/x-wmf.desktop
%{_datadir}/mimelnk/image/x-xfig.desktop
%{_datadir}/mimelnk/image/x-svg.desktop
%{_datadir}/templates/.source/Illustration.kil
%{_datadir}/templates/Illustration.desktop
%{_applnkdir}/Graphics/kontour.desktop
%{_applnkdir}/Graphics/killustrator.desktop
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
%{_datadir}/templates/.source/Presentation.kpt
%{_datadir}/templates/Presentation.desktop
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
%attr(755,root,root) %{_libdir}/kde2/libgnumericimport.??
%attr(755,root,root) %{_libdir}/kde2/libgnumericexport.??
%attr(755,root,root) %{_libdir}/kde2/libqproimport.??
%{_datadir}/apps/kspread
%{_datadir}/mimelnk/application/x-kspread.desktop
%{_datadir}/mimelnk/application/x-quattropro.desktop
%{_datadir}/mimelnk/text/x-csv.desktop
%{_datadir}/mimelnk/text/x-gnumeric.desktop
%{_datadir}/services/kspread*.desktop
%{_datadir}/templates/.source/SpreadSheet.ksp
%{_datadir}/templates/SpreadSheet.desktop
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
%attr(755,root,root) %{_libdir}/kde2/liblatexexport.??
%attr(755,root,root) %{_libdir}/kde2/librtf*port.??
%attr(755,root,root) %{_libdir}/kde2/libkspelltool.??
%{_datadir}/apps/kword
%{_datadir}/mimelnk/application/x-kword.desktop
%{_datadir}/mimelnk/application/x-abiword.desktop
%{_datadir}/services/kspelltool.desktop
%{_datadir}/services/kword*.desktop
%{_datadir}/services/*_kword.desktop
%{_datadir}/templates/.source/TextDocument.kwt
%{_datadir}/templates/TextDocument.desktop
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
# koffice-kugar
#################################
%files -f kugar.lang kugar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kugar
%attr(755,root,root) %{_libdir}/libkugarpart.??
%{_applnkdir}/Office/Presentations/kugar.desktop
%{_datadir}/apps/kugar
%{_pixmapsdir}/*color/*x*/*/kugar*.png
%{_datadir}/mimelnk/application/x-kugar.desktop
