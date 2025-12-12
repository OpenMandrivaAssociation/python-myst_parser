Name:		python-myst_parser
Version:	4.0.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/m/myst_parser/myst_parser-%{version}.tar.gz
Summary:	An extended [CommonMark](https://spec.commonmark.org/) compliant parser
URL:		https://pypi.org/project/myst_parser/
License:	None
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
An extended [CommonMark](https://spec.commonmark.org/) compliant parser

%prep
%autosetup -p1 -n myst_parser-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/*
%{py_sitedir}/myst_parser
%{py_sitedir}/myst_parser-*.*-info
