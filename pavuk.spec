Summary:	Pavuk WWW Graber
Summary(cs.UTF-8):	Program pro zrcadlení HTTP, FTP a Gopher serverů
Summary(fr.UTF-8):	Un programme de mirroring pour HTTP, FTP ou les serveurs Gopher
Summary(it.UTF-8):	Un programma di mirroring per server HTTP, FTP e Gopher
Summary(pl.UTF-8):	Narzędzie do nieinteraktywnego ściągania stron WWW
Summary(sk.UTF-8):	Program na zrkadlenie HTTP, FTP a Gopher serverov
Name:		pavuk
Version:	0.9.35
Release:	1
Epoch:		1
License:	GPL
Group:		Networking/Utilities
Source0:	http://downloads.sourceforge.net/project/pavuk/pavuk/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	6204c7a1339433ab32456ccd62126ea9
Source1:	%{name}.png
Patch0:		%{name}-fixes.patch
Patch1:		%{name}-ac.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-open-args-typo.patch
URL:		http://www.pavuk.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
Obsoletes:	pavuk-ssl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/misc

%description
Pavuk is UNIX program used to mirror contents of WWW documents or
files. It transfers documents from HTTP, FTP and Gopher servers.

%description -l cs.UTF-8
Pavuk je program používaný pro zrcadlení obsahu WWW dokumentů pomocí
protokolů HTTP, FTP, Gopher a HTTPS (SSL).

%description -l fr.UTF-8
Pavuk est un programme utilisé pour mirrorer le contenu de documents
web en utilisant HTTP, FTP, GOPHER ou HTTPS (SSL).

%description -l it.UTF-8
Pavuk e' un programma usato per fare il mirror dei contenuti dei
documenti su Web utilizzando HTTP, FTP, Gopher o HTTPS (SSL).

%description -l pl.UTF-8
Pavuk (Pająk) jest programem do robienia odbić lustrzanych (mirror)
stron WWW. Może pracować z protokołami HTTP, FTP i Gopher.

%description -l sk.UTF-8
Pavuk je program na zrkadlenie obsahu Web dokumentov prostredníctvom
HTTP, FTP, Gopher alebo HTTPS (SSL).

%prep
%setup -q
mv pavuk.desktop pavuk.desktop.latin1
iconv -flatin1 -tutf8 pavuk.desktop.latin1 > pavuk.desktop
%patch0 -p1
%patch2 -p1
%patch3 -p1
cp -a %{SOURCE1} .

%build
# don't run gettextize, pavuk has its own po install system using automake
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-ssl \
	--enable-threads \
	--disable-socks \
	--disable-maintainer-mode
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO pavukrc.sample pavuk_authinfo.sample
%attr(755,root,root) %{_bindir}/pavuk
%{_mandir}/man1/pavuk.1*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
