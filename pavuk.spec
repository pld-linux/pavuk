Summary:	Pavuk WWW Graber
Summary(pl):	Narzedzie do nieinteraktywnego ¶ci±gania stron WWW.
Name:		pavuk
Version:	0.9pl24
Release:	1
Serial:		1
License:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source0:	ftp://ftp.idata.sk/pub/unix/www/%{name}-%{version}.tgz
Patch0:		pavuk-DESTDIR.patch
URL:		http://www.idata.sk/~ondrej/pavuk/
BuildRequires:	gtk+-devel
BuildRequires:	gettext-devel
BuildRequires:	automake
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
Pavuk (Paj±k) jest programem do robienia odbiæ lustrzanych (mirror)
stron WWW. Mo¿e pracowaæ z protoko³ami HTTP, FTP i Gopher.

%prep
%setup -q
%patch -p1

%build
gettext --copy --force
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
%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz pavukrc.sample pavuk_authinfo.sample Pavuk
%attr(755,root,root) %{_bindir}/pavuk
%{_mandir}/man1/*
