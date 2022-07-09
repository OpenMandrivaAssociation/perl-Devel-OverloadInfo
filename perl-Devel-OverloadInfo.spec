%define modname Devel-OverloadInfo
%define modver 0.007

Summary:	Perl module for introspecting overloaded operators
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		http://metacpan.org/pod/Devel::OverloadInfo
Source0:	http://search.cpan.org/CPAN/authors/id/I/IL/ILMARI/Devel-OverloadInfo-%{modver}.tar.gz
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
%autosetup -n %{modname}-%{modver} -p1

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
