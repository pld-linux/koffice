%define		REV	20000420
Summary:	KOffice - powerful office suite for KDE
Summary(pl):	KOffice - potê¿ny pakiet biurowy dla KDE
Name:		koffice
Version:	2.0
Release:	1.pre_%{REV}
License:	GPL
Group:		X11/KDE/Applications
Group(pl):	X11/KDE/Aplikacje
Source:		ftp://ftp.kde.org/pub/kde/snapshots/current/%{name}-%{REV}.tar.bz2
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
* KImage - image viewer
* KImageShop - image processor
* KGraph - technical graphs processor

%description -l pl
KOffice jest zintegrowanym pakietem biurowym dla ¶rodowiska KDE 2.0.
Pakiet miêdzy innymi zawiera:
* KWord - procesor tekstu
* KSpread - arkusz kalkulacyjny
* KPresenter - tworzenie prezentacji
* KChart - generator wykresów
* KIllustrator - grafika wektorowa
* KImage - przegl±darka rysunków
* KImageShop - procesor rysunków
* KGraph - procesor rysunków techniczych

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
# koffice-kgraph
#################################
%package kgraph
Summary:	KOffice - KGraph
Summary(pl):	KOffice - KGraph
Group:		X11/KDE/Applications
Group(pl):	X11/KDE/Aplikacje
Requires:	%{name}-common = %{version}

%description kgraph
KGraph - graphs for engineers.

%description -l pl kgraph
KGraph - program graficzny dla in¿ynierów.

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
# koffice-kimage
#################################
%package kimage
Summary:	KOffice - KImage
Summary(pl):	KOffice - KImage
Group:		X11/KDE/Applications
Group(pl):	X11/KDE/Aplikacje
Requires:	%{name}-common = %{version}

%description kimage
KImage is KOffice image viewer. It's used to embed images in other KOffice
applications and can show all image formats that are supported by Qt and KDE.
It can also adjust an image to a appropriate size.

%description -l pl kimage
KImage jest przegl±dark± plików graficznych. S³u¿y do wklejania rysunków w
innych aplikacjach KOffice i mo¿e pokazaæ rysunki we szystkich formatach,
które s± obs³ugiwane przez Qt i KDE. Program posiada równie¿ mo¿liwo¶æ
zmiany formatu rysunku.

#################################
# koffice-kimageshop
#################################
%package kimageshop
Summary:	KOffice - KImageShop
Summary(pl):	KOffice - KImageShop
Group:		X11/KDE/Applications
Group(pl):	X11/KDE/Aplikacje
Requires:	%{name}-common = %{version}

%description kimageshop
KImageShop is the image processor for the KOffice suite. It's suitable for all
your image creation and editing needs. Perfect for making web images, touching
up your scanned photographs, creating original art, or anything else you might 
need.

%description -l pl kimageshop
KImageShop jest programem tworzenia i obróbki grafiki rastowej dla KOffice.
Jest to porêczne narzêdzie do robienia grafiki dla srton WWW, obróbki
skanowanych fotografii i tworzenia w³asnych dzie³ oraz wszystkiego 
czego mo¿esz chcieæ.

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
%setup -q -n %{name}

%build
make -f Makefile.cvs

CXXFLAGS="$RPM_OPT_FLAGS -Wall"
LDFLAGS="-s"
export LDFLAGS CXXFLAGS
%configure \
	--enable-final \
	--disable-path-check

make -i LD_LIBRARY_PATH="/usr/X11R6/lib"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

make -i \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_icondir=%{_pixmapsdir} \
	install

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/* || :
strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/*.so* || :

%clean
rm -rf $RPM_BUILD_ROOT

%post common	-p /sbin/ldconfig
%postun common	-p /sbin/ldconfig

%post kchart	-p /sbin/ldconfig
%postun kchart	-p /sbin/ldconfig

%post kgraph	-p /sbin/ldconfig
%postun kgraph	-p /sbin/ldconfig

%post killustrator	-p /sbin/ldconfig
%postun killustrator	-p /sbin/ldconfig

%post kimage	-p /sbin/ldconfig
%postun kimage	-p /sbin/ldconfig

%post kimageshop	-p /sbin/ldconfig
%postun kimageshop	-p /sbin/ldconfig

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
%attr(755,root,root) %{_libdir}/libolefilter.so
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_applnkdir}/Applications/KOffice
%{_datadir}/apps/koffice
%{_htmldir}/en/doc/*
%{_htmldir}/en/katabase
%{_htmldir}/en/koffice
%{_datadir}/servicetypes/*

#################################
# koffice-devel
#################################
%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_libdir}/*.la
%{_libdir}/libkofficecore.so
%{_libdir}/libkofficeui.so
%{_libdir}/libkoml.so
%{_libdir}/libkscript.so
%{_libdir}/libkstore.so

#################################
# koffice-kchart
#################################
%files kchart
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kchart
%attr(755,root,root) %{_libdir}/libkchart.so
%{_datadir}/apps/kchart
%{_applnkdir}/Applications/KOffice/kchart.desktop
%{_datadir}/mimelnk/application/x-kchart.desktop

#################################
# koffice-kgraph
#################################
%files kgraph
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgraph
%attr(755,root,root) %{_libdir}/libkgraph.so
%{_datadir}/apps/kgraph
%{_applnkdir}/Applications/KOffice/kgraph.desktop
%{_datadir}/mimelnk/application/x-kgraph.desktop

#################################
# koffice-killustrator
#################################
%files killustrator
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/killustrator
%attr(755,root,root) %{_libdir}/libkillustrator.so
%{_datadir}/apps/killustrator
%{_htmldir}/en/killustrator
%{_applnkdir}/Applications/KOffice/killustrator.desktop
%{_datadir}/mimelnk/application/x-killustrator.desktop
%{_pixmapsdir}/locolor/*x*/apps/killustrator.png
%{_pixmapsdir}/hicolor/*x*/apps/killustrator.png

#################################
# koffice-kimage
#################################
%files kimage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kimage
%attr(755,root,root) %{_libdir}/libkimage.so
%{_datadir}/apps/kimage
%{_applnkdir}/Applications/KOffice/kimage.desktop
%{_datadir}/mimelnk/application/x-kimage.desktop

#################################
# koffice-kimageshop
#################################
%files kimageshop
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kimageshop
%attr(755,root,root) %{_libdir}/libkimageshop.so
%{_datadir}/apps/kimageshop
%{_applnkdir}/Applications/KOffice/kimageshop.desktop
%{_datadir}/mimelnk/application/x-kimageshop.desktop

#################################
# koffice-kpresenter
#################################
%files kpresenter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpresenter
%attr(755,root,root) %{_libdir}/libkpresenter.so
%{_datadir}/apps/kpresenter
%{_htmldir}/en/kpresenter
%{_applnkdir}/Applications/KOffice/kpresenter.desktop
%{_datadir}/mimelnk/application/x-kpresenter.desktop
%{_datadir}/mimelnk/application/x-powerpoint97.desktop
%{_datadir}/services/ole_powerpoint97_import.desktop
%{_pixmapsdir}/locolor/*x*/apps/kpresenter.png
%{_pixmapsdir}/hicolor/*x*/apps/kpresenter.png

#################################
# koffice-kspread
#################################
%files kspread
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kspread
#%attr(755,root,root) %{_libdir}/
%{_datadir}/apps/kspread
%{_applnkdir}/Applications/KOffice/kspread.desktop
%{_datadir}/mimelnk/application/x-excel97.desktop
%{_datadir}/mimelnk/application/x-kspread.desktop
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
%attr(755,root,root) %{_libdir}/libkword.so
%attr(755,root,root) %{_libdir}/libasciiexport.so
%attr(755,root,root) %{_libdir}/libasciiimport.so
%attr(755,root,root) %{_libdir}/libhtmlexport.so
%attr(755,root,root) %{_libdir}/libhtmlimport.so
%attr(755,root,root) %{_libdir}/libkspelltool.so
%{_datadir}/apps/kword
%{_htmldir}/en/kword
%{_applnkdir}/Applications/KOffice/kword.desktop
%{_datadir}/mimelnk/application/x-kword.desktop
%{_datadir}/mimelnk/application/x-winword97.desktop
%{_datadir}/services/kspelltool.desktop
%{_datadir}/services/kword_ascii_export.desktop
%{_datadir}/services/kword_ascii_import.desktop
%{_datadir}/services/kword_html_export.desktop
%{_datadir}/services/kword_html_import.desktop
%{_datadir}/services/ole_winword97_import.desktop
%{_pixmapsdir}/locolor/*x*/apps/kword.png
%{_pixmapsdir}/hicolor/*x*/apps/kword.png
