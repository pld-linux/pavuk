Summary:	Pavuk WWW Graber
Summary(pl):	Narzedzie do nieinteraktywnego ¶ci±gania stron WWW.
Name:		pavuk
Version:	0.9pl14
Release:	1
Serial:		1
Copyright:	GPL
Group:		Networking/Utilities
Source:		ftp://ftp.idata.sk/pub/unix/www/%{name}-%{version}.tgz
Patch:		pavuk-DESTDIR.patch
URL:		http://www.idata.sk/~ondrej/pavuk/
BuildPrereq:	gtk+-devel
BuildPrereq: 	XFree86-devel
BuildPrereq:	gettext
BuildPrereq:	automake
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

%description
Pavuk is UNIX program used to mirror contents of WWW documents or files. It
transfers documents from HTTP, FTP and Gopher servers.

%description -l pl
Pavuk (Paj±k) jest programem do robienia odbiæ lustrzanych (mirror) stron WWW.
Mo¿e pracowaæ z protoko³ami HTTP, FTP i Gopher.

%prep
%setup -q
%patch -p1

%build
automake
LDFLAGS="-s"; export LDFLAGS
%configure \
	--disable-xt \
	--disable-ssl \
	--disable-socks \
	--disable-maintainer-mode
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS ChangeLog NEWS README TODO THANK_TO

%find_lang pavuk

%clean
rm -rf $RPM_BUILD_ROOT

%files -f pavuk.lang
%defattr(644,root,root,755)
%doc *.gz pavukrc.sample pavuk_authinfo.sample Pavuk
%attr(755,root,root) %{_bindir}/pavuk
%{_mandir}/man1/*

%changelog
* Sun May  9 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.9pl12-1]
- now package is FHS 2.0 compliant,
- rewrited from spec obtained from RH contrib.
