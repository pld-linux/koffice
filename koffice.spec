# TODO: kformula to separate package
%define 	no_compress_doc 1
Summary:	KOffice - powerful office suite for KDE
Summary(pl):	KOffice - potê¿ny pakiet biurowy dla KDE
Summary(pt_BR):	Suíte de aplicativos office para o KDE
Summary(ru):	îÁÂÏÒ ÏÆÆÉÓÎÙÈ ÐÒÏÇÒÁÍÍ ÄÌÑ KDE
Summary(uk):	îÁÂ¦Ò ÏÆ¦ÓÎÉÈ ÐÒÏÇÒÁÍ ÄÌÑ KDE
Summary(zh_CN):	KDE µÄ°ì¹«Ó¦ÓÃÈí¼þ¼¯¡£
Name:		koffice
Version:	1.2
Release:	2
Epoch:		4
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}-%{version}/src/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.kde.org/pub/kde/stable/%{name}-%{version}/src/%{name}-i18n-%{version}.tar.bz2
Patch0:		%{name}-fix-change-custom-variable-value.patch
Patch1:		%{name}-desktop.fixes.patch
URL:		http://www.koffice.org/
BuildRequires:	XFree86-devel
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	perl
BuildRequires:	python-devel >= 2.2
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
#Obsoletes:	koffice-kontour
#Obsoletes:	koffice-karbon

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
- Kontour - vector drawing
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
- Kontour - grafika wektorowa
- Krayon - bazuj±cy na pikselach program typu GIMP czy Adobe(c)
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

# koffice-devel
%package devel
Summary:	KOffice - header files
Summary(es):	Header files for compiling applications that use koffice libraries.
Summary(pl):	KOffice - pliki nag³ówkowe
Summary(pt_BR):	Arquivos de inclusão necessários à compilação de aplicações que usem as bibliotecas do koffice
Group:		X11/Development/Libraries
Requires:	%{name}-common = %{version}

%description devel
This package includes the header files you will need to compile
applications that use koffice libraries.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe, których bêdziesz potrzebowa³ aby
skompilowaæ programy u¿ywaj±ce bibliotek KOffice.

%description devel -l pt_BR
Arquivos de inclusão necessários à compilação de aplicações que usem
as bibliotecas do koffice.

# koffice-common
%package common
Summary:	KOffice - common files and libraries
Summary(pl):	KOffice - wspó³dzielone pliki i biblioteki
Summary(pt_BR):	Arquivos requeridos por todos os softwares koffice
Group:		X11/Applications
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
Obsoletes:	koffice-i18n-Hebrew
Obsoletes:	koffice-i18n-Hungarian
Obsoletes:	koffice-i18n-Icelandic
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

%description common -l pl
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

%description common -l pt_BR
Arquivos requeridos por todos os softwares koffice.

# koffice-karbon
%package karbon
Summary:        KOffice - Karbon
Summary(pl):    KOffice - Karbon
Group:          X11/Applications
Requires:       %{name}-common = %{version}
#karbon has changed its named (again) to curt therefore in the future:
#Obsoletes: koffice-karbon

%description karbon
Karbon is a vector graphics application within koffice.


%description karbon -l pl
Karbon to aplikacja koffice slu¿±ca do rysowania grafiki wektorowej,


# koffice-kchart
%package kchart
Summary:	KOffice - KChart
Summary(pl):	KOffice - KChart
Summary(pt_BR):	Gerador de diagramas do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{version}

%description kchart
KChart is KOffice part for generating diagrams from data, e.g. pie and
bar charts.

%description kchart -l pl
KChart jest aplikacj± s³u¿±c± do generowania wykresów.

%description kchart -l pt_BR
Gerador de diagramas do KOffice.

# koffice-kontour (f. k. a. koffice-killustrator)
%package kontour
Summary:	KOffice - Kontour
Summary(pl):	KOffice - Kontour
Summary(pt_BR):	Ferramenta de desenho vetorial do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{version}

%description kontour
Kontour is the vector drawing program for the K Desktop Environment.
The aim of the Kontour project is the development of a freely
available vector-based drawing application similar to Corel Draw or
Adobe Illustrator.
Kontour was formerly known as KIllustrator but due to blackmail made
by Adobe lawyers it has to be renamed.

%description kontour -l pl
Kontour jest programem do tworzenia grafiki wektorowej dla ¶rodowiska
KDE. Celem przy¶wiecaj±cym programistom jest stworzenie w pe³ni
funkcjonalnego programu do grafiki wektorowej podobnego do Corel Draw
lub Adobe Illustrator.

Kontour wczesniej by³ znany jako KIlustrator ale developerzy zostali
zmuszeni szanta¿em przez prawników Adobe do zmiany nazwy.

%description kontour -l pt_BR
Ferramenta de desenho vetorial do KOffice.
# koffice-kpresenter
%package kpresenter
Summary:	KOffice - KPresenter
Summary(pl):	KOffice - KPresenter
Group:		X11/Applications
Requires:	%{name}-common = %{version}

%description kpresenter
KPresenter is a presentation application of the KOffice, similar to MS
PowerPoint in the windows world. You can use it for doing screen
presentations or transparencies.

%description kpresenter -l pl
KPresenter jest aplikacj± KOffice do tworzenia prezentacji, podobn± do
MS PowerPoint. Mo¿esz u¿yæ jej do tworzenia wizualnych prezentacji.

# koffice-kspread
%package kspread
Summary:	KOffice - KSpread
Summary(pl):	KOffice - KSpread
Summary(pt_BR):	Planilha eletrônica do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{version}

%description kspread
KSpread is the spread sheet of the KOffice, similar to MS Excel.

%description kspread -l pl
KSpread jest arkuszem kalkulacyjnym, podobnym do MS Excel.

%description kspread -l pt_BR
Planilha eletrônica do KOffice.

# koffice-kword
%package kword
Summary:	KOffice - KWord
Summary(pl):	KOffice - KWord
Summary(pt_BR):	Processador de texto do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{version}

%description kword
KWord is a FrameMaker-like wordprocessor application for KOffice. So
it can be used for DTP, but also for "normal" wordprocessing (like
writing letters, reports, etc.).

%description kword -l pl
KWord jest ramkowym procesorem tekstu. Mo¿e byæ u¿yty do DTP, ale
równie¿ do zwyk³ej edycji tekstu (jak pisanie listów, raportów, itp.).

%description kword -l pt_BR
Processador de texto do KOffice.

# koffice-kivio
%package kivio
Summary:	KOffice - ivio
Summary(pl):	KOffice - ivio
Summary(pt_BR):	Editor de fluxogramas do KOffice
Group:		X11/Applications
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

%description kivio -l pl
Kivio jest programem typu flowcharting. Kivio dostarcza
najpotrzebniejsze funkcje ale wszystkie obiekty mo¿na rozszerzaæ za
pomoc± jêzyka skryptowego.

%description kivio -l pt_BR
Editor de fluxogramas do KOffice.

# koffice-kugar
%package kugar
Summary:	KOffice - KUgar
Summary(pl):	KOffice - KUgar
Summary(pt_BR):	Gerador de relatórios do KOffice
Group:		X11/Applications
Requires:	%{name}-common = %{version}

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

######################## end descriptions ########################

%prep
%setup -q -n %{name}-%{version} -a1
#%patch0 -p1
#%patch1 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
CFLAGS="-D_GNU_SOURCE %{rpmcflags}"
CXXFLAGS="-D_GNU_SOURCE %{rpmcflags} -fno-check-new"
%configure \
	%{!?debug:--disable-debug} \
	--enable-final \
	--with-xinerama \
	--enable-shared \
	--disable-rpath

%{__make}

cd %{name}-i18n-%{version}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_applnkdir}
install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/{Wordprocessors,Spreadsheets} \
	$RPM_BUILD_ROOT%{_applnkdir}/Office/{Presentation,Misc} \
	$RPM_BUILD_ROOT%{_applnkdir}/Graphics

install kontour/kontour.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Graphics
install kpresenter/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Presentation
install kspread/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Spreadsheets
install kword/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Wordprocessors
install kivio/kiviopart/k*.desktop	$RPM_BUILD_ROOT%{_applnkdir}/Office/Misc
install kugar/part/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Presentation
install kchart/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Misc

install kformula/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office/Misc
install koshell/k*.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Office

#mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/apps/{kchart,kontour,kpresenter,kspread,kword,kivio}.png \
#	$RPM_BUILD_ROOT%{_pixmapsdir}

cd %{name}-i18n-%{version}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd ..

##############
## KPRESENTER:
%find_lang kpresenter --with-kde
%find_lang kpresenterkwordfilter --with-kde
cat kpresenterkwordfilter.lang >> kpresenter.lang

##############
## KSPREAD:
%find_lang kspread --with-kde
%find_lang kspreadcalc_calc --with-kde
%find_lang kspreadqprofilter --with-kde
%find_lang csvfilter --with-kde
cat kspreadcalc_calc.lang kspreadqprofilter.lang csvfilter.lang >> kspread.lang

##############
## KWORD:
%find_lang kword --with-kde
programs="kthesaurus kwordasciifilter kwordhtmlexportfilter kwordhtmlfilter kwordhtmlimportfilter kwordlatexfilter kwordmswritefilter thesaurus_tool"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kword.lang
done

##############
## COMMON:
> common.lang
programs="desktop_koffice example graphite kdatabase kfile_koffice kformula kformulalib kformulalatexfilter kformulapngfilter koconverter kocryptfilter koffice koshell kscan_plugin kounavail kplato krita kudesigner olefilterswinword97filter xsltfilter xsltexportfilter xsltimportfilter"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> common.lang
done

###############
## OTHERS:
%find_lang kchart --with-kde
#%find_lang kdiagramm --with-kde
#cat kdiagramm.lang >> kchart.lang
%find_lang kivio --with-kde
%find_lang kugar --with-kde
%find_lang kontour --with-kde

# will be introduced in koffice 1.3:
%find_lang karbon --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post common	-p /sbin/ldconfig
%postun common	-p /sbin/ldconfig

%post karbon   -p /sbin/ldconfig
%postun karbon -p /sbin/ldconfig

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
%files common -f common.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kformula
%attr(755,root,root) %{_bindir}/kudesigner
%attr(755,root,root) %{_bindir}/koconverter
%attr(755,root,root) %{_bindir}/koscript
%attr(755,root,root) %{_bindir}/koshell
%attr(755,root,root) %{_libdir}/koshell.??
%attr(755,root,root) %{_libdir}/kformulamain.??
%attr(755,root,root) %{_libdir}/kde3/clipartthumbnail.??
%attr(755,root,root) %{_libdir}/kde3/kfile_koffice.??
%attr(755,root,root) %{_libdir}/kde3/kodocinfopropspage.??
%attr(755,root,root) %{_libdir}/kde3/kofficescan.??
%attr(755,root,root) %{_libdir}/kde3/kofficethumbnail.??
%attr(755,root,root) %{_libdir}/libkotext.??
%attr(755,root,root) %{_libdir}/libkopainter.??
#%attr(755,root,root) %{_libdir}/kde3/lib[!k][!a][!r][!b][!o][!n]*export.??
#%attr(755,root,root) %{_libdir}/kde3/lib[!k][!a][!r][!b][!o][!n]*import.??
#%attr(755,root,root) %{_libdir}/kde3/lib[!karbon]*import.??
%attr(755,root,root) %{_libdir}/kde3/liblibkfo*.??
%attr(755,root,root) %{_libdir}/kde3/libxslt*port*.??
%attr(755,root,root) %{_libdir}/kde3/libkformulapart.??
%attr(755,root,root) %{_libdir}/kde3/libkounavailpart.??
%attr(755,root,root) %{_libdir}/kde3/liblatexparser.??
%attr(755,root,root) %{_libdir}/kde3/libolefilter.??
%attr(755,root,root) %{_libdir}/libkwmf.??
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libkdchart.la
%{_applnkdir}/Office/koshell.desktop
%{_applnkdir}/Office/Misc/kformula.desktop
%{_datadir}/servicetypes/*
%{_pixmapsdir}/*color/*x*/actions/abs.png
%{_pixmapsdir}/*color/*x*/actions/brac*.png
%{_pixmapsdir}/*color/*x*/actions/frac.png
%{_pixmapsdir}/*color/*x*/actions/ins*.png
%{_pixmapsdir}/*color/*x*/actions/rem*.png
%{_pixmapsdir}/*color/*x*/actions/int.png
%{_pixmapsdir}/*color/*x*/actions/[lr]su[bp].png
%{_pixmapsdir}/*color/*x*/actions/matrix.png
%{_pixmapsdir}/*color/*x*/actions/paren.png
%{_pixmapsdir}/*color/*x*/actions/prod.png
%{_pixmapsdir}/*color/*x*/actions/sqrt.png
%{_pixmapsdir}/*color/*x*/actions/sum.png
%{_pixmapsdir}/*color/*x*/actions/onetwomatrix.png
%{_pixmapsdir}/*color/*x*/apps/kudesigner.png
%{_pixmapsdir}/*color/*x*/apps/kformula.png    
%{_datadir}/apps/kformula
%{_datadir}/apps/koffice
%{_datadir}/apps/kudesigner
%{_datadir}/services/clipartthumbnail.desktop
%{_datadir}/services/kfile_koffice.desktop
%{_datadir}/services/kformula*
%{_datadir}/services/kodocinfopropspage.desktop
%{_datadir}/services/kofficethumbnail.desktop
%{_datadir}/services/kounavail.desktop
%{_datadir}/services/ole_*.desktop
%{_datadir}/services/otherofficethumbnail.desktop
%{_datadir}/services/xslt_*.desktop
%{_datadir}/mimelnk/application/x-kudesigner.desktop
# Conflicts with kdelibs
#%{_datadir}/mimelnk/image/x-msod.desktop
#%{_datadir}/mimelnk/image/x-wmf.desktop
#%{_datadir}/mimelnk/image/x-xfig.desktop
#%{_datadir}/mimelnk/text/x-csv.desktop

#################################
# koffice-devel
#################################
%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/libkformul*.??
#%attr(755,root,root) %{_libdir}/libkodocinfopropspage.??
%attr(755,root,root) %{_libdir}/libkochart.??
%attr(755,root,root) %{_libdir}/libkdchart.so
%attr(755,root,root) %{_libdir}/libkofficecore.??
%attr(755,root,root) %{_libdir}/libkofficeui.??
%attr(755,root,root) %{_libdir}/libkoscript.??
%attr(755,root,root) %{_libdir}/libkstore.??

#################################
# koffice-karbon
#################################
%files -f karbon.lang karbon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karbon
%attr(755,root,root) %{_libdir}/karbon.??
%attr(755,root,root) %{_libdir}/libkugar.la
%attr(755,root,root) %{_libdir}/kde3/libkarbonpart.??
%attr(755,root,root) %{_libdir}/kde3/libkarbon*import*
%attr(755,root,root) %{_libdir}/kde3/libkarbon*export*
#%{_datadir}/apps/karbon
#%{_datadir}/templates/.source/Presentation.kpt
##%{_datadir}/templates/Presentation.desktop
#%{_applnkdir}/Office/Presentation/kpresenter.desktop
%{_datadir}/services/karbon*

##%{_pixmapsdir}/kpresenter.png
%{_pixmapsdir}/*/*/apps/karbon.png


#################################
# koffice-kchart
#################################
%files -f kchart.lang kchart
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kchart
%attr(755,root,root) %{_libdir}/kchart.??
%attr(755,root,root) %{_libdir}/kde3/libkchartpart.??
%{_datadir}/apps/kchart
%{_applnkdir}/Office/Misc/kchart.desktop
#%{_pixmapsdir}/kchart.png
%{_pixmapsdir}/*/*/apps/kchart*.png

#################################
# koffice-kontour
#################################
%files -f kontour.lang kontour
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kontour
%attr(755,root,root) %{_libdir}/kontour.??
%attr(755,root,root) %{_libdir}/kde3/libkontourpart.??
%attr(755,root,root) %{_libdir}/kde3/libapplixgraphicimport.??
%attr(755,root,root) %{_libdir}/kde3/libmsodimport.??
%attr(755,root,root) %{_libdir}/kde3/libwmfimport.??
#%attr(755,root,root) %{_libdir}/kde3/liblibkfo*.??
%attr(755,root,root) %{_libdir}/kde3/libkontourrtfexport.so
%attr(755,root,root) %{_libdir}/kde3/libtexgraphexport.so
#%attr(755,root,root) %{_libdir}/kde3/libsvgexport.??
#%attr(755,root,root) %{_libdir}/kde3/libxfigimport.??
%{_datadir}/apps/kontour
%{_datadir}/services/kontour*.desktop
%{_datadir}/services/kprkword.desktop
#%{_datadir}/mimelnk/image/x-svg.desktop
%{_datadir}/templates/.source/Illustration.kil
%{_datadir}/templates/Illustration.desktop
%{_applnkdir}/Graphics/kontour.desktop
%{_pixmapsdir}/*/*/*/kontour.png


#################################
# koffice-kpresenter
#################################
%files -f kpresenter.lang kpresenter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpresenter
%attr(755,root,root) %{_bindir}/kprconverter.pl
%attr(755,root,root) %{_libdir}/kpresenter.??
%attr(755,root,root) %{_libdir}/kde3/libkpresenterpart.??
%attr(755,root,root) %{_libdir}/kde3/libkprkword.??
%{_datadir}/apps/kpresenter
%{_datadir}/templates/.source/Presentation.kpt
%{_datadir}/templates/Presentation.desktop
%{_applnkdir}/Office/Presentation/kpresenter.desktop
#%{_pixmapsdir}/kpresenter.png
%{_pixmapsdir}/*/*/apps/kpresenter*.png

#################################
# koffice-kspread
#################################
%files -f kspread.lang kspread
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kspread
%attr(755,root,root) %{_libdir}/kspread.??
%attr(755,root,root) %{_libdir}/kde3/libkspread*.??
%attr(755,root,root) %{_libdir}/kde3/libcsv*.??
%attr(755,root,root) %{_libdir}/kde3/libapplixspreadimport.??
%attr(755,root,root) %{_libdir}/kde3/libgnumeric*port.??
%attr(755,root,root) %{_libdir}/kde3/libdbase*port.??
%attr(755,root,root) %{_libdir}/kde3/libqproimport.??
%{_datadir}/apps/kspread
#%{_datadir}/mimelnk/text/x-gnumeric.desktop
%{_datadir}/services/kspread*.desktop
%{_datadir}/templates/.source/SpreadSheet.ksp
%{_datadir}/templates/SpreadSheet.desktop
%{_applnkdir}/Office/Spreadsheets/kspread.desktop
#%{_pixmapsdir}/kspread.png
%{_pixmapsdir}/*/*/apps/kspread*.png

#################################
# koffice-kword
#################################
%files -f kword.lang kword
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kthesaurus
%attr(755,root,root) %{_bindir}/kword
%attr(755,root,root) %{_libdir}/kword.??
%attr(755,root,root) %{_libdir}/libkwmailmerge*.??
%attr(755,root,root) %{_libdir}/libkwordexport*.??
%attr(755,root,root) %{_libdir}/kde3/kwmailmerge*.??
%attr(755,root,root) %{_libdir}/kde3/libabiword*port.??
%attr(755,root,root) %{_libdir}/kde3/libapplixwordimport.??
%attr(755,root,root) %{_libdir}/kde3/libascii*port.??
%attr(755,root,root) %{_libdir}/kde3/libdocbookexport.??
%attr(755,root,root) %{_libdir}/kde3/libhtml*port.??
%attr(755,root,root) %{_libdir}/kde3/libpalmdoc*port.??
%attr(755,root,root) %{_libdir}/kde3/libamipro*port.??
%attr(755,root,root) %{_libdir}/kde3/libwml*port.??
%attr(755,root,root) %{_libdir}/kde3/libkspelltool.??
%attr(755,root,root) %{_libdir}/kde3/libkwordpart.??
%attr(755,root,root) %{_libdir}/kde3/liblatexexport.??
%attr(755,root,root) %{_libdir}/kde3/librtf*port.??
%attr(755,root,root) %{_libdir}/kde3/libthesaurustool.??
%attr(755,root,root) %{_libdir}/kde3/libwp*port.??
%attr(755,root,root) %{_libdir}/kde3/libmswrite*port.??

%{_datadir}/apps/kword
%{_datadir}/apps/thesaurus
%{_datadir}/services/kspelltool.desktop
%{_datadir}/services/kword*.desktop
%{_datadir}/services/kprkword.desktop
%{_datadir}/services/kwserialletter*
%{_datadir}/services/thesaurustool.desktop
%{_datadir}/templates/.source/TextDocument.kwt
%{_datadir}/templates/TextDocument.desktop
%{_applnkdir}/Office/Wordprocessors/kword.desktop
%{_applnkdir}/Office/Wordprocessors/kwmailmerge.desktop
#%{_pixmapsdir}/kword.png
%{_pixmapsdir}/*/*/apps/kword*.png
%{_datadir}/apps/xsltfilter/export/kword/xslfo/*.xsl

#################################
# koffice-kivio
#################################
%files -f kivio.lang kivio
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kivio
%attr(755,root,root) %{_libdir}/*kivio*.??
%attr(755,root,root) %{_libdir}/kde3/*kivio*.??
%{_applnkdir}/Office/Misc/kivio.desktop
%{_datadir}/apps/kivio
#%{_pixmapsdir}/kivio.png
%{_pixmapsdir}/*/*/apps/kivio*.png
#%{_datadir}/mimelnk/application/x-kivio.desktop
%{_datadir}/services/kivio*.desktop

#################################
# koffice-kugar
#################################
%files -f kugar.lang kugar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kugar
%attr(755,root,root) %{_libdir}/libkugar*.??
%attr(755,root,root) %{_libdir}/straight_connector.ksp
%{_applnkdir}/Office/Presentation/kugar.desktop
%{_datadir}/apps/kugar
%{_pixmapsdir}/*/*/apps/kugar*.png
#%{_datadir}/mimelnk/application/x-kugar.desktop
%{_pixmapsdir}/*/*/mimetypes/*kugar*
