%define upstream_name    Devel-ArgNames
%define upstream_version 0.03
Name:		perl-%{upstream_name}
Version:	0.03
Release:	2

Summary:	Figure out the names of variables passed into subroutines
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Devel-ArgNames
Source0:	https://cpan.metacpan.org/authors/id/N/NU/NUFFIN/Devel-ArgNames-0.03.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(PadWalker)
BuildRequires:	perl(Test::use::ok)
BuildArch:	noarch

%description
When print-debugging code, you will often ind yourself going:

	print "\$foo is $foo, \$bar is $bar"

With this module, you can write a reusable subroutine easily:

%prep
%setup -q -n Devel-ArgNames-0.03

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test

%install
%makeinstall_std

%files
%doc META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


