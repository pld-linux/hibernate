Summary:	Software suspend 2 hibernate script
Summary(pl):	Skrypt hibernuj�cy dla Software suspend 2
Name:		hibernate
Version:	1.12
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://suspend2.net/downloads/all/%{name}-script-%{version}.tar.gz
# Source0-md5:	0fb7c524a30daacf200f27de2e398646
URL:		http://www.suspend2.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hibernate is a shell script that handles the process of getting ready
to suspend to disk and to resume from disk. It requires the Software
Suspend 2 patches available at <http://www.suspend2.net/>.
After installing you will want to run 'hibernate -h' to see available
options and modify your /etc/hibernate/hibernate.conf to set them.

%description -l pl
hibernate to skrypt pow�oki obs�uguj�cy proces przygotowania do
zachowania stanu na dysku (suspend to disk) i obudzenia z dysku.
Wymaga �at Software Suspend 2 dost�pnych pod
<http://www.suspend2.net/>. Po zainstalowaniu 'hibernate -h' poka�e
dost�pne opcje, kt�re mo�na ustawi� w /etc/hibernate/hibernate.conf .

%prep
%setup -q -n %{name}-script-%{version}

%install
rm -rf $RPM_BUILD_ROOT

BASE_DIR=$RPM_BUILD_ROOT \
PREFIX=%{_prefix} \
MAN_DIR=$RPM_BUILD_ROOT%{_mandir} \
sh ./install.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG COPYING SCRIPTLET-API
%attr(755,root,root) %{_sbindir}/hibernate
%{_datadir}/hibernate
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/hibernate
%{_mandir}/man?/*
