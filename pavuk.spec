%define prefix /usr/local

Summary: Pavuk WWW Graber
Name: pavuk
Version: 0.9pl7
Release: 1
Serial: 1
Copyright: GPL
Packager: Stefan Ondrejicka <ondrej@idata.sk>
Group: Networking/Utilities
Source: ftp://ftp.idata.sk/pub/unix/www/pavuk-%{PACKAGE_VERSION}.tgz
BuildRoot: /tmp/pavuk_root/
URL: http://www.idata.sk/~ondrej/pavuk/
Provides: pavuk

%description
WWW graber used to mirror files located on HTTP, HTTPS, FTP, Gopher servers.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target}
	--prefix=%{prefix} \
	--disable-maintainer-mode
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
%doc AUTHORS COPYING ChangeLog NEWS README INSTALL TODO THANK_TO pavukrc.sample pavuk_authinfo.sample pavuk.lsm pavuk.spec po/pavuk.pot Pavuk

%{prefix}/bin/pavuk
%{prefix}/share/locale/sk/LC_MESSAGES/pavuk.mo
%{prefix}/share/locale/de/LC_MESSAGES/pavuk.mo
%{prefix}/share/locale/cs/LC_MESSAGES/pavuk.mo
%{prefix}/man/man1/pavuk.1
