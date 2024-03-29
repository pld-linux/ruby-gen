%define pkgname gen
Summary:	Gen library for Nitro + Og
Summary(pl.UTF-8):	Biblioteka Gen dla Nitro + Og
Name:		ruby-%{pkgname}
Version:	0.25.0
Release:	2
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/download.php/7167/%{pkgname}-%{version}.zip
# Source0-md5:	ff6a5cabc188ef3cc6f57cac29f22fd8
URL:		http://nitrohq.com/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	unzip
%{?ruby_mod_ver_requires_eq}
Provides:	ruby-Gen
Obsoletes:	ruby-Gen
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Gen for Nitro + Og.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę Gen dla Nitro + Og.

%prep
%setup -q -n %{pkgname}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{ruby_rubylibdir},%{ruby_ridir},%{_examplesdir}/%{name}-%{version}}
install bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README doc/*
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*
%{ruby_ridir}/Gen
