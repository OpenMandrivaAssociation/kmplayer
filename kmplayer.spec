Name:		kmplayer
Version:	0.11.3c
Release:	2
Summary:	A multimedia mplayer/phonon frontend for KDE
License:	GPLv2+
Group:		Video
Url:		http://kmplayer.kde.org/
Source0:	http://kmplayer.kde.org/pkgs/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	libnspr-devel
BuildRequires:	gtk2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libxt-devel
Obsoletes:	kde4-%{name} < 0.11.0-0.rc2.5
Suggests:	mplayer

%description
KMPlayer can play all the audio/video supported by mplayer/phonon from local
file or url, be embedded inside Konqueror and KHTML and play DVD's.

%files -f %{name}.lang
%doc ChangeLog README
%{_kde_bindir}/%{name}
%{_kde_bindir}/kphononplayer
%{_kde_datadir}/apps/%{name}
%{_kde_services}/*.desktop
%{_kde_configdir}/%{name}rc
%{_kde_libdir}/*.so
%{_kde_libdir}/kde4/*.so
%{_kde_iconsdir}/hicolor/*/*/*
%{_kde_applicationsdir}/%{name}.desktop
%{_docdir}/HTML/en/%{name}/common
%{_docdir}/HTML/en/%{name}/index*

#--------------------------------------------------------------------

%package	npplayer
Group:		Video
Summary:	Kmplayer netscape plugin player
Requires:	%{name}

%description	npplayer
Kmplayer netscape plugin player.

%files npplayer
%doc AUTHORS ChangeLog README
%{_kde_bindir}/knpplayer
#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}

# fix .desktop file
desktop-file-install \
		--vendor="" \
		--remove-mime-type="uri/mms;uri/pnm;uri/rtspt;uri/rtspu" \
		--dir %{buildroot}%{_kde_applicationsdir} %{buildroot}%{_kde_applicationsdir}/%{name}.desktop

%check
for f in %{buildroot}%{_kde_datadir}/applications/kde4/*.desktop ; do
     desktop-file-validate $f
done


%changelog
* Thu Mar 15 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.11.3c-1mdv2012.0
+ Revision: 785040
- version update 0.11.3c

* Tue Feb 14 2012 Andrey Bondrov <abondrov@mandriva.org> 0.11.3b-1
+ Revision: 774033
- Add patch to fix DSO issue, don't use find_lang as locales are not built (they cause problems)
- New version 0.11.3b

* Fri Nov 11 2011 Andrey Bondrov <abondrov@mandriva.org> 0.11.3a-1
+ Revision: 730005
- Update patch0
- Add patch0 to deal with new glib issues
- New version 0.11.3a

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.11.2c-2
+ Revision: 677490
- br xt
- rebuild for updated mimehandler

* Mon Oct 04 2010 Funda Wang <fwang@mandriva.org> 0.11.2c-1mdv2011.0
+ Revision: 583014
- update to new version 0.11.2c

* Sun Apr 25 2010 Funda Wang <fwang@mandriva.org> 0.11.2b-1mdv2010.1
+ Revision: 538567
- update to new version 0.11.2b

* Tue Apr 20 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.11.2a-2mdv2010.1
+ Revision: 537273
- suggest, only suggest, mplayer
- add dbus-glib-devel back, needed for older releases
- remove redundant BR, dbus-glib-devel is already required by kdelibs4-devel

* Mon Mar 22 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.11.2a-1mdv2010.1
+ Revision: 526359
- new upstream release (fixes mdv bug#58045)
- add new check as per new kde policy

* Thu Mar 18 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.11.2-2mdv2010.1
+ Revision: 524966
- clean spec
- fix .deksktop file

* Sun Mar 07 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.11.2-1mdv2010.1
+ Revision: 515522
- update to 0.11.2
- Fix mixed-use-of-spaces-and-tabs

* Thu Jun 18 2009 Funda Wang <fwang@mandriva.org> 0.11.1b-1mdv2010.0
+ Revision: 386901
- New version 0.11.1b

* Sun May 17 2009 Funda Wang <fwang@mandriva.org> 0.11.1a-1mdv2010.0
+ Revision: 376677
- New version 0.11.1a

* Mon May 11 2009 Funda Wang <fwang@mandriva.org> 0.11.1-1mdv2010.0
+ Revision: 374113
- New version 0.11.1

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove unneeded macros

* Mon Jan 26 2009 Funda Wang <fwang@mandriva.org> 0.11.0a-1mdv2009.1
+ Revision: 333584
- new version 0.11.0a

* Tue Sep 30 2008 Helio Chissini de Castro <helio@mandriva.com> 0.11.0-0.rc4.4mdv2009.0
+ Revision: 290272
- Fix crash on dolphin due invalid location of desktop file.

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.11.0-0.rc4.3mdv2009.0
+ Revision: 264766
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Jun 06 2008 Funda Wang <fwang@mandriva.org> 0.11.0-0.rc4.2mdv2009.0
+ Revision: 216400
- compile using new LDFLAGS
- New version 0.11.0 rc4

* Thu May 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.11.0-0.rc2.6mdv2009.0
+ Revision: 210130
- Fix Obsoletes
- Fix name
- Fix spec file name
- Use kde4 app by default

* Sat Mar 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.11.0-0.rc2.4mdv2008.1
+ Revision: 182317
- Rebuild against new qt4 changes

* Sat Mar 01 2008 Funda Wang <fwang@mandriva.org> 0.11.0-0.rc2.3mdv2008.1
+ Revision: 177098
- add conflicts on kmplayer3

* Fri Feb 08 2008 Funda Wang <fwang@mandriva.org> 0.11.0-0.rc2.2mdv2008.1
+ Revision: 164103
- fix conflict with oxygen-icon-theme

* Mon Jan 28 2008 Funda Wang <fwang@mandriva.org> 0.11.0-0.rc2.1mdv2008.1
+ Revision: 159053
- New version 0.11.0 rc2

* Sun Jan 20 2008 Funda Wang <fwang@mandriva.org> 0.11.0-0.rc1.1mdv2008.1
+ Revision: 155249
- BR dbus-glib
- reword summary
- import souorce and spec
- Created package structure for kde4-kmplayer.

