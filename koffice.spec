#
# Conditional build:
%bcond_without  apidocs # do not prepare API documentation
%bcond_with	i18n	# disable i18n (26MB less to download)
#
%define		_state		snapshots
%define		_ver		1.3
%define		_snap		040510
%define		artsver		13:1.2.0
%define		_packager	adgor	

Summary:	KOffice - powerful office suite for KDE
Summary(pl):	KOffice - potê¿ny pakiet biurowy dla KDE
Summary(pt_BR):	Suíte de aplicativos office para o KDE
Summary(ru):	îÁÂÏÒ ÏÆÆÉÓÎÙÈ ÐÒÏÇÒÁÍÍ ÄÌÑ KDE
Summary(uk):	îÁÂ¦Ò ÏÆ¦ÓÎÉÈ ÐÒÏÇÒÁÍ ÄÌÑ KDE
Summary(zh_CN):	KDE µÄ°ì¹«Ó¦ÓÃÈí¼þ¼¯¡£
Name:		koffice
Version:	%{_ver}.%{_snap}
Release:	0.1
Epoch:		5
License:	GPL/LGPL
Group:		X11/Applications
Source0:	%{name}.tar.bz2
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{version}/src/%{name}-%{version}.tar.bz2
Source0:	http://ep09.pld-linux.org/~%{_packager}/kde/%{name}-%{_snap}.tar.bz2
##%% Source0-md5:	8e4c9db57f701d42f21d61651f0b03bd
#Source1:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{version}/src/%{name}-i18n-%{version}.tar.bz2
##%% Source1-md5:	ca89c9c944508de11ca2908eb0a851e4
Patch0:		%{name}-vcategories.patch
Patch1:		kde-common-QTDOCDIR.patch
Patch2:		%{name}-gcc34.patch
URL:		http://www.koffice.org/
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	arts-qt-devel >= %{artsver}
BuildRequires:	aspell-devel >= 0.50.2
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.2.90
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	mysql-devel
BuildRequires:	perl-base
BuildRequires:	python-devel >= 2.2
%{?with_apidocs:BuildRequires:  qt-doc}
BuildRequires:	rpmbuild(macros) >= 1.129
#BuildRequires:	wv2-devel >= 0.0.7
BuildRequires:	zlib-devel
#Requires:	wv2 >= 0.0.7
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

%package apidocs
Summary:	API documentation
Summary(pl):	Dokumentacja API
Group:		Development/Docs
Requires:	kdelibs >= 9:3.2.90

%description apidocs
API documentation.

%description apidocs -l pl
Dokumentacja API.

%package common
Summary:	KOffice - common files and libraries
Summary(pl):	KOffice - wspólne pliki i biblioteki
Summary(pt_BR):	Arquivos requeridos por todos os softwares koffice
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
#karbon has changed its named (again) to curt therefore in the future:
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
Requires:	mysql-libs

%description kexi
Kexi is KOffice part for using database system such as mysql.

%description kexi -l pl
Kexi jest aplikacj± s³u¿±c± do korzystania systemów baz danych
takich jak mysql.

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

%package krita
Summary:	KOffice - Krita
Summary(pl):	KOffice - Krita
Summary(pt_BR):	Ferramenta de desenho vetorial do KOffice
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

%description krita -l pl
Krita jest programem do tworzenia grafiki wektorowej dla ¶rodowiska
KDE. Celem przy¶wiecaj±cym programistom jest stworzenie w pe³ni
funkcjonalnego programu do grafiki wektorowej podobnego do Corel Draw
lub Adobe Illustrator.

Krita wczesniej by³ znany jako KIlustrator ale developerzy zostali
zmuszeni szanta¿em przez prawników Adobe do zmiany nazwy.

%description krita -l pt_BR
Ferramenta de desenho vetorial do KOffice.

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

%package common-i18n
Summary:	Internationalization and localization files for koffice-common
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla koffice-common
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:3.2

%description common-i18n
Internationalization and localization files for koffice-common.

%description common-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla koffice-common.

%package karbon-i18n
Summary:	Internationalization and localization files for karbon
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla karbona
Group:		X11/Applications
Requires:	%{name}-karbon = %{epoch}:%{version}-%{release}
Requires:	%{name}-common-i18n = %{epoch}:%{version}-%{release}

%description karbon-i18n
Internationalization and localization files for karbon.

%description karbon-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla karbon.

%package kchart-i18n
Summary:	Internationalization and localization files for kchart
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcharta
Group:		X11/Applications
Requires:	%{name}-kchart = %{epoch}:%{version}-%{release}
Requires:	%{name}-common-i18n = %{epoch}:%{version}-%{release}

%description kchart-i18n
Internationalization and localization files for kchart.

%description kchart-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcharta.

%package kformula-i18n
Summary:	Internationalization and localization files for kformula
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kformuli
Group:		X11/Applications
Requires:	%{name}-kformula = %{epoch}:%{version}-%{release}
Requires:	%{name}-common-i18n = %{epoch}:%{version}-%{release}

%description kformula-i18n
Internationalization and localization files for kformula.

%description kformula-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kformuli.

%package kivio-i18n
Summary:	Internationalization and localization files for kivio
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kivio
Group:		X11/Applications
Requires:	%{name}-kivio = %{epoch}:%{version}-%{release}
Requires:	%{name}-common-i18n = %{epoch}:%{version}-%{release}

%description kivio-i18n
Internationalization and localization files for kivio.

%description kivio-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kivio.

%package kpresenter-i18n
Summary:	Internationalization and localization files for kpresenter
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpresentera
Group:		X11/Applications
Requires:	%{name}-kpresenter = %{epoch}:%{version}-%{release}
Requires:	%{name}-common-i18n = %{epoch}:%{version}-%{release}

%description kpresenter-i18n
Internationalization and localization files for kpresenter.

%description kpresenter-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpresentera.

%package kspread-i18n
Summary:	Internationalization and localization files for kspread
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kspreada
Group:		X11/Applications
Requires:	%{name}-kspread = %{epoch}:%{version}-%{release}
Requires:	%{name}-common-i18n = %{epoch}:%{version}-%{release}

%description kspread-i18n
Internationalization and localization files for kspread.

%description kspread-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kspreada.

%package kugar-i18n
Summary:	Internationalization and localization files for kugar
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kugara
Group:		X11/Applications
Requires:	%{name}-kugar = %{epoch}:%{version}-%{release}
Requires:	%{name}-common-i18n = %{epoch}:%{version}-%{release}

%description kugar-i18n
Internationalization and localization files for kugar.

%description kugar-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kugara.

%package kword-i18n
Summary:	Internationalization and localization files for kword
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kworda
Group:		X11/Applications
Requires:	%{name}-kword = %{epoch}:%{version}-%{release}
Requires:	%{name}-common-i18n = %{epoch}:%{version}-%{release}

%description kword-i18n
Internationalization and localization files for kword.

%description kword-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kworda.

%prep
%if %{with i18n}
%setup -q -a1
%else
%setup -q -n %{name}-%{_snap}
%endif
%patch0 -p1
%patch1 -p1
%patch2 -p1

echo "KDE_OPTIONS = nofinal" >> kexi/kexidb/parser/Makefile.am

%build
cp /usr/share/automake/config.sub admin

export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

export DO_NOT_COMPILE="$DO_NOT_COMPILE kdgantt"

%configure \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir}

%{__make}

%{?with_apidocs:%{__make} apidox}

%if %{with i18n}
cd %{name}-i18n-%{version}
%configure
%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# Workaround for doc caches (unsermake bug?)
cd doc
for i in `find . -name index.cache.bz2`; do
	install -c -p -m 644 $i $RPM_BUILD_ROOT%{_kdedocdir}/en/$i
done
cd -	 

install -d $RPM_BUILD_ROOT{%{_desktopdir}/kde,%{_mandir}/man1}

mv $RPM_BUILD_ROOT{%{_datadir}/applnk/Office/*,%{_desktopdir}/kde}

install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%if %{with i18n}
cd %{name}-i18n-%{version}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}
cd ..
%endif

%find_lang kchart	--with-kde
%find_lang kformula	--with-kde
%find_lang kivio	--with-kde
%find_lang koffice	--with-kde
%find_lang koshell	--with-kde
cat koshell.lang >> koffice.lang
%find_lang kugar	--with-kde
%find_lang kpresenter	--with-kde
%find_lang kspread	--with-kde
%find_lang kword	--with-kde
%find_lang thesaurus	--with-kde
cat thesaurus.lang >> kword.lang

%if %{with i18n}
plikez="\
	desktop_koffice \
	xsltexportfilter \
	kfile_koffice \
	kfile_ooo \
	koconverter \
	kocryptfilter \
	kounavail \
	kscan_plugin \
	xsltimportfilter \
	xsltfilter"

for i in $plikez; do
	%find_lang $i --with-kde
	cat ${i}.lang >> koffice.lang
done

%find_lang karbon		--with-kde
%find_lang karbonepsfilter	--with-kde
cat karbonepsfilter.lang >> karbon.lang
%find_lang kudesigner		--with-kde
cat kudesigner.lang >> karbon.lang

kform="\
	kformulalatexfilter \
	kformulamathmlfilter \
	kformulapngfilter"

for i in $kform; do
	%find_lang $i --with-kde
	cat ${i}.lang >> kformula.lang
done

%find_lang kpresenterkwordfilter --with-kde
cat kpresenterkwordfilter.lang >> kpresenter.lang

kspread="\
	csvfilter \
	kspreadcalc_calc \
	kspreaddbasefilter \
	kspreadexcelimportfilter \
	kspreadlatexexportfilter \
	kspreadopencalcfilter \
	kspreadqprofilter"

for i in $kspread; do
	%find_lang $i --with-kde
	cat ${i}.lang >> kspread.lang
done

kword="\
	kthesaurus \
	kwordabiwordfilter \
	kwordasciifilter \
	kwordhtmlexportfilter \
	kwordhtmlimportfilter \
	kwordlatexexportfilter \
	kwordlatexfilter \
	kwordlateximportfilter \
	kwordmswordfilter \
	kwordmswritefilter \
	kwordoowriterfilter \
	kwordpdfimport \
	olefilterswinword97filter \
	thesaurus_tool \
	kwordhtmlfilter"

for i in $kword; do
	%find_lang $i --with-kde
	cat ${i}.lang >> kword.lang
done
%endif

files="\
	kchart \
	kformula \
	kivio \
	koffice \
	kugar \
	kpresenter \
	kspread \
	kword"

for i in $files; do
	echo "%defattr(644,root,root,755)" > ${i}_en.lang
	grep en\/ ${i}.lang|grep -v apidocs >> ${i}_en.lang
	grep -v apidocs $i.lang|grep -v en\/ > ${i}.lang.1
	mv ${i}.lang.1 ${i}.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	common -p /sbin/ldconfig
%postun common -p /sbin/ldconfig

%if %{with i18n}
%files common-i18n	-f koffice.lang
%defattr(644,root,root,755)
%files karbon-i18n	-f karbon.lang
%defattr(644,root,root,755)
%files kchart-i18n	-f kchart.lang
%defattr(644,root,root,755)
%files kformula-i18n	-f kformula.lang
%defattr(644,root,root,755)
%files kivio-i18n	-f kivio.lang
%defattr(644,root,root,755)
%files kpresenter-i18n	-f kpresenter.lang
%defattr(644,root,root,755)
%files kspread-i18n	-f kspread.lang
%defattr(644,root,root,755)
%files kugar-i18n	-f kugar.lang
%defattr(644,root,root,755)
%files kword-i18n	-f kword.lang
%defattr(644,root,root,755)
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/libkarbonbase.so
%{_libdir}/libkdchart.so
#%{_libdir}/libkdgantt.so
%{_libdir}/libkexicore.so
%{_libdir}/libkexidatatable.so
%{_libdir}/libkexidb.so
%{_libdir}/libkexidbparser.so
%{_libdir}/libkexiextendedwidgets.so
#%{_libdir}/libkexiimportwizard.so
%{_libdir}/libkeximain.so
%{_libdir}/libkexipropertyeditor.so
%{_libdir}/libkexirelationsview.so
%{_libdir}/libkexisql.so
#%{_libdir}/libkformeditor.so
%{_libdir}/libkformula.so
%{_libdir}/libkiviocommon.so
%{_libdir}/libkochart.so
%{_libdir}/libkofficecore.so
%{_libdir}/libkofficeui.so
%{_libdir}/libkopainter.so
%{_libdir}/libkoscript.so
%{_libdir}/libkospell.so
%{_libdir}/libkotext.so
%{_libdir}/libkowmf.so
%{_libdir}/libkstore.so
%{_libdir}/libkugar.so
%{_libdir}/libkwmailmerge_interface.so
%{_libdir}/libkwmf.so
%{_libdir}/libkwordexportfilters.so
%{_includedir}/*.h
%{_includedir}/kword

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_kdedocdir}/en/%{name}-apidocs
%endif

%files common -f koffice_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/koconverter
%attr(755,root,root) %{_bindir}/koscript
%attr(755,root,root) %{_bindir}/koshell
%{_libdir}/libkarbonbase.la
%attr(755,root,root) %{_libdir}/libkarbonbase.so.2.0.0
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
%{_libdir}/libkeximain.la
%attr(755,root,root) %{_libdir}/libkeximain.so.0.0.0
%{_libdir}/libkexipropertyeditor.la
%attr(755,root,root) %{_libdir}/libkexipropertyeditor.so.0.0.0
%{_libdir}/libkexirelationsview.la
%attr(755,root,root) %{_libdir}/libkexirelationsview.so.0.0.0
%{_libdir}/libkexisql.la
%attr(755,root,root) %{_libdir}/libkexisql.so.*.*.*
%{_libdir}/libkformula.la
%attr(755,root,root) %{_libdir}/libkformula.so.*.*.*
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
%{_libdir}/libkoscript.la
%attr(755,root,root) %{_libdir}/libkoscript.so.*.*.*
%{_libdir}/libkospell.la
%attr(755,root,root) %{_libdir}/libkospell.so.*.*.*
%{_libdir}/libkotext.la
%attr(755,root,root) %{_libdir}/libkotext.so.*.*.*
%{_libdir}/libkowmf.la
%attr(755,root,root) %{_libdir}/libkowmf.so.*.*.*
%{_libdir}/libkstore.la
%attr(755,root,root) %{_libdir}/libkstore.so.*.*.*
%{_libdir}/libkugar.la
%attr(755,root,root) %{_libdir}/libkugar.so.*.*.*
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
%{_datadir}/servicetypes/*
%{_datadir}/apps/koffice
%dir %{_datadir}/apps/kontour
%dir %{_datadir}/apps/kontour/kpartplugins
%{_datadir}/apps/kontour/kpartplugins/scan-kontour.rc
%{_datadir}/apps/koshell
%{_datadir}/services/clipartthumbnail.desktop
%{_datadir}/services/kfile_koffice.desktop
%{_datadir}/services/kfile_ooo.desktop
%{_datadir}/services/kodocinfopropspage.desktop
%{_datadir}/services/kofficethumbnail.desktop
%{_datadir}/services/kounavail.desktop
%{_datadir}/services/ole_*.desktop
#%{_datadir}/services/otherofficethumbnail.desktop
%{_datadir}/services/xslt_*.desktop
%{_datadir}/services/generic_filter.desktop
%dir %{_datadir}/templates/.source
# Conflicts with kdelibs
#%{_datadir}/mimelnk/image/x-msod.desktop
#%{_datadir}/mimelnk/image/x-wmf.desktop
#%{_datadir}/mimelnk/image/x-xfig.desktop
#%{_datadir}/mimelnk/text/x-csv.desktop
%{_desktopdir}/kde/koshell.desktop
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
%{_datadir}/services/karbon*
%{_datadir}/templates/.source/Illustration.karbon
%{_desktopdir}/kde/karbon.desktop
%{_iconsdir}/*/*/apps/karbon.png
%{_mandir}/man1/karbon.1*

%files kchart -f kchart_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kchart
%{_libdir}/libkdeinit_kchart.la
%attr(755,root,root) %{_libdir}/libkdeinit_kchart.so
%{_libdir}/kde3/kchart.la
%attr(755,root,root) %{_libdir}/kde3/kchart.so
%{_libdir}/kde3/libkchartpart.la
%attr(755,root,root) %{_libdir}/kde3/libkchartpart.so
%{_datadir}/apps/kchart
%{_datadir}/services/kchartpart.desktop
%{_desktopdir}/kde/kchart.desktop
%{_iconsdir}/*/*x*/apps/kchart.png
%{_mandir}/man1/kchart.1*

%files kexi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kexi*
%{_libdir}/libkdeinit_kexi.la
%attr(755,root,root) %{_libdir}/libkdeinit_kexi.so
%{_libdir}/kde3/kexi.la
%attr(755,root,root) %{_libdir}/kde3/kexi.so
%{_libdir}/kde3/kexidb_mysqldriver.la
%attr(755,root,root) %{_libdir}/kde3/kexidb_mysqldriver.so
%{_libdir}/kde3/kexidb_sqlitedriver.la
%attr(755,root,root) %{_libdir}/kde3/kexidb_sqlitedriver.so
%{_libdir}/kde3/kexihandler_query.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_query.so
%{_libdir}/kde3/kexihandler_relation.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_relation.so
%{_libdir}/kde3/kexihandler_table.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_table.so
%{_datadir}/apps/kexi
%{_datadir}/config/kexirc
%{_datadir}/config/magic/kexi.magic
%{_datadir}/mimelnk/application/x-kexiproject-shortcut.desktop
%{_datadir}/mimelnk/application/x-kexiproject-sqlite.desktop
%{_datadir}/services/kexi*
%{_desktopdir}/kde/kexi.desktop
%{_iconsdir}/*/*/*/kexi.png
%{_iconsdir}/crystalsvg/32x32/mimetypes/kexiproject_shortcut.png
%{_iconsdir}/crystalsvg/32x32/mimetypes/kexiproject_sqlite.png
#%{_mandir}/man1/kexi.1*
#%{_mandir}/man1/kformdesigner.1*

%files kformula -f kformula_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kformula
#%{_libdir}/kde3/kformula*.la
#%attr(755,root,root) %{_libdir}/kde3/kformula*.so
%{_libdir}/kde3/libkfo*.la
%attr(755,root,root) %{_libdir}/kde3/libkfo*.so
%{_datadir}/apps/kformula
%{_datadir}/services/kformula*
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
%{_mandir}/man1/kformula.1*

%files kivio -f kivio_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kivio
%{_libdir}/*kivio*.la
%attr(755,root,root) %{_libdir}/*kivio*.so
%{_libdir}/kde3/*kivio*.la
%attr(755,root,root) %{_libdir}/kde3/*kivio*.so
%{_libdir}/kde3/sml_connector.la
%attr(755,root,root) %{_libdir}/kde3/sml_connector.so
%{_libdir}/kde3/straight_connector.la
%attr(755,root,root) %{_libdir}/kde3/straight_connector.so
%{_datadir}/apps/kivio
%{_datadir}/config.kcfg/kivio.kcfg
%{_datadir}/services/kivio*.desktop
%{_desktopdir}/kde/kivio.desktop
%{_iconsdir}/*/*/apps/kivio.png
%{_mandir}/man1/kivio.1*

%files kpresenter -f kpresenter_en.lang
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
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krita
%{_libdir}/kde3/*krita*.la
%attr(755,root,root) %{_libdir}/kde3/*krita*.so
%{_libdir}/*krita*.la
%attr(755,root,root) %{_libdir}/*krita*.so
%{_libdir}/kde3/*magick*port.la
%attr(755,root,root) %{_libdir}/kde3/*magick*port.so
%{_libdir}/kde3/colorsfilters.la
%attr(755,root,root) %{_libdir}/kde3/colorsfilters.so
#%{_libdir}/libkisp_example.la
#%attr(755,root,root) %{_libdir}/libkisp_example.so
#%dir %{_datadir}/apps/krayon
#%dir %{_datadir}/apps/krayon/plugins
#%{_datadir}/apps/krayon/plugins/example.kisplugin
%{_datadir}/apps/krita
%{_datadir}/services/krita_magick_import.desktop
%{_datadir}/services/kritapart.desktop
%{_datadir}/templates/Illustration.desktop
%{_desktopdir}/kde/krita.desktop
%{_iconsdir}/*/*/*/krita.png

%files kspread -f kspread_en.lang
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
%{_datadir}/apps/kspread
%{_datadir}/services/kspread*.desktop
%{_datadir}/templates/.source/SpreadSheet.ksp
%{_datadir}/templates/SpreadSheet.desktop
%{_desktopdir}/kde/kspread.desktop
%{_iconsdir}/[!l]*/*/apps/kspread*.png
%{_mandir}/man1/kspread.1*

%files kugar -f kugar_en.lang
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
%{_datadir}/apps/kudesigner
%{_datadir}/apps/kugar
%{_datadir}/services/kugar_kugar_import.desktop
%{_datadir}/services/kugarpart.desktop
%{_iconsdir}/*/*/*/kugar.png
%{_iconsdir}/*/*/mimetypes/kugardata.png
%{_mandir}/man1/kudesigner.1*
%{_mandir}/man1/kugar.1*

%files kword -f kword_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kthesaurus
%attr(755,root,root) %{_bindir}/kword
%{_libdir}/libkdeinit_kword.la
%attr(755,root,root) %{_libdir}/libkdeinit_kword.so
%{_libdir}/kde3/kword.la
%attr(755,root,root) %{_libdir}/kde3/kword.so
%{_libdir}/libkwmailmerge*.la
%attr(755,root,root) %{_libdir}/libkwmailmerge*.so
%{_libdir}/libkword*export*.la
%attr(755,root,root) %{_libdir}/libkword*export*.so
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
%{_libdir}/kde3/libkspelltool.la
%attr(755,root,root) %{_libdir}/kde3/libkspelltool.so
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
%{_datadir}/apps/kword
%{_datadir}/apps/thesaurus
%{_datadir}/apps/xsltfilter/export/kword/xslfo/*.xsl
%{_datadir}/services/kwmailmerge_kabc.desktop
%{_datadir}/services/kspelltool.desktop
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
