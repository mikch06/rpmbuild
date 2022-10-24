Name:		cmk-plugins           
Version:        1
Release:        0
Summary:        Build rpm of Checkmk plugins
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
plg_dir=%{buildroot}/opt/cmk/plg
cfg_dir=%{buildroot}/opt/cmk/cfg

mkdir -p %{buildroot}
mkdir -p $plg_dir
mkdir -p $cfg_dir

cp -R * $plg_dir

%files
/opt/cmk/plg/mk_inventory.linux
/opt/cmk/plg/mk_docker.py


%changelog
* Sat Oct 22 2022 mik <mail@kissel.ch>
- 
