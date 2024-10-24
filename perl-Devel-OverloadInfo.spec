%define modname Devel-OverloadInfo

Summary:	Perl module for introspecting overloaded operators
Name:		perl-%{modname}
Version:	0.007
Release:	1
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		https://metacpan.org/pod/Devel::OverloadInfo
Source0:	http://search.cpan.org/CPAN/authors/id/I/IL/ILMARI/Devel-OverloadInfo-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	perl(Sub::Identify)
BuildRequires:	perl(MRO::Compat)
# For tests
BuildRequires:	perl(Package::Stash)
BuildRequires:	perl(Test::Fatal)

%description
Perl module for introspecting overloaded operators

%prep
%autosetup -n %{modname}-%{version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc README Changes
%{perl_vendorlib}/Devel
%doc %{_mandir}/man3*/*
