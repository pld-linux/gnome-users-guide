Summary:	The GNOME Users' Guide
Name:		gnome-users-guide
Version:	1.0.5
Release:	4
License:	GPL
Group:		Documentation
Group(pl):	Dokumentacja
Source0:	users-guide-%{PACKAGE_VERSION}-rh.tar.gz
Source1:	users-guide-%{PACKAGE_VERSION}-de.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
This package will install the users' guide for the GNOME Desktop
Environment on your computer.

You should install this package if you are going to use GNOME and you
want a quick, handy reference.

%prep
%setup -q -n users-guide-%{PACKAGE_VERSION}

%build
./configure --prefix=%{_prefix}

%install

rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT/%{_prefix} install 

# hack de into this for now
cd $RPM_BUILD_ROOT/%{_datadir}/gnome/help/users-guide
tar xzf %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog 
%{_datadir}/gnome/help/users-guide/C
%lang(de) %{_datadir}/gnome/help/users-guide/de
