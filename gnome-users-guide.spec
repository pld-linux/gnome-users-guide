%define  ver     1.0.5
%define  rel     4rh
%define  prefix  /usr

Summary: The GNOME Users' Guide.
Name: gnome-users-guide
Version: %ver
Release: %rel
Copyright: GPL
Group: Documentation
Source: users-guide-%{PACKAGE_VERSION}-rh.tar.gz
Source1: users-guide-%{PACKAGE_VERSION}-de.tar.gz

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Docdir: %{prefix}/doc
BuildArchitectures: noarch

%description
This package will install the users' guide for the
GNOME Desktop Environment on your computer.

You should install this package if you are going to
use GNOME and you want a quick, handy reference.

%prep
%setup -n users-guide-%{PACKAGE_VERSION}

%build
./configure --prefix=%{prefix}

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/%{prefix} install 

# hack de into this for now
cd $RPM_BUILD_ROOT/%{prefix}/share/gnome/help/users-guide
tar xzf %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README ChangeLog 
%{prefix}/share/gnome/help/users-guide/C
%lang(de) %{prefix}/share/gnome/help/users-guide/de
