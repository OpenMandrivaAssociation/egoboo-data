%define oname	egoboo
%define	name	%{oname}-data
%define version	2.220
%define	rel	2
%define release %mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}_%{version}.orig.tar.gz
License:	GPL
Group:		Games/Adventure
URL:		http://egoboo.sourceforge.net/
Summary:	Data files for egoboo
Requires:	%{oname} >= 2.22
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Egoboo is an open source project, using OpenGL and SDL(Simple
DirectMedia Layer) libraries. It is a 3d dungeon role playing
game in the spirit of NetHack. Nice colorful graphics, and
detailed models(using Quake2 modeling tools) make this game
stand out in the gaming open-source community.

%prep
%setup -q -n %{oname}

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
