Name:		fcos-cmk-plugins           
Version:        1
Release:        0
Summary:        Checkmk plugins for FCOS
License:	no 
BuildArch:	noarch

Source0:	%{name}-%{version}.tar.gz

%description
%{summary}

%prep

%setup -q 

%build

%install

echo %{buildroot}
plg_dir=%{buildroot}/usr/lib/check_mk_agent/plugins/

mkdir -p %{buildroot}
mkdir -p $plg_dir

cp -R * $plg_dir

%files
/usr/lib/check_mk_agent/plugins/mk_inventory.linux
%config /usr/lib/check_mk_agent/plugins/mk_docker.py


%changelog
* Tue Oct 25 2022 mik <mail@kissel.ch>
- Initial

