# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		sarge
%define		egg_name	sarge
%define		pypi_name	sarge
Summary:	A wrapper for subprocess which provides command pipeline functionality
Name:		python-%{module}
Version:	0.1.7
Release:	2
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.debian.net/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	91477365bb9327e377e98272004aaab4
URL:		https://github.com/vsajip/sarge
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The sarge package provides a wrapper for subprocess which provides
command pipeline functionality.

This package leverages subprocess to provide easy-to-use
cross-platform command pipelines with a POSIX flavour: you can have
chains of commands using ;, &, pipes using | and |&, and redirection.

%package -n python3-%{module}
Summary:	A wrapper for subprocess which provides command pipeline functionality
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
The sarge package provides a wrapper for subprocess which provides
command pipeline functionality.

This package leverages subprocess to provide easy-to-use
cross-platform command pipelines with a POSIX flavour: you can have
chains of commands using ;, &, pipes using | and |&, and redirection.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=build-2/lib %{__python} test_sarge.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHON3PATH=build-3/lib %{__python3} test_sarge.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
