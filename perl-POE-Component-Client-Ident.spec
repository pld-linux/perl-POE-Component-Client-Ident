#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	POE
%define	pnam	Component-Client-Ident
Summary:	POE::Filter::Ident - A POE-based parser for the Ident protocol
Summary(pl.UTF-8):	POE::Filter::Ident - oparty na POE analizator protokołu Ident
Name:		perl-POE-Component-Client-Ident
Version:	1.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cfe5b1e3658df5455ed43526325b239a
URL:		http://search.cpan.org/dist/POE-Component-Client-Ident/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 0.0607
BuildRequires:	perl-Test-POE-Server-TCP
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Filter::Ident takes lines of raw Ident input and turns them into
weird little data structures, suitable for feeding to
POE::Component::Client::Ident::Agent. They look like this: 

{ name => 'event name', args => [ some info about the event ] }

%description -l pl.UTF-8
POE::Filter::Ident przyjmuje linie surowego wejścia od Identa i
zamienia je na dziwne małe struktury danych, nadające się do
przekazywania do modułu POE::Component::Client::Ident::Agent.
Wyglądają tak:

{ name => 'nazwa zdarzenia', args => [ informacja o zdarzeniu ] }

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/Client/*.pm
%{perl_vendorlib}/POE/Component/Client/Ident
%{perl_vendorlib}/POE/Filter/Ident.pm
%{_mandir}/man3/*
