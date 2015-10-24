%define	oname	xlwt

Name:		python-%{oname}
Version:	1.0.0
Release:	2
Summary:	Library to create spreadsheet 
Source0:	http://pypi.python.org/packages/source/x/%{oname}/%{oname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://www.python-excel.org/
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools

%description
xlwt is a library for generating spreadsheet files that are compatible
with Excel 97/2000/XP/2003, OpenOffice.org Calc, and Gnumeric. xlwt has
full support for Unicode. Excel spreadsheets can be generated on any
platform without needing Excel or a COM server. The only requirement is
Python 2.6 to 3.4.

%package -n python2-%{oname}
Summary:     Library to create spreadsheet
Group:          Development/Python

%prep
%setup -q -n %{oname}-%{version}

pushd ..
cp -rp %{oname}-%{version} %{py2dir}

%build
python setup.py build

pushd %py2dir
python2 setup.py build

%install
python setup.py install --root=%{buildroot}

chmod +x %{buildroot}%{py_puresitedir}/xlwt/Formatting.py

pushd %py2dir
python2 setup.py install --root=%{buildroot}

%files
%{py_puresitedir}/xlwt
%{py_puresitedir}/xlwt*.egg-info

%files -n python2-%oname
%{py2_puresitedir}/xlwt
%{py2_puresitedir}/xlwt*.egg-info
