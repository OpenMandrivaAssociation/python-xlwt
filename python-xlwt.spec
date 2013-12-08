%define	oname	xlwt

Name:		python-%{oname}
Version:	0.7.5
Release:	1
Summary:	Library to create spreadsheet 
Source0:	http://pypi.python.org/packages/source/x/%{oname}/%{oname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://www.python-excel.org/
BuildArch:	noarch
BuildRequires:	python-setuptools

%description
xlwt is a library for generating spreadsheet files that are compatible
with Excel 97/2000/XP/2003, OpenOffice.org Calc, and Gnumeric. xlwt has
full support for Unicode. Excel spreadsheets can be generated on any
platform without needing Excel or a COM server. The only requirement is
Python 2.3 to 2.7.

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

pushd %{buildroot}%{py_puresitedir}/xlwt/examples
find . -name "*.py" |xargs chmod +x
chmod -x {wsprops,simple,parse-fmla,xlwt_easyxf_simple_demo,protection}.py
popd
chmod +x %{buildroot}%{py_puresitedir}/xlwt/Formatting.py

%files
%doc xlwt/doc/xlwt.html
%{py_puresitedir}/xlwt/doc/xlwt.html
%{py_puresitedir}/xlwt/*.py*
%{py_puresitedir}/xlwt*.egg-info
%{py_puresitedir}/xlwt/examples/*.py
%{py_puresitedir}/xlwt/examples/python.bmp
