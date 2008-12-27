Summary:	Software suspend 2 hibernate script
Summary(pl.UTF-8):	Skrypt hibernujący dla Software suspend 2
Name:		hibernate
Version:	1.99
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://tuxonice.net/downloads/all/%{name}-script-%{version}.tar.gz
# Source0-md5:	11832e77edc4a13330aaced8cea52dfb
URL:		http://www.tuxonice.net/
Requires:	kbd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hibernate is a shell script that handles the process of getting ready
to suspend to disk and to resume from disk. It requires the Software
Suspend 2 patches available at <http://www.suspend2.net/>.
After installing you will want to run 'hibernate -h' to see available
options and modify your /etc/hibernate/hibernate.conf to set them.

%description -l pl.UTF-8
hibernate to skrypt powłoki obsługujący proces przygotowania do
zachowania stanu na dysku (suspend to disk) i obudzenia z dysku.
Wymaga łat Software Suspend 2 dostępnych pod
<http://www.suspend2.net/>. Po zainstalowaniu 'hibernate -h' pokaże
dostępne opcje, które można ustawić w /etc/hibernate/hibernate.conf .

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
