Summary:	The GNOME Users' Guide
Summary(pl):	Podrêcznik u¿ytkownika GNOME
Name:		gnome-users-guide
Version:	1.2
Release:	1
License:	GPL
Group:		Documentation
Source0:	http://ftp.gnome.org/pub/GNOME/sources/users-guide/1.2/users-guide-%{version}.tar.gz
URL:		http://www.gnome.org/users-guide/project.shtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch


%description
This package will install the users' guide for the GNOME Desktop
Environment on your computer.

You should install this package if you are going to use GNOME and you
want a quick, handy reference.

%description -l pl
Ten pakiet zawiera podrêcznik u¿ytkownika do GNOME.

%prep
%setup -q -n users-guide-%{version}

%build
%configure2_13

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{makeinstall}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%{_datadir}/gnome/help/users-guide/C
