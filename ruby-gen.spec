%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"])')
%define	ruby_version	%(ruby -r rbconfig -e 'print Config::CONFIG["ruby_version"]')
Summary:	Gen library for Nitro + Og
Summary(pl):	Biblioteka Gen dla Nitro + Og
Name:		ruby-Gen
%define tarname gen
Version:	0.24.0
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/download.php/6768/%{tarname}-%{version}.tgz
# Source0-md5:	4dba19c84b3e2dc3a21642f14c1060c9
URL:		http://nitrohq.com/
BuildRequires:	ruby
Requires:	ruby
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Gen for Nitro + Og.

%description -l pl
Ten pakiet zawiera bibliotekê Gen dla Nitro + Og.

%prep
%setup -q -n %{tarname}-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{ruby_rubylibdir},%{ruby_ridir},%{_examplesdir}/%{name}-%{version}}
install bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README doc/*
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*
%{ruby_ridir}/Gen
