Summary:	Pavuk WWW Graber
Summary(cs):	Program pro zrcadlení HTTP, FTP a Gopher serverù
Summary(fr):	Un programme de mirroring pour HTTP, FTP ou les serveurs Gopher
Summary(it):	Un programma di mirroring per server HTTP, FTP e Gopher
Summary(pl):	Narzêdzie do nieinteraktywnego ¶ci±gania stron WWW
Summary(sk):	Program na zrkadlenie HTTP, FTP a Gopher serverov
Name:		pavuk
Version:	0.9pl29d
Release:	3
Epoch:		1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.idata.sk/~ondrej/sw/%{name}-%{version}.tgz
Source1:	%{name}.png
Patch0:		%{name}-fixes.patch
Patch1:		%{name}-ac.patch
Patch2:		%{name}-desktop.patch
Icon:		pavuk.xpm
URL:		http://www.idata.sk/~ondrej/pavuk/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	db1-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7
Obsoletes:	pavuk-ssl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/misc

%description
Pavuk is UNIX program used to mirror contents of WWW documents or
files. It transfers documents from HTTP, FTP and Gopher servers.

%description -l cs
Pavuk je program pou¾ívaný pro zrcadlení obsahu WWW dokumentù
pomocí protokolù HTTP, FTP, Gopher a HTTPS (SSL).

%description -l fr
Pavuk est un programme utilisé pour mirrorer le contenu de documents
web en utilisant HTTP, FTP, GOPHER ou HTTPS (SSL).

%description -l it
Pavuk e' un programma usato per fare il mirror dei contenuti dei
documenti su Web utilizzando HTTP, FTP, Gopher o HTTPS (SSL).

%description -l pl
Pavuk (Paj±k) jest programem do robienia odbiæ lustrzanych (mirror)
stron WWW. Mo¿e pracowaæ z protoko³ami HTTP, FTP i Gopher.

%description -l sk
Pavuk je program na zrkadlenie obsahu Web dokumentov prostredníctvom
HTTP, FTP, Gopher alebo HTTPS (SSL).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
cp %{SOURCE1} .

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
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
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Network/Misc

cp -af pavukrc.sample pavuk_authinfo.sample $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/pavuk
%{_applnkdir}/Network/Misc/*
%{_examplesdir}/%{name}-%{version}/*
%{_pixmapsdir}/*
%{_mandir}/man?/*
