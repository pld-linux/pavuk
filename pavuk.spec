Summary:	Pavuk WWW Graber
Summary(pl):	Narzedzie do nieinteraktywnego �ci�gania stron WWW
Name:		pavuk
Version:	0.9pl25
Release:	1
Serial:		1
License:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narz�dzia
Source0:	ftp://ftp.idata.sk/pub/unix/www/%{name}-%{version}.tgz
Source1:	pavuk.png
Patch0:		pavuk-fixes.patch
Icon:		pavuk.xpm
URL:		http://www.idata.sk/~ondrej/pavuk/
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	openssl-devel >= 0.9.4-2
Obsoletes:	pavuk-ssl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/misc

%description
Pavuk is UNIX program used to mirror contents of WWW documents or
files. It transfers documents from HTTP, FTP and Gopher servers.

%description -l pl
Pavuk (Paj�k) jest programem do robienia odbi� lustrzanych (mirror)
stron WWW. Mo�e pracowa� z protoko�ami HTTP, FTP i Gopher.

%prep
%setup -q
%patch -p1
cp %{SOURCE1} .

%build
automake

CFLAGS="-I/usr/include/openssl"; export CFLAGS 
LDFLAGS="-s"; export LDFLAGS
%configure \
	--disable-xt \
	--enable-ssl \
	--disable-socks \
	--disable-maintainer-mode
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Network/Misc

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz pavukrc.sample pavuk_authinfo.sample Pavuk
%attr(755,root,root) %{_bindir}/pavuk
%{_applnkdir}/Network/Misc/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
