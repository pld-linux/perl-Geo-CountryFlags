#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Geo
%define		pnam	CountryFlags
Summary:	Geo::CountryFlags - methods to fetch flag GIFs
Summary(pl.UTF-8):   Geo::CountryFlags - metody do uzyskiwania GIFów z flagami
Name:		perl-Geo-CountryFlags
Version:	0.02
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2af4c15fbcaf211a1a71adc566e4718c
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
Moduł Geo::CountryFlags udostępnia metody do wyświetlania/uzyskiwania
GIFów z flagami ze strony WWW Central Intelligence Agency. Po
ściągnięciu flagi zachowuje ją lokalnie.

Flagi wszystkich krajów z czasu wydania modułu zostały załączone w
katalogu %{_datadir}/%{pdir}-%{pnam}. Jeśli zainstalowany jest moduł
LWP::Simple (pakiet perl-libwww), Geo::CountryFlags może ściągać flagi
i zapisywać je w ./flags (domyślnie) lub wybranym katalogu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

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
