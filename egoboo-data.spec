%define oname	egoboo

Summary:	Data files for egoboo
Name:		%{oname}-data
Version:	2.8.1
Release:	1
Epoch:		1
License:	GPL
Group:		Games/Adventure
URL:		http://egoboo.sourceforge.net/
Source0:	http://downloads.sourceforge.net/egoboo/%{name}-%{version}.tar.xz
Requires:	%{oname} = %{epoch}:%{version}
BuildArch:	noarch

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
install -d %{buildroot}%{_gamesdatadir}/%{oname}
cp -r basicdat modules %{buildroot}%{_gamesdatadir}/%{oname}

%files
%defattr(644,root,root,755)
%dir %{_gamesdatadir}/%{oname}
%{_gamesdatadir}/%{oname}/basicdat
%{_gamesdatadir}/%{oname}/modules
