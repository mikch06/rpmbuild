Name:           test
Version:        0.1
Release:        1%{?dist}
Summary:        A rpm build test 

License:       no 
URL:           no 
#BuildArch:	noarch
Source0:       %{name}-%{version}.tar.gz 

#BuildRequires:  bash
Requires:       bash

%description
Build an rpm

%prep
%autosetup

%install
install -m 0755 test1.sh /tmp/test1.sh

%files
/tmp/tmp/test1.sh

%changelog
* Sat Oct 22 2022 mik <mail@kissel.ch>
- 
