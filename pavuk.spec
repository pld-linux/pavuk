Summary:	Pavuk WWW Graber
Summary(pl):	Narz�dzie do nieinteraktywnego �ci�gania stron WWW
Name:		pavuk
Version:	0.9pl29d
Release:	1
Epoch:		1
License:	GPL
Group:		Networking/Utilities
Group(cs):	S�ov�/Utility
Group(da):	Netv�rks/V�rkt�j
Group(de):	Netzwerkwesen/Dienstprogramme
Group(es):	Red/Utilitarios
Group(fr):	R�seau/Utilitaires
Group(is):	Net/T�l
Group(it):	Rete/Utility
Group(no):	Nettverks/Verkt�y
Group(pl):	Sieciowe/Narz�dzia
Group(pt_BR):	Rede/Utilit�rios
Group(pt):	Rede/Utilidades
Group(ru):	�������/����������
Group(sl):	Omre�ni/Pripomo�ki
Group(sv):	N�tverk/Verktyg
Source0:	http://www.idata.sk/~ondrej/sw/%{name}-%{version}.tgz
Source1:	%{name}.png
Patch0:		%{name}-fixes.patch
Icon:		pavuk.xpm
URL:		http://www.idata.sk/~ondrej/pavuk/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	db1-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.6a
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
rm missing
libtoolize --copy --force
gettextize --copy --force
aclocal
autoconf
automake -a -c
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
	desktopdir=%{_applnkdir}/Network/Misc

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz pavukrc.sample pavuk_authinfo.sample Pavuk
%attr(755,root,root) %{_bindir}/pavuk
%{_applnkdir}/Network/Misc/*
%{_pixmapsdir}/*
%{_mandir}/man?/*
