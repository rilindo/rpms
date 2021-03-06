# $Id$
# Authority: cmr
# Upstream: Rafael Kitover <rkitover@io.com>
# el4 ships /usr/share/man/man3/Carp::Clan.3pm.gz inside perl-Date-Calc!
# and we need a new Carp::Clan here
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-Types

Summary: Organise your Moose types in libraries
Name: perl-MooseX-Types
Version: 0.21
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Types/

Source: http://search.cpan.org/CPAN/authors/id/R/RK/RKITOVER/MooseX-Types-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
BuildRequires: perl(Carp::Clan) >= 6.00
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(FindBin)
BuildRequires: perl(Moose) >= 0.91
BuildRequires: perl(Scalar::Util) >= 1.19
BuildRequires: perl(Sub::Install) >= 0.924
BuildRequires: perl(Sub::Name)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Moose)
#BuildRequires: perl(Test::More) >= 0.80
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::clean) >= 0.08
BuildRequires: perl >= 5.8.0
Requires: perl(Carp)
Requires: perl(Carp::Clan) >= 6.00
Requires: perl(Moose) >= 0.93
Requires: perl(Scalar::Util) >= 1.19
Requires: perl(Sub::Install) >= 0.924
Requires: perl(Sub::Name)
Requires: perl(namespace::clean) >= 0.08
Requires: perl >= 5.8.0

%filter_from_requires /^perl*/d
%filter_setup

%description
Organise your Moose types in libraries.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/MooseX::Types.3pm*
%doc %{_mandir}/man3/MooseX::Types*.3pm*
%dir %{perl_vendorlib}/MooseX/
%{perl_vendorlib}/MooseX/Types/
%{perl_vendorlib}/MooseX/Types.pm

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.21-1
- Updated to version 0.21.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.20-2
- Updated to version 0.20.

* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.17-1
- Updated to version 0.17.

* Wed Jul 22 2009 Christoph Maser <cmr@financial.com> - 0.16-1
- Updated to version 0.16.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Initial package. (using DAR)
