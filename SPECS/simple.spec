Name: hello_world
Version: 1.0.0 
Release: 1 
Summary: The show must go on
License: no
BuildRoot: /var/tmp/%{name}-buildroot 

%description
This is it this is now


%files
%defattr(700, root, root) /opt/hello_world/hello_world  

%preun 
 echo "the pre-uninstall sh commands" 

%postun 
 echo "the post-uninstall sh commands"
