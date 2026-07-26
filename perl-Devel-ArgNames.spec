%define upstream_name    Devel-ArgNames
Name:		perl-%{upstream_name}
Version:	0.03
Release:	7

Summary:	Figure out the names of variables passed into subroutines
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Devel-ArgNames
Source0:	https://cpan.metacpan.org/authors/id/N/NU/NUFFIN/Devel-ArgNames-%{version}.tar.gz

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
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 653405
- rebuild for updated spec-helper

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 561557
- import perl-Devel-ArgNames


* Tue Jul 27 2010 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist
