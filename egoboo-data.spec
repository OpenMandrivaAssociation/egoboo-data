%define oname	egoboo

Summary:	Data files for egoboo
Name:		%{oname}-data
Version:	2.8.1
Release:	2
Epoch:		1
License:	GPLv3+
Group:		Games/Adventure
URL:		https://egoboo.sourceforge.net/
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


%changelog
* Sun Jan 22 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:2.8.1-1
+ Revision: 765023
- update license
- ditch no longer required macros to disable debug packages
- fix file permissions
- drop legacy rpm junk
- new version

* Thu Sep 23 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:2.8.0-1mdv2011.0
+ Revision: 580680
- new release: 2.8.0

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1:2.7.7-2mdv2010.0
+ Revision: 437399
- rebuild

* Sun Nov 30 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:2.7.7-1mdv2009.1
+ Revision: 308495
- update to new version 2.7.7
- spec file clean

* Fri Aug 01 2008 Funda Wang <fwang@mandriva.org> 1:2.6.4-1mdv2009.0
+ Revision: 259644
- fix tarball dir
- New version 2.6.4

* Fri Aug 01 2008 Funda Wang <fwang@mandriva.org> 1:2.6.3b-2mdv2009.0
+ Revision: 259528
- fix requires

* Tue Jul 15 2008 Funda Wang <fwang@mandriva.org> 1:2.6.3b-1mdv2009.0
+ Revision: 235726
- raise epoch
- New version 2.6.3b

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 2.220-2mdv2008.1
+ Revision: 140728
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.220-2mdv2008.0
+ Revision: 89632
- rebuild

  + Emmanuel Andry <eandry@mandriva.org>
    - Import egoboo-data



* Mon Aug 28 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.220-1mdv2007.0
- initial package split out from egoboo
