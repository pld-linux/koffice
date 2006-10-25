#
# TODO:
#	- package:
#	/usr/share/services/ole_powerpoint97_import.desktop
#
#	- move libkexidb*.so to -common package? i.e. kspread needs them.
#	- fix /usr/share/apps/xsltfilter/export/kword/xslfo issue.
#	- remove /usr/share/doc/kde/HTML/en/koffice-apidocs parts from non-apidoc packages.
#
%define		_state		stable
%define		_ver		1.6.0
%define		_snap		%{nil}
%define		artsver		13:1.3.0

Summary:	KOffice - powerful office suite for KDE
Summary(pl):	KOffice - potê¿ny pakiet biurowy dla KDE
Summary(pt_BR):	Suíte de aplicativos office para o KDE
Summary(ru):	îÁÂÏÒ ÏÆÆÉÓÎÙÈ ÐÒÏÇÒÁÍÍ ÄÌÑ KDE
Summary(uk):	îÁÂ¦Ò ÏÆ¦ÓÎÉÈ ÐÒÏÇÒÁÍ ÄÌÑ KDE
Summary(zh_CN):	KDE µÄ°ì¹«Ó¦ÓÃÈí¼þ¼¯¡£
Name:		koffice
Version:	%{_ver}
Release:	0.1
Epoch:		5
License:	GPL/LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/koffice-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	e669cf19b2e1c7db7029c0772c527c0d
Patch0:		kde-common-PLD.patch
Patch1:		%{name}-build.patch
Patch2:		%{name}-python25-64bit.patch
Patch3:		kde-ac260-lt.patch
URL:		http://www.koffice.org/
BuildRequires:	ImageMagick-c++-devel >= 1:6.2.4.0
BuildRequires:	OpenEXR-devel
BuildRequires:	arts-qt-devel >= %{artsver}
BuildRequires:	aspell-devel >= 2:0.50.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdebindings-kjsembed-devel
BuildRequires:	kdelibs-devel >= 9:3.2
BuildRequires:	lcms-devel >= 1.15
BuildRequires:	libexif-devel >= 0.6.12
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libpqxx-devel
BuildRequires:	libtiff-devel
BuildRequires:	libwpd-devel
BuildRequires:	libxml2-devel >= 0:2.4.8
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.2
BuildRequires:	readline-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	ruby-devel
BuildRequires:	sed >= 4.0
BuildRequires:	wv2-devel >= 0.1.9
BuildRequires:	zlib-devel
Requires:	wv2 >= 0.1.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KOffice is an integrated office suite for K Desktop Environment.
KOffice contains:
- KWord - word processor
- KFormula - formula editor
- KSpread - spreadsheet
- KPresenter - presentations
- Kivio - A Visio(R)-style flowcharting application
- KChart - diagram generator
- Kontour - vector drawing
- Karbon - A pixel-based image manipulation program like The GIMP or
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
- Kontour - grafika wektorowa
- Karbon - bazuj±cy na pikselach program typu GIMP czy Adobe(c)
  Photoshop(R)
- Kugar - narzêdzie do generowania raportów jako¶ci biznesowej

%description -l ru
ïÆÆÉÓÎÙÅ ÐÒÏÇÒÁÍÍÙ ÄÌÑ K Desktop Environment 2.0. óÏÄÅÒÖÉÔ: KWord
(ÔÅËÓÔÏ×ÙÊ ÐÒÏÃÅÓÓÏÒ), KSpread (ÜÌÅËÔÒÏÎÎÁÑ ÔÁÂÌÉÃÁ), KPresenter
(ÐÒÅÚÅÎÔÁÃÉÉ) É KChart (ÇÅÎÅÒÁÔÏÒ ÄÉÁÇÒÁÍÍ).

%description -l uk
ïÆ¦ÓÎ¦ ÐÒÏÇÒÁÍÉ ÄÌÑ K Desktop Environment 2.0. í¦ÓÔÉÔØ: KWord
(ÔÅËÓÔÏ×ÉÊ ÐÒÏÃÅÓÏÒ), KSpread (ÅÌÅËÔÒÏÎÎÁ ÔÁÂÌÉÃÑ), KPresenter
(ÐÒÅÚÅÎÔÁÃ¦§) ÔÁ KChart (ÇÅÎÅÒÁÔÏÒ Ä¦ÁÇÒÁÍ).

%package devel
Summary:	KOffice - header files
Summary(es):	Header files for compiling applications that use koffice libraries
Summary(pl):	KOffice - pliki nag³ówkowe
Summary(pt_BR):	Arquivos de inclusão necessários à compilação de aplicações que usem as bibliotecas do koffice
Group:		X11/Development/Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description devel
This package includes the header files you will need to compile
applications that use koffice libraries.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe potrzebne przy kompilowaniu
programów u¿ywaj±cych bibliotek KOffice.

%description devel -l pt_BR
Arquivos de inclusão necessários à compilação de aplicações que usem
as bibliotecas do koffice.

%package common
Summary:	KOffice - common files and libraries
Summary(pl):	KOffice - wspólne pliki i biblioteki
Summary(pt_BR):	Arquivos requeridos por todos os softwares koffice
Group:		X11/Applications
Requires:	kdebase-core >= 9:3.2.0

%description common
KOffice is an integrated office suite for K Desktop Environment.
KOffice contains:
- KWord - word processor
- KFormula - formula editor
- KSpread - spreadsheet
- KPresenter - presentations
- Kivio - A Visio(R)-style flowcharting application
- KChart - diagram generator
- Kontour - vector drawing
- Karbon - A pixel-based image manipulation program like The GIMP or
  Adobe(c) Photoshop(R)
- Kugar - A tool for generating business quality reports

Package contains common files and libraries needs by KOffice
applications.

%description common -l pl
KOffice jest zintegrowanym pakietem biurowym dla ¶rodowiska KDE.
Pakiet miêdzy innymi zawiera:
- KWord - procesor tekstu
- KFormula - edytor równañ
- KSpread - arkusz kalkulacyjny
- KPresenter - tworzenie prezentacji
- Kivio - aplikacja wzorowana na Visio(R)
- KChart - generator wykresów
- Kontour - grafika wektorowa
- Karbon - bazuj±cy na pikselach program typu GIMP czy Adobe(c)
  Photoshop(R)
- Kugar - narzêdzie do generowania raportów jako¶ci biznesowej

Pakiet zawiera wspólne pliki i biblioteki wymagane przez aplikacje
KOffice.

%description common -l pt_BR
Arquivos requeridos por todos os softwares koffice.

%package karbon
Summary:	KOffice - Karbon
Summary(pl):	KOffice - Karbon
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
#karbon has changed its name (again) to curt therefore in the future:
Obsoletes:	koffice-krayon

%description karbon
Karbon is a vector graphics application within koffice.

%description karbon -l pl
Karbon to aplikacja koffice s³u¿±ca do rysowania grafiki wektorowej,

%package kchart
Summary:	KOffice - KChart
Summary(pl):	KOffice - KChart
Summary(pt_BR):	Gerador de diagramas do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description kchart
KChart is KOffice part for generating diagrams from data, e.g. pie and
bar charts.

%description kchart -l pl
KChart jest aplikacj± s³u¿±c± do generowania wykresów.

%description kchart -l pt_BR
Gerador de diagramas do KOffice.

%package kexi
Summary:	KOffice - Kexi
Summary(pl):	KOffice - Kexi
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Obsoletes:	kexi
Obsoletes:	kexi-backend-mysql
Obsoletes:	kexi-backend-pgsql

%description kexi
Kexi is KOffice part for using database system such as MySQL.

%description kexi -l pl
Kexi jest aplikacj± s³u¿±c± do korzystania z systemów baz danych
takich jak MySQL.

%package kformula
Summary:	KOffice - kformula
Summary(pl):	KOffice - kformula
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description kformula
KFormula is KOffice part for creating formulas, equations, etc...

%description kformula -l pl
KFormula jest aplikacj± s³u¿±c± do tworzenia wzorów, równañ, itp.

%package kivio
Summary:	KOffice - kivio
Summary(pl):	KOffice - kivio
Summary(pt_BR):	Editor de fluxogramas do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

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

%description kivio -l pl
Kivio jest programem typu flowcharting. Pod tym pojêciem jednak kryje
siê znacznie wiêcej. Kivio dostarcza najpotrzebniejsze funkcje, ale
wszystkie obiekty mo¿na rozszerzaæ za pomoc± jêzyka skryptowego, a
system wtyczek backendowych oferuje mo¿liwo¶æ tworzenia obiektów
dotycz±cych prawie wszystkiego. Kivio mo¿na nakarmiæ katalogiem plików
nag³ówkowych C++ lub plików Javy i pozwoliæ wygenerowaæ graficzn± mapê
klas. Po podaniu sieci przejrzy j± i stworzy jej mapê. Wszystko to
jest mo¿liwe poprzez architekturê skryptów i wtyczek Kivio.

%description kivio -l pt_BR
Editor de fluxogramas do KOffice.

%package kplato
Summary:	KOffice - KPlato
Summary(pl):	KOffice - KPlato
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description kplato
KPlato is a project management application.

%package kpresenter
Summary:	KOffice - KPresenter
Summary(pl):	KOffice - KPresenter
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description kpresenter
KPresenter is a presentation application of the KOffice, similar to MS
PowerPoint in the windows world. You can use it for doing screen
presentations or transparencies.

%description kpresenter -l pl
KPresenter jest aplikacj± KOffice do tworzenia prezentacji, podobn± do
MS PowerPoint. Mo¿esz u¿yæ jej do tworzenia wizualnych prezentacji.

%package krita
Summary:	KOffice - Krita
Summary(pl):	KOffice - Krita
Summary(pt_BR):	Ferramenta de desenho vetorial do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Obsoletes:	koffice-killustrator

%description krita
Krita is the vector drawing program for the K Desktop Environment. The
aim of the Kontour project is the development of a freely available
vector-based drawing application similar to Corel Draw or Adobe
Illustrator. Krita was formerly known as KIllustrator but due to
blackmail made by Adobe lawyers it has to be renamed.

%description krita -l pl
Krita jest programem do tworzenia grafiki wektorowej dla ¶rodowiska
KDE. Celem przy¶wiecaj±cym programistom jest stworzenie w pe³ni
funkcjonalnego programu do grafiki wektorowej podobnego do Corel Draw
lub Adobe Illustrator.

Krita wczesniej by³ znany jako KIlustrator ale developerzy zostali
zmuszeni szanta¿em przez prawników Adobe do zmiany nazwy.

%description krita -l pt_BR
Ferramenta de desenho vetorial do KOffice.

%package kross-python
Summary:	KOffice - Kross Python
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description kross-python
Kross is a scripting bridge to embed scripting functionality into an
application. Kross provides an abstract API to access the scripting
functionality in a interpreter-independend way. This package provides
Python scripting backend.

%package kross-ruby
Summary:	KOffice - Kross Ruby
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description kross-ruby
Kross is a scripting bridge to embed scripting functionality into an
application. Kross provides an abstract API to access the scripting
functionality in a interpreter-independend way. This package provides
Ruby scripting backend.

%package kspread
Summary:	KOffice - KSpread
Summary(pl):	KOffice - KSpread
Summary(pt_BR):	Planilha eletrônica do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description kspread
KSpread is the spread sheet of the KOffice, similar to MS Excel.

%description kspread -l pl
KSpread jest arkuszem kalkulacyjnym, podobnym do MS Excel.

%description kspread -l pt_BR
Planilha eletrônica do KOffice.

%package kugar
Summary:	KOffice - KUgar
Summary(pl):	KOffice - KUgar
Summary(pt_BR):	Gerador de relatórios do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description kugar
Kugar is a KDE tool for generating business quality reports which can
be viewed and printed. It includes a standalone report application can
embed the report viewing functionality and that reports can be viewed
using the Konqueror browser.

%description kugar -l pl
Kugar jest narzêdziem KDE do generowania raportów o jako¶ci
biznesowej, które mog± byæ przegl±dane oraz drukowane. Dodatkowo
do³±czony jest program który mo¿e byæ do³±czony do raportu
umo¿liwiaj±c ogl±danie raportu w przegl±darce Konqueror.

%description kugar -l pt_BR
Gerador de relatórios do KOffice.

%package kword
Summary:	KOffice - KWord
Summary(pl):	KOffice - KWord
Summary(pt_BR):	Processador de texto do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description kword
KWord is a FrameMaker-like wordprocessor application for KOffice. So
it can be used for DTP, but also for "normal" wordprocessing (like
writing letters, reports, etc.).

%description kword -l pl
KWord jest ramkowym procesorem tekstu. Mo¿e byæ u¿yty do DTP, ale
równie¿ do zwyk³ej edycji tekstu (jak pisanie listów, raportów, itp.).

%description kword -l pt_BR
Processador de texto do KOffice.

%package apidocs
Summary:	Koffice API documentation
Summary(pl):	Dokumentacja API dla Koffice
Group:		Documentation
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description apidocs
Annotated reference of KOffice libraries programming interface
including:
- class lists
- class members
- namespaces

%description apidocs -l pl
Dokumentacja interfejsu programowania bibliotek KOffice z przypisami.
Zawiera:
- listy klas i ich sk³adników
- listê przestrzeni nazw (namespace)

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1
%patch3 -p1

%{__sed} -i 's/Categories=Qt;KDE;Office/Categories=Qt;KDE;Office;X-Misc;/' \
	tools/kthesaurus/KThesaurus.desktop
%{__sed} -i 's/Categories=Qt;KDE;Office/Categories=Qt;KDE;Graphics;/' \
        karbon/data/karbon.desktop
%{__sed} -i 's/Categories=Qt;KDE;Office/Categories=Qt;KDE;Office;X-Misc;/' \
        kchart/kchart.desktop
%{__sed} -i 's/Categories=Qt;KDE;Office/Categories=Qt;KDE;Office;X-Misc;/' \
        kformula/kformula.desktop
%{__sed} -i 's/Categories=Qt;KDE;Office/Categories=Qt;KDE;Office;X-Misc;/' \
        kivio/kiviopart/kivio.desktop
%{__sed} -i 's/Categories=Qt;KDE;Office/Categories=Qt;KDE;Office;Presentation;/' \
        kpresenter/kpresenter.desktop
%{__sed} -i 's/Categories=Qt;KDE;Office/Categories=Qt;KDE;Office;Spreadsheet;/' \
        kspread/kspread.desktop
%{__sed} -i 's/Categories=Qt;KDE;Office/Categories=Qt;KDE;Office;X-Misc;/' \
        kugar/kudesigner/kudesigner.desktop
%{__sed} -i 's/Categories=Qt;KDE;Office/Categories=Qt;KDE;Office;X-Misc;/' \
        kugar/part/kugar.desktop
%{__sed} -i 's/Categories=Qt;KDE;Office/Categories=Qt;KDE;Office;WordProcessor;/' \
        kword/kword.desktop

%{__sed} -i -e '/\[Desktop Entry\]/aEncoding=UTF-8' \
	karbon/data/karbon.desktop
%{__sed} -i -e 's/Terminal=0/Terminal=false/' \
	kugar/kudesigner/kudesigner.desktop \
	kugar/part/kugar.desktop \
	kugar/part/kugarpart.desktop
for f in `find . -name *.desktop`; do
	if grep -q '\[ven\]' $f; then
		sed -i -e 's/\[ven\]/[ve]/' $f
	fi
done

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-pgsqlincdir=%{_includedir} \
	--with-pgsqllibdir=%{_libdir} \
	--with-pqxxincdir=%{_includedir}/pqxx \
	--with-pqxxlibdir=%{_libdir} \
	--with-qt-libraries=%{_libdir} \
	--disable-rpath \
	--disable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT{%{_desktopdir}/kde,%{_mandir}/man1}

mv $RPM_BUILD_ROOT{%{_datadir}/applnk/Office/*,%{_desktopdir}/kde}

install kexi/debian/man/k[es]*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%find_lang karbon		--with-kde
%find_lang kchart		--with-kde
%find_lang kexi			--with-kde
%find_lang kformula		--with-kde
%find_lang kivio		--with-kde
%find_lang koffice		--with-kde
%find_lang koshell		--with-kde
cat koshell.lang >> koffice.lang
%find_lang kplato		--with-kde
%find_lang kpresenter		--with-kde
%find_lang krita		--with-kde
%find_lang kspread		--with-kde
%find_lang kugar		--with-kde
%find_lang kword		--with-kde
%find_lang thesaurus		--with-kde
cat thesaurus.lang >> kword.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	common -p /sbin/ldconfig
%postun common -p /sbin/ldconfig

%post   karbon -p /sbin/ldconfig
%postun karbon -p /sbin/ldconfig

%post   kchart -p /sbin/ldconfig
%postun kchart -p /sbin/ldconfig

%post	kexi -p /sbin/ldconfig
%postun	kexi -p /sbin/ldconfig

%post	kivio -p /sbin/ldconfig
%postun	kivio -p /sbin/ldconfig

%post	kplato -p /sbin/ldconfig
%postun	kplato -p /sbin/ldconfig

%post	kpresenter -p /sbin/ldconfig
%postun	kpresenter -p /sbin/ldconfig

%post	krita -p /sbin/ldconfig
%postun	krita -p /sbin/ldconfig

%post   kspread -p /sbin/ldconfig
%postun kspread -p /sbin/ldconfig

%post   kugar -p /sbin/ldconfig
%postun kugar -p /sbin/ldconfig

%post   kword -p /sbin/ldconfig
%postun kword -p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%exclude %{_libdir}/libkdeinit_*.so
%exclude %{_libdir}/libkudesignercore.so
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_includedir}/kword
%{_includedir}/kross
# move it with *.so for -kexi to -kexi-devel?
%{_includedir}/kexidb
%{_includedir}/kexiutils

%files common -f koffice.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/koconverter
%attr(755,root,root) %{_bindir}/koshell
%attr(755,root,root) %{_bindir}/krossrunner
%{_libdir}/libkdeinit_koshell.la
%attr(755,root,root) %{_libdir}/libkdeinit_koshell.so
%{_libdir}/libkdchart.la
%attr(755,root,root) %{_libdir}/libkdchart.so.*.*.*
%{_libdir}/libkformulalib.la
%attr(755,root,root) %{_libdir}/libkformulalib.so.*.*.*
%{_libdir}/libkochart.la
%attr(755,root,root) %{_libdir}/libkochart.so.*.*.*
%{_libdir}/libkofficecore.la
%attr(755,root,root) %{_libdir}/libkofficecore.so.*.*.*
%{_libdir}/libkofficeui.la
%attr(755,root,root) %{_libdir}/libkofficeui.so.*.*.*
%{_libdir}/libkopainter.la
%attr(755,root,root) %{_libdir}/libkopainter.so.*.*.*
%{_libdir}/libkopalette.la
%attr(755,root,root) %{_libdir}/libkopalette.so.*.*.*
%{_libdir}/libkoproperty.la
%attr(755,root,root) %{_libdir}/libkoproperty.so.*.*.*
%{_libdir}/libkotext.la
%attr(755,root,root) %{_libdir}/libkotext.so.*.*.*
%{_libdir}/libkowmf.la
%attr(755,root,root) %{_libdir}/libkowmf.so.*.*.*
%{_libdir}/libkross*.la
%attr(755,root,root) %{_libdir}/libkross*.so.*.*.*
%{_libdir}/libkstore.la
%attr(755,root,root) %{_libdir}/libkstore.so.*.*.*
%{_libdir}/libkugarlib.la
%attr(755,root,root) %{_libdir}/libkugarlib.so.*.*.*
%{_libdir}/libkwmailmerge_interface.la
%attr(755,root,root) %{_libdir}/libkwmailmerge_interface.so.*.*.*
%{_libdir}/libkwmf.la
%attr(755,root,root) %{_libdir}/libkwmf.so.*.*.*
%{_libdir}/libkwordexportfilters.la
%attr(755,root,root) %{_libdir}/libkwordexportfilters.so.*.*.*
%{_libdir}/kde3/clipartthumbnail.la
%attr(755,root,root) %{_libdir}/kde3/clipartthumbnail.so
%{_libdir}/kde3/kfile_koffice.la
%attr(755,root,root) %{_libdir}/kde3/kfile_koffice.so
%{_libdir}/kde3/kfile_ooo.la
%attr(755,root,root) %{_libdir}/kde3/kfile_ooo.so
%{_libdir}/kde3/kodocinfopropspage.la
%attr(755,root,root) %{_libdir}/kde3/kodocinfopropspage.so
%{_libdir}/kde3/kofficescan.la
%attr(755,root,root) %{_libdir}/kde3/kofficescan.so
%{_libdir}/kde3/kofficethumbnail.la
%attr(755,root,root) %{_libdir}/kde3/kofficethumbnail.so
%{_libdir}/kde3/koshell.la
%attr(755,root,root) %{_libdir}/kde3/koshell.so
%{_libdir}/kde3/libgenerickofilter.la
%attr(755,root,root) %{_libdir}/kde3/libgenerickofilter.so
%{_libdir}/kde3/libxslt*port*.la
%attr(755,root,root) %{_libdir}/kde3/libxslt*port*.so
%{_libdir}/kde3/libkounavailpart.la
%attr(755,root,root) %{_libdir}/kde3/libkounavailpart.so
%{_libdir}/kde3/libolefilter.la
%attr(755,root,root) %{_libdir}/kde3/libolefilter.so
%{_datadir}/apps/koffice
%{_datadir}/apps/kofficewidgets
%{_datadir}/apps/koshell
%{_datadir}/config.kcfg/koshell.kcfg
%{_datadir}/services/clipartthumbnail.desktop
%{_datadir}/services/kfile_koffice.desktop
%{_datadir}/services/kfile_ooo.desktop
%{_datadir}/services/kodocinfopropspage.desktop
%{_datadir}/services/kofficethumbnail.desktop
%{_datadir}/services/kounavail.desktop
%{_datadir}/services/xslt_*.desktop
%{_datadir}/services/generic_filter.desktop
%{_datadir}/servicetypes/*
%dir %{_datadir}/apps/kross
%dir %{_datadir}/templates/.source
%{_desktopdir}/kde/koshell.desktop
%{_datadir}/services/ole_powerpoint97_import.desktop
%{_iconsdir}/hicolor/*/apps/koshell.*
%{_iconsdir}/crystalsvg/*/actions/gsu*.png

%files karbon -f karbon.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karbon
%{_libdir}/libkarbon*.la
%attr(755,root,root) %{_libdir}/libkarbon*.so.*.*.*
%{_libdir}/libkdeinit_karbon.la
%attr(755,root,root) %{_libdir}/libkdeinit_karbon.so
%{_libdir}/kde3/liboodrawimport.la
%attr(755,root,root) %{_libdir}/kde3/liboodrawimport.so
%{_libdir}/kde3/*karbon*.la
%attr(755,root,root) %{_libdir}/kde3/*karbon*.so
%{_libdir}/kde3/*wmf*port.la
%attr(755,root,root) %{_libdir}/kde3/*wmf*port.so
%{_datadir}/apps/karbon
%{_datadir}/apps/konqueror/servicemenus/karbon_konqi.desktop
%{_datadir}/services/karbon*
%{_datadir}/templates/.source/Illustration.karbon
%{_datadir}/templates/Illustration.desktop
%{_desktopdir}/kde/karbon.desktop
%{_iconsdir}/*/*/apps/karbon.png
%{_iconsdir}/hicolor/scalable/apps/karbon.svgz

%files kchart -f kchart.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kchart
%{_libdir}/libkchartcommon.la
%attr(755,root,root) %{_libdir}/libkchartcommon.so.*.*.*
%{_libdir}/libkchartimageexport.la
%attr(755,root,root) %{_libdir}/libkchartimageexport.so.*.*.*
%{_libdir}/libkdeinit_kchart.la
%attr(755,root,root) %{_libdir}/libkdeinit_kchart.so
%{_libdir}/kde3/kchart.la
%attr(755,root,root) %{_libdir}/kde3/kchart.so
%{_libdir}/kde3/libkchart*.la
%attr(755,root,root) %{_libdir}/kde3/libkchart*.so
%{_datadir}/apps/kchart
%{_datadir}/apps/konqueror/servicemenus/kchart_konqi.desktop
%{_datadir}/services/kchart*.desktop
%{_desktopdir}/kde/kchart.desktop
%{_iconsdir}/*/*x*/apps/kchart.png

%files kexi -f kexi.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kexi*
%attr(755,root,root) %{_bindir}/ksqlite
%attr(755,root,root) %{_bindir}/ksqlite2
%attr(755,root,root) %{_bindir}/ksqlite2to3
%{_libdir}/libkdeinit_kexi.la
%attr(755,root,root) %{_libdir}/libkdeinit_kexi.so
%{_libdir}/libkformdesigner.la
%attr(755,root,root) %{_libdir}/libkformdesigner.so.*.*.*
%{_libdir}/libkexi*.la
%attr(755,root,root) %{_libdir}/libkexi*.so.*.*.*
%{_libdir}/kde3/*kexi*.la
%attr(755,root,root) %{_libdir}/kde3/*kexi*.so
%{_libdir}/kde3/kformdesigner_containers.la
%attr(755,root,root) %{_libdir}/kde3/kformdesigner_containers.so
%{_libdir}/kde3/kformdesigner_stdwidgets.la
%attr(755,root,root) %{_libdir}/kde3/kformdesigner_stdwidgets.so
%{_datadir}/apps/kexi
%{_datadir}/apps/konqueror/servicemenus/kexi_konqi.desktop
%{_datadir}/config/kexirc
%{_datadir}/config/magic/kexi.magic
%{_datadir}/mimelnk/application/x-kexiproject-shortcut.desktop
%{_datadir}/mimelnk/application/x-kexiproject-sqlite**.desktop
%{_datadir}/mimelnk/application/x-kexi-connectiondata.desktop
%{_datadir}/services/kexi*
%{_datadir}/services/kformdesigner
%{_desktopdir}/kde/kexi.desktop
%{_iconsdir}/hicolor/*/apps/kexi.*
%{_iconsdir}/crystalsvg/*/mimetypes/kexiproject_*.png
%{_mandir}/man1/*

%files kformula -f kformula.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kformula
%{_libdir}/libkdeinit_kformula*.la
%attr(755,root,root) %{_libdir}/libkdeinit_kformula*.so
%{_libdir}/kde3/libkfo*.la
%attr(755,root,root) %{_libdir}/kde3/libkfo*.so
%{_libdir}/kde3/kformula.la
%attr(755,root,root) %{_libdir}/kde3/kformula.so
%{_datadir}/apps/kformula
%{_datadir}/services/kformula*
%{_datadir}/apps/konqueror/servicemenus/kformula_konqi.desktop
%{_desktopdir}/kde/kformula.desktop
%{_iconsdir}/*/*/actions/abs.png
%{_iconsdir}/*/*/actions/brac*.png
%{_iconsdir}/*/*/actions/frac.png
%{_iconsdir}/*/*/actions/ins*.png
%{_iconsdir}/*/*/actions/rem*.png
%{_iconsdir}/*/*/actions/int.png
%{_iconsdir}/*/*/actions/[lr]su[bp].png
%{_iconsdir}/*/*/actions/matrix.png
%{_iconsdir}/*/*/actions/paren.png
%{_iconsdir}/*/*/actions/prod.png
%{_iconsdir}/*/*/actions/sqrt.png
%{_iconsdir}/*/*/actions/sum.png
%{_iconsdir}/*/*/actions/onetwomatrix.png
%{_iconsdir}/*/*/actions/multiline.png
%{_iconsdir}/*/*/actions/over.png
%{_iconsdir}/*/*/actions/under.png
%{_iconsdir}/*/*/apps/kformula.png

%files kivio -f kivio.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kivio
%{_libdir}/libkiviocommon.la
%attr(755,root,root) %{_libdir}/libkiviocommon.so.*.*.*
%{_libdir}/libkdeinit_kivio.la
%attr(755,root,root) %{_libdir}/libkdeinit_kivio.so
%{_libdir}/kde3/*kivio*.la
%attr(755,root,root) %{_libdir}/kde3/*kivio*.so
%{_libdir}/kde3/straight_connector.la
%attr(755,root,root) %{_libdir}/kde3/straight_connector.so
%{_datadir}/apps/kivio
%{_datadir}/apps/konqueror/servicemenus/kivio_konqi.desktop
%{_datadir}/config.kcfg/kivio.kcfg
%{_datadir}/services/kivio*.desktop
%{_desktopdir}/kde/kivio.desktop
%{_iconsdir}/*/*/apps/kivio.png

%files kplato -f kplato.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kplato
%{_libdir}/libkdeinit_kplato.la
%attr(755,root,root) %{_libdir}/libkdeinit_kplato.so
%{_libdir}/kde3/kplato.la
%attr(755,root,root) %{_libdir}/kde3/kplato.so
%{_libdir}/kde3/libkplatopart.la
%attr(755,root,root) %{_libdir}/kde3/libkplatopart.so
%{_datadir}/apps/kplato
%{_datadir}/services/kplatopart.desktop
%{_desktopdir}/kde/kplato.desktop
%{_iconsdir}/crystalsvg/*/apps/kplato.*

%files kpresenter -f kpresenter.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpresenter
%attr(755,root,root) %{_bindir}/kprconverter.pl
%{_libdir}/libkpresenterimageexport.la
%attr(755,root,root) %{_libdir}/libkpresenterimageexport.so.*.*.*
%{_libdir}/libkpresenterprivate.la
%attr(755,root,root) %{_libdir}/libkpresenterprivate.so.*.*.*
%{_libdir}/libkdeinit_kpresenter.la
%attr(755,root,root) %{_libdir}/libkdeinit_kpresenter.so
%{_libdir}/kde3/kpresenter.la
%attr(755,root,root) %{_libdir}/kde3/kpresenter.so
%{_libdir}/kde3/libkpresenter*.la
%attr(755,root,root) %{_libdir}/kde3/libkpresenter*.so
%{_libdir}/kde3/libkprkword.la
%attr(755,root,root) %{_libdir}/kde3/libkprkword.so
%{_libdir}/kde3/libooimpress*port.la
%attr(755,root,root) %{_libdir}/kde3/libooimpress*port.so
%{_libdir}/kde3/libpowerpointimport.la
%attr(755,root,root) %{_libdir}/kde3/libpowerpointimport.so
%{_datadir}/apps/kpresenter
%{_datadir}/apps/konqueror/servicemenus/kpresenter_konqi.desktop
%{_datadir}/templates/.source/Presentation.kpt
%{_datadir}/templates/Presentation.desktop
%{_datadir}/services/kprkword.desktop
%{_datadir}/services/kpresenter*.desktop
%{_desktopdir}/kde/kpresenter.desktop
%{_iconsdir}/*/*/apps/kpresenter*.png

%files krita -f krita.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krita
%{_libdir}/libkrita*.la
%attr(755,root,root) %{_libdir}/libkrita*.so.*.*.*
%{_libdir}/libkdeinit_krita.la
%attr(755,root,root) %{_libdir}/libkdeinit_krita.so
%{_libdir}/kde3/*krita*.la
%attr(755,root,root) %{_libdir}/kde3/*krita*.so
%{_datadir}/apps/konqueror/servicemenus/krita_konqi.desktop
%{_datadir}/apps/krita
%{_datadir}/apps/kritaplugins
%{_datadir}/services/krita*.desktop
%{_datadir}/templates/Illustration.desktop
%{_desktopdir}/kde/krita.desktop
%{_desktopdir}/kde/krita_*.desktop
%{_iconsdir}/hicolor/*/apps/krita.png

%files kross-python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/krosspython.so
%{_libdir}/kde3/krosspython.la
%{_datadir}/apps/kross/python

%files kross-ruby
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/krossruby.so
%{_libdir}/kde3/krossruby.la

%files kspread -f kspread.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kspread
%{_libdir}/libkdeinit_kspread.la
%attr(755,root,root) %{_libdir}/libkdeinit_kspread.so
%{_libdir}/libkspreadcommon.la
%attr(755,root,root) %{_libdir}/libkspreadcommon.so.*.*.*
%{_libdir}/kde3/kspread.la
%attr(755,root,root) %{_libdir}/kde3/kspread.so
%{_libdir}/kde3/krosskspreadcore.la
%attr(755,root,root) %{_libdir}/kde3/krosskspreadcore.so
%{_libdir}/kde3/kspreadscripting.la
%attr(755,root,root) %{_libdir}/kde3/kspreadscripting.so
%{_libdir}/kde3/libkspread*.la
%attr(755,root,root) %{_libdir}/kde3/libkspread*.so
%{_libdir}/kde3/libcsv*.la
%attr(755,root,root) %{_libdir}/kde3/libcsv*.so
%{_libdir}/kde3/libapplixspreadimport.la
%attr(755,root,root) %{_libdir}/kde3/libapplixspreadimport.so
%{_libdir}/kde3/libexcelimport.la
%attr(755,root,root) %{_libdir}/kde3/libexcelimport.so
%{_libdir}/kde3/kfile_gnumeric.la
%attr(755,root,root) %{_libdir}/kde3/kfile_gnumeric.so
%{_libdir}/kde3/libgnumeric*port.la
%attr(755,root,root) %{_libdir}/kde3/libgnumeric*port.so
%{_libdir}/kde3/libdbase*port.la
%attr(755,root,root) %{_libdir}/kde3/libdbase*port.so
%{_libdir}/kde3/libqproimport.la
%attr(755,root,root) %{_libdir}/kde3/libqproimport.so
%{_libdir}/kde3/libopencalc*port.la
%attr(755,root,root) %{_libdir}/kde3/libopencalc*port.so
%{_libdir}/kde3/kwmailmerge_kspread.la
%attr(755,root,root) %{_libdir}/kde3/kwmailmerge_kspread.so
%{_datadir}/apps/kspread
%{_datadir}/apps/konqueror/servicemenus/kspread_konqi.desktop
%{_datadir}/services/kfile_gnumeric.desktop
%{_datadir}/services/kspread*.desktop
%{_datadir}/services/kwmailmerge_kspread.desktop
%{_datadir}/templates/.source/SpreadSheet.kst
%{_datadir}/templates/SpreadSheet.desktop
%{_desktopdir}/kde/kspread.desktop
%{_iconsdir}/[!l]*/*/apps/kspread*.png

%files kugar -f kugar.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kudesigner
%attr(755,root,root) %{_bindir}/kugar
%{_libdir}/libkdeinit_kudesigner.la
%attr(755,root,root) %{_libdir}/libkdeinit_kudesigner.so
%{_libdir}/libkugarlib.la
%attr(755,root,root) %{_libdir}/libkugarlib.so.*.*.*
%{_libdir}/libkdeinit_kugar.la
%attr(755,root,root) %{_libdir}/libkdeinit_kugar.so
%{_libdir}/libkudesignercore.la
%attr(755,root,root) %{_libdir}/libkudesignercore.so
%{_libdir}/kde3/*kugar*.la
%attr(755,root,root) %{_libdir}/kde3/*kugar*.so
%{_libdir}/kde3/*kudesigner*.la
%attr(755,root,root) %{_libdir}/kde3/*kudesigner*.so
%{_desktopdir}/kde/kudesigner.desktop
%{_desktopdir}/kde/kugar.desktop
%{_datadir}/apps/kudesigner
%{_datadir}/apps/kugar
%{_datadir}/services/kugar_kugar_import.desktop
%{_datadir}/services/kugarpart.desktop
%{_iconsdir}/*/*/*/kudesigner.png
%{_iconsdir}/*/*/*/kugar.png
%{_iconsdir}/*/*/mimetypes/kugardata.png

%files kword -f kword.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kthesaurus
%attr(755,root,root) %{_bindir}/kword
%{_libdir}/libkdeinit_kword.la
%attr(755,root,root) %{_libdir}/libkdeinit_kword.so
%{_libdir}/libkwordprivate.la
%attr(755,root,root) %{_libdir}/libkwordprivate.so.*.*.*
%{_libdir}/libkword*export*.la
%attr(755,root,root) %{_libdir}/libkword*export*.so
%{_libdir}/libkdeinit_kthesaurus.la
%attr(755,root,root) %{_libdir}/libkdeinit_kthesaurus.so
%{_libdir}/kde3/kthesaurus.la
%attr(755,root,root) %{_libdir}/kde3/kthesaurus.so
%{_libdir}/kde3/kword.la
%attr(755,root,root) %{_libdir}/kde3/kword.so
%{_libdir}/kde3/kfile_abiword.la
%attr(755,root,root) %{_libdir}/kde3/kfile_abiword.so
%{_libdir}/kde3/libabiword*port.la
%attr(755,root,root) %{_libdir}/kde3/libabiword*port.so
%{_libdir}/kde3/libhancomwordimport.la
%attr(755,root,root) %{_libdir}/kde3/libhancomwordimport.so
%{_libdir}/kde3/libmswordimport.la
%attr(755,root,root) %{_libdir}/kde3/libmswordimport.so
%{_libdir}/kde3/libapplixwordimport.la
%attr(755,root,root) %{_libdir}/kde3/libapplixwordimport.so
%{_libdir}/kde3/libascii*port.la
%attr(755,root,root) %{_libdir}/kde3/libascii*port.so
%{_libdir}/kde3/libdocbookexport.la
%attr(755,root,root) %{_libdir}/kde3/libdocbookexport.so
%{_libdir}/kde3/libhtml*port.la
%attr(755,root,root) %{_libdir}/kde3/libhtml*port.so
%{_libdir}/kde3/libpalmdoc*port.la
%attr(755,root,root) %{_libdir}/kde3/libpalmdoc*port.so
%{_libdir}/kde3/libamipro*port.la
%attr(755,root,root) %{_libdir}/kde3/libamipro*port.so
%{_libdir}/kde3/libpdfimport.la
%attr(755,root,root) %{_libdir}/kde3/libpdfimport.so
%{_libdir}/kde3/libwml*port.la
%attr(755,root,root) %{_libdir}/kde3/libwml*port.so
%{_libdir}/kde3/librtf*port.la
%attr(755,root,root) %{_libdir}/kde3/librtf*port.so
%{_libdir}/kde3/libthesaurustool.la
%attr(755,root,root) %{_libdir}/kde3/libthesaurustool.so
%{_libdir}/kde3/libwp*port.la
%attr(755,root,root) %{_libdir}/kde3/libwp*port.so
%{_libdir}/kde3/libmswrite*port.la
%attr(755,root,root) %{_libdir}/kde3/libmswrite*port.so
%{_libdir}/kde3/libkword*.la
%attr(755,root,root) %{_libdir}/kde3/libkword*.so
%{_libdir}/kde3/liboowriter*port.la
%attr(755,root,root) %{_libdir}/kde3/liboowriter*port.so
%{_libdir}/kde3/kwmailmerge_classic.la
%attr(755,root,root) %{_libdir}/kde3/kwmailmerge_classic.so
%{_libdir}/kde3/kwmailmerge_kabc.la
%attr(755,root,root) %{_libdir}/kde3/kwmailmerge_kabc.so
%{_libdir}/kde3/kwmailmerge_qtsqldb*.la
%attr(755,root,root) %{_libdir}/kde3/kwmailmerge_qtsqldb*.so
%{_datadir}/apps/kword
%{_datadir}/apps/thesaurus
%{_datadir}/apps/xsltfilter/export/kword/xslfo/*.xsl
%{_datadir}/apps/konqueror/servicemenus/kword_konqi.desktop
%{_datadir}/services/kfile_abiword.desktop
%{_datadir}/services/kword*.desktop
%{_datadir}/services/thesaurustool.desktop
%{_datadir}/services/kwmailmerge_kabc.desktop
# this is the mailmerge service info for qtsqldb and classic
%{_datadir}/services/kwserialletter*
%{_datadir}/templates/.source/TextDocument.kwt
%{_datadir}/templates/TextDocument.desktop
%{_desktopdir}/kde/KThesaurus.desktop
%{_desktopdir}/kde/kword.desktop
%{_iconsdir}/*/*/apps/kword.png

%files apidocs
%defattr(644,root,root,755)
%{_kdedocdir}/en/%{name}-apidocs
