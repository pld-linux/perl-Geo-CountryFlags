#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Geo
%define	pnam	CountryFlags
Summary:	Geo::CountryFlags - methods to fetch flag GIFs
Summary(pl):	Geo::CountryFlags - metody do uzyskiwania GIFów z flagami
Name:		perl-Geo-CountryFlags
Version:	0.01
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	714b64ae9bdb2b224f086263c065bf71
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Geo::CountryFlags provides methods to display/retrieve flag GIFs from
the web site of the Central Intelligence Agency. Permanently caches a
local copy of the flag if it is not already present.

The flags for all country codes as of module publication are included
in the %{_datadir}/%{pdir}-%{pnam} directory. However, if LWP::Simple
(perl-libwww package) is installed, Geo::CountryFlags will fetch them
as needed and store them in ./flags [default] or the directory of you
choice.

%description -l pl
Modu³ Geo::CountryFlags udostêpnia metody do wy¶wietlania/uzyskiwania
GIFów z flagami ze strony WWW Central Intelligence Agency. Po
¶ci±gniêciu flagi zachowuje j± lokalnie.

Flagi wszystkich krajów z czasu wydania modu³u zosta³y za³±czone w
katalogu %{_datadir}/%{pdir}-%{pnam}. Je¶li zainstalowany jest modu³
LWP::Simple (pakiet perl-libwww), Geo::CountryFlags mo¿e ¶ci±gaæ flagi
i zapisywaæ je w ./flags (domy¶lnie) lub wybranym katalogu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{pdir}-%{pnam}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install flags/*.gif $RPM_BUILD_ROOT%{_datadir}/%{pdir}-%{pnam}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Geo
%{perl_vendorlib}/Geo/CountryFlags.pm
%{_datadir}/%{pdir}-%{pnam}
%{_mandir}/man3/*
