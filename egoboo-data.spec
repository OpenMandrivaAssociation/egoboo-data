%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define oname	egoboo

Summary:	Data files for egoboo
Name:		%{oname}-data
Version:	2.7.7
Release:	%mkrel 2
Epoch:		1
License:	GPL
Group:		Games/Adventure
URL:		http://egoboo.sourceforge.net/
Source0:	http://downloads.sourceforge.net/egoboo/%{name}-%{version}.tar.lzma
Requires:	%{oname} = %{epoch}:%{version}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Egoboo is an open source project, using OpenGL and SDL(Simple
DirectMedia Layer) libraries. It is a 3d dungeon role playing
game in the spirit of NetHack. Nice colorful graphics, and
detailed models(using Quake2 modeling tools) make this game
stand out in the gaming open-source community.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_gamesdatadir}/%{oname}
cp -r * %{buildroot}%{_gamesdatadir}/%{oname}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_gamesdatadir}/%{oname}
