Summary:	Pavuk WWW Graber
Name:		pavuk
Version:	0.9pl12
Release:	1
Serial:		1
Copyright:	GPL
Group:		Networking/Utilities
Source:		ftp://ftp.idata.sk/pub/unix/www/%{name}-%{version}.tgz
URL:		http://www.idata.sk/~ondrej/pavuk/
BuildPrereq:	gtk+-devel
BuildPrereq: 	XFree86-devel
BuildPrereq:	gettext
BuildPrereq:	autoconf >= 2.13-8
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Pavuk is UNIX program used to mirror contents of WWW documents or files. It
transfers documents from HTTP, FTP, Gopher and HTTPS (SSL) servers.

%prep
%setup -q

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr/X11R6 \
	--disable-xt \
	--disable-ssl \
	--disable-socks \
	--disable-maintainer-mode
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/share/man/man1/* \
	AUTHORS ChangeLog NEWS README TODO THANK_TO
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz pavukrc.sample pavuk_authinfo.sample Pavuk
%attr(755,root,root) /usr/X11R6/bin/pavuk
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/pavuk.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/pavuk.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/pavuk.mo
/usr/X11R6/share/man/man1/*

%changelog
* Sun May  9 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.9pl12-1]
- now package is FHS 2.0 compliant,
- rewrited from spec obtained from RH contrib.
