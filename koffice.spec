#
# Conditional build:
%bcond_without  apidocs # do not prepare API documentation

%define		_state		stable
%define		_ver		1.4.1
%define		_snap		%{nil}
%define		artsver		13:1.4.1

Summary:	KOffice - powerful office suite for KDE
Summary(pl.UTF-8):   KOffice - potężny pakiet biurowy dla KDE
Summary(pt_BR.UTF-8):   Suíte de aplicativos office para o KDE
Summary(ru.UTF-8):   Набор оффисных программ для KDE
Summary(uk.UTF-8):   Набір офісних програм для KDE
Summary(zh_CN.UTF-8):   KDE 的办公应用软件集。
Name:		koffice
Version:	%{_ver}
Release:	0.1
Epoch:		6
License:	GPL/LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	91a7b68757addc5934c5a8209a4926d5
Patch0:		kde-common-PLD.patch
URL:		http://www.koffice.org/
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	arts-qt-devel >= %{artsver}
BuildRequires:	aspell-devel >= 0.50.2
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.2.92
#BuildRequires:	kdebindings-kjsembed-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libpqxx-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libwpd-devel
BuildRequires:	mysql-devel
BuildRequires:	perl-base
BuildRequires:	python-devel >= 2.2
%{?with_apidocs:BuildRequires:  qt-doc}
BuildRequires:	rpmbuild(macros) >= 1.129
#BuildRequires:	unsermake >= 040511
BuildRequires:	wv2-devel >= 0.0.7
BuildRequires:	zlib-devel
Requires:	wv2 >= 0.0.7
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

%description -l pl.UTF-8
KOffice jest zintegrowanym pakietem biurowym dla środowiska KDE.
Pakiet między innymi zawiera:
- KWord - procesor tekstu
- KFormula - edytor równań
- KSpread - arkusz kalkulacyjny
- KPresenter - tworzenie prezentacji
- Kivio - aplikacja wzorowana na Visio(R)
- KChart - generator wykresów
- Kontour - grafika wektorowa
- Karbon - bazujący na pikselach program typu GIMP czy Adobe(c)
  Photoshop(R)
- Kugar - narzędzie do generowania raportów jakości biznesowej

%description -l ru.UTF-8
Оффисные программы для K Desktop Environment 2.0. Содержит: KWord
(текстовый процессор), KSpread (электронная таблица), KPresenter
(презентации) и KChart (генератор диаграмм).

%description -l uk.UTF-8
Офісні програми для K Desktop Environment 2.0. Містить: KWord
(текстовий процесор), KSpread (електронна таблиця), KPresenter
(презентації) та KChart (генератор діаграм).

%package devel
Summary:	KOffice - header files
Summary(es.UTF-8):   Header files for compiling applications that use koffice libraries
Summary(pl.UTF-8):   KOffice - pliki nagłówkowe
Summary(pt_BR.UTF-8):   Arquivos de inclusão necessários à compilação de aplicações que usem as bibliotecas do koffice
Group:		X11/Development/Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description devel
This package includes the header files you will need to compile
applications that use koffice libraries.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne przy kompilowaniu
programów używających bibliotek KOffice.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão necessários à compilação de aplicações que usem
as bibliotecas do koffice.

%package apidocs
Summary:	API documentation
Summary(pl.UTF-8):   Dokumentacja API
Group:		Development/Docs
Requires:	kdelibs >= 9:3.2.90

%description apidocs
API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API.

%package common
Summary:	KOffice - common files and libraries
Summary(pl.UTF-8):   KOffice - wspólne pliki i biblioteki
Summary(pt_BR.UTF-8):   Arquivos requeridos por todos os softwares koffice
Group:		X11/Applications
Requires:	kdebase-core >= 9:3.2.90

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

%description common -l pl.UTF-8
KOffice jest zintegrowanym pakietem biurowym dla środowiska KDE.
Pakiet między innymi zawiera:
- KWord - procesor tekstu
- KFormula - edytor równań
- KSpread - arkusz kalkulacyjny
- KPresenter - tworzenie prezentacji
- Kivio - aplikacja wzorowana na Visio(R)
- KChart - generator wykresów
- Kontour - grafika wektorowa
- Karbon - bazujący na pikselach program typu GIMP czy Adobe(c)
  Photoshop(R)
- Kugar - narzędzie do generowania raportów jakości biznesowej

Pakiet zawiera wspólne pliki i biblioteki wymagane przez aplikacje
KOffice.

%description common -l pt_BR.UTF-8
Arquivos requeridos por todos os softwares koffice.

%package karbon
Summary:	KOffice - Karbon
Summary(pl.UTF-8):   KOffice - Karbon
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
#karbon has changed its named (again) to curt therefore in the future:
Obsoletes:	koffice-krayon

%description karbon
Karbon is a vector graphics application within koffice.

%description karbon -l pl.UTF-8
Karbon to aplikacja koffice służąca do rysowania grafiki wektorowej,

%package kchart
Summary:	KOffice - KChart
Summary(pl.UTF-8):   KOffice - KChart
Summary(pt_BR.UTF-8):   Gerador de diagramas do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description kchart
KChart is KOffice part for generating diagrams from data, e.g. pie and
bar charts.

%description kchart -l pl.UTF-8
KChart jest aplikacją służącą do generowania wykresów.

%description kchart -l pt_BR.UTF-8
Gerador de diagramas do KOffice.

%package kexi
Summary:	KOffice - Kexi
Summary(pl.UTF-8):   KOffice - Kexi
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	libpqxx
Requires:	mysql-libs

%description kexi
Kexi is KOffice part for using database system such as mysql.

%description kexi -l pl.UTF-8
Kexi jest aplikacją służącą do korzystania systemów baz danych
takich jak mysql.

%package kformula
Summary:	KOffice - kformula
Summary(pl.UTF-8):   KOffice - kformula
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description kformula
KFormula is KOffice part for creating formulas, equations, etc...

%description kformula -l pl.UTF-8
KFormula jest aplikacją służącą do tworzenia wzorów, równań, itp.

%package kivio
Summary:	KOffice - kivio
Summary(pl.UTF-8):   KOffice - kivio
Summary(pt_BR.UTF-8):   Editor de fluxogramas do KOffice
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

%description kivio -l pl.UTF-8
Kivio jest programem typu flowcharting. Pod tym pojęciem jednak kryje
się znacznie więcej. Kivio dostarcza najpotrzebniejsze funkcje, ale
wszystkie obiekty można rozszerzać za pomocą języka skryptowego, a
system wtyczek backendowych oferuje możliwość tworzenia obiektów
dotyczących prawie wszystkiego. Kivio można nakarmić katalogiem plików
nagłówkowych C++ lub plików Javy i pozwolić wygenerować graficzną mapę
klas. Po podaniu sieci przejrzy ją i stworzy jej mapę. Wszystko to
jest możliwe poprzez architekturę skryptów i wtyczek Kivio.

%description kivio -l pt_BR.UTF-8
Editor de fluxogramas do KOffice.

#%package kplato
#Summary:	KOffice - kplato
#Summary(pl):	KOffice - kplato
#Group:		X11/Applications
#Requires:	%{name}-common = %{epoch}:%{version}-%{release}

#%description kplato
#TODO.

#%description kplato -l pl
#TODO.

%package kpresenter
Summary:	KOffice - KPresenter
Summary(pl.UTF-8):   KOffice - KPresenter
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description kpresenter
KPresenter is a presentation application of the KOffice, similar to MS
PowerPoint in the windows world. You can use it for doing screen
presentations or transparencies.

%description kpresenter -l pl.UTF-8
KPresenter jest aplikacją KOffice do tworzenia prezentacji, podobną do
MS PowerPoint. Możesz użyć jej do tworzenia wizualnych prezentacji.

%package krita
Summary:	KOffice - Krita
Summary(pl.UTF-8):   KOffice - Krita
Summary(pt_BR.UTF-8):   Ferramenta de desenho vetorial do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Obsoletes:	koffice-killustrator

%description krita
Krita is the vector drawing program for the K Desktop Environment.
The aim of the Kontour project is the development of a freely
available vector-based drawing application similar to Corel Draw or
Adobe Illustrator.
Krita was formerly known as KIllustrator but due to blackmail made
by Adobe lawyers it has to be renamed.

%description krita -l pl.UTF-8
Krita jest programem do tworzenia grafiki wektorowej dla środowiska
KDE. Celem przyświecającym programistom jest stworzenie w pełni
funkcjonalnego programu do grafiki wektorowej podobnego do Corel Draw
lub Adobe Illustrator.

Krita wczesniej był znany jako KIlustrator ale developerzy zostali
zmuszeni szantażem przez prawników Adobe do zmiany nazwy.

%description krita -l pt_BR.UTF-8
Ferramenta de desenho vetorial do KOffice.

%package kspread
Summary:	KOffice - KSpread
Summary(pl.UTF-8):   KOffice - KSpread
Summary(pt_BR.UTF-8):   Planilha eletrônica do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description kspread
KSpread is the spread sheet of the KOffice, similar to MS Excel.

%description kspread -l pl.UTF-8
KSpread jest arkuszem kalkulacyjnym, podobnym do MS Excel.

%description kspread -l pt_BR.UTF-8
Planilha eletrônica do KOffice.

%package kugar
Summary:	KOffice - KUgar
Summary(pl.UTF-8):   KOffice - KUgar
Summary(pt_BR.UTF-8):   Gerador de relatórios do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description kugar
Kugar is a KDE tool for generating business quality reports which can
be viewed and printed. It includes a standalone report application can
embed the report viewing functionality and that reports can be viewed
using the Konqueror browser.

%description kugar -l pl.UTF-8
Kugar jest narzędziem KDE do generowania raportów o jakości
biznesowej, które mogą być przeglądane oraz drukowane. Dodatkowo
dołączony jest program który może być dołączony do raportu
umożliwiając oglądanie raportu w przeglądarce Konqueror.

%description kugar -l pt_BR.UTF-8
Gerador de relatórios do KOffice.

%package kword
Summary:	KOffice - KWord
Summary(pl.UTF-8):   KOffice - KWord
Summary(pt_BR.UTF-8):   Processador de texto do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description kword
KWord is a FrameMaker-like wordprocessor application for KOffice. So
it can be used for DTP, but also for "normal" wordprocessing (like
writing letters, reports, etc.).

%description kword -l pl.UTF-8
KWord jest ramkowym procesorem tekstu. Może być użyty do DTP, ale
również do zwykłej edycji tekstu (jak pisanie listów, raportów, itp.).

%description kword -l pt_BR.UTF-8
Processador de texto do KOffice.

%prep
%setup -q
%patch0 -p1

for f in `find . -name *.desktop`; do
    %{__sed} -i -e 's/Terminal=0/Terminal=false/' \
    -e 's/Terminal=1/Terminal=true/' $f
done    

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;X-Misc;/' \
	tools/kthesaurus/KThesaurus.desktop \
	kchart/kchart.desktop \
	kformula/kformula.desktop \
	kivio/kiviopart/kivio.desktop \
	kugar/kudesigner/kudesigner.desktop \
	kugar/part/kugar.desktop \
	kexi/formeditor/test/kformdesigner.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Graphics;/' \
	karbon/data/karbon.desktop \
	krita/krita.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;Database;/' \
	kexi/kexi.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;Presentation;/' \
	kpresenter/kpresenter.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;Spreadsheet;/' \
	kspread/kspread.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;WordProcessor;/' \
	kword/kword.desktop
for f in `find . -name \*.desktop`; do
	if grep -q '^Categories=.*[^;]$' $f; then
		sed -i -e 's/\(^Categories=.*$\)/\1;/' $f
	fi
done

#echo "KDE_OPTIONS = nofinal" >> kplato/Makefile.am

%build
cp /usr/share/automake/config.sub admin

#export PATH=/usr/share/unsermake:$PATH

%{__make} -f admin/Makefile.common cvs

#export DO_NOT_COMPILE="$DO_NOT_COMPILE kdgantt"

%configure \
	--disable-rpath \
	--enable-final \
	--with-pgsqllibdir=%{_libdir} \
	--with-pqxxlibdir=%{_libdir} \
	--with-qt-libraries=%{_libdir}

#%%{__make} -C kword/mailmerge/sql qtsqlopenwidget.h

%{__make}

%{?with_apidocs:%{__make} apidox}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT{%{_desktopdir}/kde,%{_mandir}/man1}

mv $RPM_BUILD_ROOT{%{_datadir}/applnk/{Office,Utilities}/*,%{_desktopdir}/kde}

install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%find_lang kchart	--with-kde
#%find_lang kexi		--with-kde
%find_lang kformula	--with-kde
%find_lang kivio	--with-kde
%find_lang koffice	--with-kde
%find_lang koshell	--with-kde
cat koshell.lang >> koffice.lang
%find_lang kpresenter	--with-kde
#%find_lang krita	--with-kde
%find_lang kspread	--with-kde
%find_lang kugar	--with-kde
%find_lang kword	--with-kde
%find_lang thesaurus	--with-kde
cat thesaurus.lang >> kword.lang

# Omit apidocs entries
sed -i 's/.*apidocs.*//' *.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	common -p /sbin/ldconfig
%postun common -p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%{_libdir}/libkarbonbase.so
%{_libdir}/libkarboncommon.so
%{_libdir}/libkdchart.so
%{_libdir}/libkchartcommon.so
%{_libdir}/libkexicore.so
%{_libdir}/libkexidatatable.so
%{_libdir}/libkexidb.so
%{_libdir}/libkexidbparser.so
%{_libdir}/libkexiextendedwidgets.so
%{_libdir}/libkexiformutils.so
%{_libdir}/libkexiguiutils.so
%{_libdir}/libkeximain.so
%{_libdir}/libkeximigrate.so
%{_libdir}/libkexipropertyeditor.so
%{_libdir}/libkexirelationsview.so
%{_libdir}/libkexisql2.so
%{_libdir}/libkexisql3.so
#%{_libdir}/libkexiutils.so
%{_libdir}/libkformdesigner.so
%{_libdir}/libkformulalib.so
%{_libdir}/libkiviocommon.so
%{_libdir}/libkochart.so
%{_libdir}/libkofficecore.so
%{_libdir}/libkofficeui.so
%{_libdir}/libkopainter.so
#%{_libdir}/libkoproperty.so
%{_libdir}/libkoscript.so
%{_libdir}/libkotext.so
%{_libdir}/libkowmf.so
%{_libdir}/libkritacommon.so
%{_libdir}/libkspreadcommon.so
%{_libdir}/libkstore.so
%{_libdir}/libkugarlib.so
%{_libdir}/libkwmailmerge_interface.so
%{_libdir}/libkwmf.so
%{_libdir}/libkwordexportfilters.so
%{_includedir}/*.h
%{_includedir}/kexidb
#%{_includedir}/kexiutils
%{_includedir}/kword

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_kdedocdir}/en/%{name}-apidocs
%endif

%files common
# -f koffice.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/koconverter
%attr(755,root,root) %{_bindir}/koscript
%attr(755,root,root) %{_bindir}/koshell
%{_libdir}/libkarbonbase.la
%attr(755,root,root) %{_libdir}/libkarbonbase.so.*.*.*
%{_libdir}/libkarboncommon.la
%attr(755,root,root) %{_libdir}/libkarboncommon.so.*.*.*
%{_libdir}/libkchartcommon.la
%attr(755,root,root) %{_libdir}/libkchartcommon.so.*.*.*
%{_libdir}/libkdchart.la
%attr(755,root,root) %{_libdir}/libkdchart.so.*.*.*
%{_libdir}/libkdeinit_koshell.la
%attr(755,root,root) %{_libdir}/libkdeinit_koshell.so
%{_libdir}/libkexicore.la
%attr(755,root,root) %{_libdir}/libkexicore.so.*.*.*
%{_libdir}/libkexidatatable.la
%attr(755,root,root) %{_libdir}/libkexidatatable.so.*.*.*
%{_libdir}/libkexidb.la
%attr(755,root,root) %{_libdir}/libkexidb.so.*.*.*
%{_libdir}/libkexidbparser.la
%attr(755,root,root) %{_libdir}/libkexidbparser.so.*.*.*
%{_libdir}/libkexiextendedwidgets.la
%attr(755,root,root) %{_libdir}/libkexiextendedwidgets.so.*.*.*
%{_libdir}/libkexiformutils.la
%attr(755,root,root)  %{_libdir}/libkexiformutils.so.*.*.*
%{_libdir}/libkexiguiutils.la
%attr(755,root,root) %{_libdir}/libkexiguiutils.so.*.*.*
%{_libdir}/libkeximain.la
%attr(755,root,root) %{_libdir}/libkeximain.so.*.*.*
%{_libdir}/libkeximigrate.la
%attr(755,root,root) %{_libdir}/libkeximigrate.so.*.*.*
%{_libdir}/libkexipropertyeditor.la
%attr(755,root,root) %{_libdir}/libkexipropertyeditor.so.*.*.*
%{_libdir}/libkexirelationsview.la
%attr(755,root,root) %{_libdir}/libkexirelationsview.so.*.*.*
%{_libdir}/libkexisql2.la
%attr(755,root,root) %{_libdir}/libkexisql2.so.*.*.*
%{_libdir}/libkexisql3.la
%attr(755,root,root) %{_libdir}/libkexisql3.so.*.*.*
#%{_libdir}/libkexiutils.la
#%attr(755,root,root) %{_libdir}/libkexiutils.so.*.*.*
%{_libdir}/libkformdesigner.la
%attr(755,root,root) %{_libdir}/libkformdesigner.so.*.*.*
%{_libdir}/libkformulalib.la
%attr(755,root,root) %{_libdir}/libkformulalib.so.*.*.*
%{_libdir}/libkiviocommon.la
%attr(755,root,root) %{_libdir}/libkiviocommon.so.*.*.*
%{_libdir}/libkochart.la
%attr(755,root,root) %{_libdir}/libkochart.so.*.*.*
%{_libdir}/libkofficecore.la
%attr(755,root,root) %{_libdir}/libkofficecore.so.*.*.*
%{_libdir}/libkofficeui.la
%attr(755,root,root) %{_libdir}/libkofficeui.so.*.*.*
%{_libdir}/libkopainter.la
%attr(755,root,root) %{_libdir}/libkopainter.so.*.*.*
#%{_libdir}/libkoproperty.la
#%attr(755,root,root) %{_libdir}/libkoproperty.so.*.*.*
%{_libdir}/libkoscript.la
%attr(755,root,root) %{_libdir}/libkoscript.so.*.*.*
%{_libdir}/libkotext.la
%attr(755,root,root) %{_libdir}/libkotext.so.*.*.*
%{_libdir}/libkowmf.la
%attr(755,root,root) %{_libdir}/libkowmf.so.*.*.*
%{_libdir}/libkritacommon.la
%attr(755,root,root) %{_libdir}/libkritacommon.so.*.*.*
%{_libdir}/libkspreadcommon.la
%attr(755,root,root) %{_libdir}/libkspreadcommon.so.*.*.*
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
#%{_libdir}/kde3/kfile_abiword.la
#%attr(755,root,root) %{_libdir}/kde3/kfile_abiword.so
#%{_libdir}/kde3/kfile_gnumeric.la
#%attr(755,root,root) %{_libdir}/kde3/kfile_gnumeric.so
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
%{_datadir}/servicetypes/*
%{_datadir}/apps/koffice
%{_datadir}/apps/koshell
%{_datadir}/config.kcfg/koshell.kcfg
%{_datadir}/services/clipartthumbnail.desktop
#%{_datadir}/services/kfile_abiword.desktop
#%{_datadir}/services/kfile_gnumeric.desktop
%{_datadir}/services/kfile_koffice.desktop
%{_datadir}/services/kfile_ooo.desktop
%{_datadir}/services/kodocinfopropspage.desktop
%{_datadir}/services/kofficethumbnail.desktop
%{_datadir}/services/kounavail.desktop
%{_datadir}/services/ole_*.desktop
%{_datadir}/services/xslt_*.desktop
%{_datadir}/services/generic_filter.desktop
%dir %{_datadir}/templates/.source
%{_desktopdir}/kde/koshell.desktop
%{_iconsdir}/*/*/apps/koshell.*
%{_mandir}/man1/koconverter.1*
%{_mandir}/man1/koscript.1*
%{_mandir}/man1/koshell.1*

%files karbon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karbon
%{_libdir}/libkdeinit_karbon.la
%attr(755,root,root) %{_libdir}/libkdeinit_karbon.so
%{_libdir}/kde3/*karbon*.la
%attr(755,root,root) %{_libdir}/kde3/*karbon*.so*
%{_libdir}/kde3/*wmf*port.la
%attr(755,root,root) %{_libdir}/kde3/*wmf*port.so*
%{_datadir}/apps/karbon
%{_datadir}/apps/konqueror/servicemenus/karbon_konqi.desktop
%{_datadir}/services/karbon*
%{_datadir}/templates/.source/Illustration.karbon
%{_desktopdir}/kde/karbon.desktop
%{_iconsdir}/*/*/apps/karbon.*
%{_mandir}/man1/karbon.1*

%files kchart -f kchart.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kchart
%{_libdir}/libkdeinit_kchart.la
%attr(755,root,root) %{_libdir}/libkdeinit_kchart.so
%{_libdir}/kde3/kchart.la
%attr(755,root,root) %{_libdir}/kde3/kchart.so
%{_libdir}/kde3/libkchartpart.la
%attr(755,root,root) %{_libdir}/kde3/libkchartpart.so
%{_libdir}/kde3/libkchartpngexport.la
%attr(755,root,root) %{_libdir}/kde3/libkchartpngexport.so
%{_libdir}/kde3/libkchartsvgexport.la
%attr(755,root,root) %{_libdir}/kde3/libkchartsvgexport.so
#%{_libdir}/kde3/libkptchart.la
#%attr(755,root,root) %{_libdir}/kde3/libkptchart.so
%{_datadir}/apps/kchart
#%{_datadir}/apps/konqueror/servicemenus/kchart_konqi.desktop
%{_datadir}/services/kchartpart.desktop
%{_datadir}/services/kchart_png_export.desktop
%{_datadir}/services/kchart_svg_export.desktop
%{_desktopdir}/kde/kchart.desktop
%{_iconsdir}/*/*x*/apps/kchart.png
%{_mandir}/man1/kchart.1*

%files kexi
# -f kexi.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kexi*
%attr(755,root,root) %{_bindir}/ksqlite
%attr(755,root,root) %{_bindir}/ksqlite2
%attr(755,root,root) %{_bindir}/ksqlite2to3
%{_libdir}/libkdeinit_kexi.la
%attr(755,root,root) %{_libdir}/libkdeinit_kexi.so
%{_libdir}/kde3/kexi.la
%attr(755,root,root) %{_libdir}/kde3/kexi.so
%{_libdir}/kde3/kexidb_mysqldriver.la
%attr(755,root,root) %{_libdir}/kde3/kexidb_mysqldriver.so
%{_libdir}/kde3/kexidb_pqxxsqldriver.la
%attr(755,root,root) %{_libdir}/kde3/kexidb_pqxxsqldriver.so
%{_libdir}/kde3/kexidb_sqlite2driver.la
%attr(755,root,root) %{_libdir}/kde3/kexidb_sqlite2driver.so
%{_libdir}/kde3/kexidb_sqlite3driver.la
%attr(755,root,root) %{_libdir}/kde3/kexidb_sqlite3driver.so
%{_libdir}/kde3/kexidbwidgets.la
%attr(755,root,root) %{_libdir}/kde3/kexidbwidgets.so
#%{_libdir}/kde3/kexihandler_csv_import.la
#%attr(755,root,root) %{_libdir}/kde3/kexihandler_csv_import.so
%{_libdir}/kde3/kexihandler_form.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_form.so
%{_libdir}/kde3/kexihandler_migration.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_migration.so
%{_libdir}/kde3/kexihandler_query.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_query.so
%{_libdir}/kde3/kexihandler_relation.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_relation.so
%{_libdir}/kde3/kexihandler_script.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_script.so
%{_libdir}/kde3/kexihandler_table.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_table.so
%{_libdir}/kde3/keximigrate_mysql.la
%attr(755,root,root) %{_libdir}/kde3/keximigrate_mysql.so
%{_libdir}/kde3/keximigrate_pqxx.la
%attr(755,root,root) %{_libdir}/kde3/keximigrate_pqxx.so
%{_datadir}/apps/kexi
%{_datadir}/apps/konqueror/servicemenus/kexi_konqi.desktop
%{_datadir}/config/kexirc
%{_datadir}/config/magic/kexi.magic
%{_datadir}/mimelnk/application/x-kexiproject-shortcut.desktop
%{_datadir}/mimelnk/application/x-kexiproject-sqlite.desktop
%{_datadir}/services/kexi*
%{_desktopdir}/kde/kexi.desktop
%{_iconsdir}/*/*/apps/kexi.*
%{_iconsdir}/crystalsvg/32x32/mimetypes/kexiproject_shortcut.png
%{_iconsdir}/crystalsvg/32x32/mimetypes/kexiproject_sqlite.png
# Separate?
%attr(755,root,root) %{_bindir}/kformdesigner
%{_libdir}/kde3/containers.la
%attr(755,root,root) %{_libdir}/kde3/containers.so
%{_libdir}/kde3/stdwidgets.la
%attr(755,root,root) %{_libdir}/kde3/stdwidgets.so
%{_datadir}/apps/kformdesigner
%{_datadir}/apps/kformdesigner_part/kformdesigner_part.rc
%{_datadir}/apps/kformdesigner_part/kformdesigner_part_shell.rc
%dir %{_datadir}/services/kformdesigner/
%{_datadir}/services/kformdesigner/containerfactory.desktop
%{_datadir}/services/kformdesigner/kexidbfactory.desktop
%{_datadir}/services/kformdesigner/stdwidgets.desktop
%{_datadir}/services/kformdesigner_part.desktop
%{_desktopdir}/kde/kformdesigner.desktop
%{_datadir}/mimelnk/application/x-kexiproject-sqlite2.desktop
%{_datadir}/mimelnk/application/x-kexiproject-sqlite3.desktop
%{_iconsdir}/crystalsvg/16x16/mimetypes/kexiproject_sqlite.png
%{_iconsdir}/crystalsvg/16x16/mimetypes/kexiproject_sqlite2.png
%{_iconsdir}/crystalsvg/32x32/mimetypes/kexiproject_sqlite2.png

%files kformula
# -f kformula.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kformula
%{_libdir}/libkdeinit_kformula.la
%attr(755,root,root) %{_libdir}/libkdeinit_kformula.so
%{_libdir}/kde3/kformula.la
%attr(755,root,root) %{_libdir}/kde3/kformula.so
%{_libdir}/kde3/libkfo*.la
%attr(755,root,root) %{_libdir}/kde3/libkfo*.so
%{_datadir}/apps/kformula
%{_datadir}/apps/konqueror/servicemenus/kformula_konqi.desktop
%{_datadir}/services/kformula*
%{_desktopdir}/kde/kformula.desktop
%{_iconsdir}/*/*/actions/abs.png
%{_iconsdir}/*/*/actions/brac*.png
%{_iconsdir}/*/*/actions/frac.png
%{_iconsdir}/*/*/actions/ins*.png
%{_iconsdir}/*/*/actions/rem*.png
%{_iconsdir}/*/*/actions/int.png
%{_iconsdir}/*/*/actions/gsub.png
%{_iconsdir}/*/*/actions/gsup.png
%{_iconsdir}/*/*/actions/lsub.png
%{_iconsdir}/*/*/actions/lsup.png
%{_iconsdir}/*/*/actions/rsub.png
%{_iconsdir}/*/*/actions/rsup.png
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
%{_mandir}/man1/kformula.1*

%files kivio 
#-f kivio.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kivio
%{_libdir}/*kivio*.la
%attr(755,root,root) %{_libdir}/*kivio*.so
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
%{_mandir}/man1/kivio.1*

#%files kplato
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kplato
#%{_libdir}/libkdeinit_kplato.la
#%attr(755,root,root) %{_libdir}/libkdeinit_kplato.so
#%{_libdir}/kde3/kplato.la
#%attr(755,root,root) %{_libdir}/kde3/kplato.so
#%{_libdir}/kde3/libkplatopart.la
#%attr(755,root,root) %{_libdir}/kde3/libkplatopart.so
#%{_datadir}/apps/kplato
#%{_datadir}/services/kplatopart.desktop
#%{_desktopdir}/kde/kplato.desktop
#%{_iconsdir}/*/*/apps/kplato.*

%files kpresenter
# -f kpresenter.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpresenter
%attr(755,root,root) %{_bindir}/kprconverter.pl
%{_libdir}/libkdeinit_kpresenter.la
%attr(755,root,root) %{_libdir}/libkdeinit_kpresenter.so
%{_libdir}/kde3/kpresenter.la
%attr(755,root,root) %{_libdir}/kde3/kpresenter.so
%{_libdir}/kde3/libkpresenterpart.la
%attr(755,root,root) %{_libdir}/kde3/libkpresenterpart.so
%{_libdir}/kde3/libkprkword.la
%attr(755,root,root) %{_libdir}/kde3/libkprkword.so
%{_libdir}/kde3/libooimpress*port.la
%attr(755,root,root) %{_libdir}/kde3/libooimpress*port.so
%{_datadir}/apps/konqueror/servicemenus/kpresenter_konqi.desktop
%{_datadir}/apps/kpresenter
%{_datadir}/templates/.source/Presentation.kpt
%{_datadir}/templates/Presentation.desktop
%{_datadir}/services/kprkword.desktop
%{_datadir}/services/kpresenter_ooimpress_export.desktop
%{_datadir}/services/kpresenter_ooimpress_import.desktop
%{_datadir}/services/kpresenterpart.desktop
%{_desktopdir}/kde/kpresenter.desktop
%{_iconsdir}/*/*/apps/kpresenter*.png
%{_mandir}/man1/kpresenter.1*
%{_mandir}/man1/kprconverter.pl.1*

%files krita
# -f krita.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krita
%{_libdir}/kde3/*krita*.la
%attr(755,root,root) %{_libdir}/kde3/*krita*.so
%{_libdir}/*krita*.la
%attr(755,root,root) %{_libdir}/*krita*.so
%{_datadir}/apps/konqueror/servicemenus/krita_konqi.desktop
%{_datadir}/apps/krita
%{_datadir}/services/krita_magick_export.desktop
%{_datadir}/services/krita_magick_import.desktop
#%{_datadir}/services/krita_rgb_u16_plugin.desktop
#%{_datadir}/services/kritacmykplugin.desktop
%{_datadir}/services/kritadefaulttools.desktop
%{_datadir}/services/kritagrayplugin.desktop
%{_datadir}/services/kritapart.desktop
%{_datadir}/services/kritargbplugin.desktop
%{_datadir}/services/kritacimg.desktop
%{_datadir}/services/kritadefaultpaintops.desktop
#%{_datadir}/services/kritamagick.desktop
%{_datadir}/services/kritaselectiontools.desktop
#%{_datadir}/services/kritatestcsplugin.desktop
%{_datadir}/services/kritatoolcrop.desktop
%{_datadir}/services/kritatoolfilter.desktop
%{_datadir}/services/kritatoolpolygon.desktop
%{_datadir}/services/kritatoolpolyline.desktop
%{_datadir}/services/kritatoolselectpicker.desktop
%{_datadir}/services/kritatoolstar.desktop
%{_datadir}/services/kritatooltransform.desktop
#%{_datadir}/services/kritawetplugin.desktop
#%{_datadir}/services/kritawsbrushpaintop.desktop
#%{_datadir}/services/kritawsplugin.desktop
%{_datadir}/templates/Illustration.desktop
%{_desktopdir}/kde/krita.desktop
%{_iconsdir}/*/*/*/krita.png

%files kspread
# -f kspread.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kspread
%{_libdir}/libkdeinit_kspread.la
%attr(755,root,root) %{_libdir}/libkdeinit_kspread.so
%{_libdir}/kde3/kspread.la
%attr(755,root,root) %{_libdir}/kde3/kspread.so
%{_libdir}/kde3/libkspread*.la
%attr(755,root,root) %{_libdir}/kde3/libkspread*.so
%{_libdir}/kde3/libcsv*.la
%attr(755,root,root) %{_libdir}/kde3/libcsv*.so
%{_libdir}/kde3/libapplixspreadimport.la
%attr(755,root,root) %{_libdir}/kde3/libapplixspreadimport.so
%{_libdir}/kde3/libgnumeric*port.la
%attr(755,root,root) %{_libdir}/kde3/libgnumeric*port.so
%{_libdir}/kde3/libdbase*port.la
%attr(755,root,root) %{_libdir}/kde3/libdbase*port.so
%{_libdir}/kde3/libqproimport.la
%attr(755,root,root) %{_libdir}/kde3/libqproimport.so
%{_libdir}/kde3/libopencalc*port.la
%attr(755,root,root) %{_libdir}/kde3/libopencalc*port.so
%{_libdir}/kde3/libexcelimport.la
%attr(755,root,root) %{_libdir}/kde3/libexcelimport.so
%{_datadir}/apps/kspread
%{_datadir}/services/kspread*.desktop
%{_datadir}/services/kwmailmerge_kspread.desktop
%{_datadir}/templates/.source/SpreadSheet.kst
%{_datadir}/templates/SpreadSheet.desktop
%{_desktopdir}/kde/kspread.desktop
%{_iconsdir}/[!l]*/*/apps/kspread*.png
%{_mandir}/man1/kspread.1*

%files kugar
# -f kugar.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kudesigner
%attr(755,root,root) %{_bindir}/kugar
%{_libdir}/kde3/*kugar*.la
%attr(755,root,root) %{_libdir}/kde3/*kugar*.so
%{_libdir}/*kugar*.la
%attr(755,root,root) %{_libdir}/*kugar*.so
%{_libdir}/kde3/*kudesigner*.la
%attr(755,root,root) %{_libdir}/kde3/*kudesigner*.so
%{_libdir}/*kudesigner*.la
%attr(755,root,root) %{_libdir}/*kudesigner*.so
%{_desktopdir}/kde/kudesigner.desktop
%{_desktopdir}/kde/kugar.desktop
%{_datadir}/apps/konqueror/servicemenus/kspread_konqi.desktop
%{_datadir}/apps/kudesigner
%{_datadir}/apps/kugar
%{_datadir}/services/kugar_kugar_import.desktop
%{_datadir}/services/kugarpart.desktop
%{_iconsdir}/*/*/*/kudesigner.png
%{_iconsdir}/*/*/*/kugar.png
%{_iconsdir}/*/*/mimetypes/kugardata.png
%{_mandir}/man1/kudesigner.1*
%{_mandir}/man1/kugar.1*

%files kword
# -f kword.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kthesaurus
%attr(755,root,root) %{_bindir}/kword
%{_libdir}/libkdeinit_kthesaurus.la
%attr(755,root,root) %{_libdir}/libkdeinit_kthesaurus.so
%{_libdir}/libkdeinit_kword.la
%attr(755,root,root) %{_libdir}/libkdeinit_kword.so
%{_libdir}/kde3/kword.la
%attr(755,root,root) %{_libdir}/kde3/kword.so
%{_libdir}/libkwmailmerge*.la
%attr(755,root,root) %{_libdir}/libkwmailmerge*.so
%{_libdir}/libkword*export*.la
%attr(755,root,root) %{_libdir}/libkword*export*.so
%{_libdir}/kde3/kthesaurus.la
%attr(755,root,root) %{_libdir}/kde3/kthesaurus.so
%{_libdir}/kde3/kwmailmerge*.la
%attr(755,root,root) %{_libdir}/kde3/kwmailmerge*.so
%{_libdir}/kde3/libabiword*port.la
%attr(755,root,root) %{_libdir}/kde3/libabiword*port.so
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
%{_datadir}/apps/konqueror/servicemenus/kword_konqi.desktop
%{_datadir}/apps/kword
%{_datadir}/apps/thesaurus
%{_datadir}/apps/xsltfilter/export/kword/xslfo/*.xsl
%{_datadir}/services/kwmailmerge_kabc.desktop
%{_datadir}/services/kword*.desktop
%{_datadir}/services/kwserialletter*
%{_datadir}/services/thesaurustool.desktop
%{_datadir}/templates/.source/TextDocument.kwt
%{_datadir}/templates/TextDocument.desktop
%{_desktopdir}/kde/KThesaurus.desktop
%{_desktopdir}/kde/kword.desktop
%{_iconsdir}/*/*/apps/kword.png
%{_mandir}/man1/kthesaurus.1*
%{_mandir}/man1/kword.1*
