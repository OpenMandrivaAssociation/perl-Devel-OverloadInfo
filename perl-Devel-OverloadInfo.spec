%define	modname	Devel-OverloadInfo
%define	modver	0.005

Summary:	Perl module for introspecting overloaded operators
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/I/IL/ILMARI/Devel-OverloadInfo-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Perl module for introspecting overloaded operators

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Devel
%{_mandir}/man3*/*
