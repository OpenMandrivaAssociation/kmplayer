Name:		kmplayer
Version:	0.11.2c
Release:	%mkrel 1
Summary:	A multimedia mplayer/phonon frontend for KDE
License:	GPLv2+
Group:		Video
Url:		http://kmplayer.kde.org/
Source:		http://kmplayer.kde.org/pkgs/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdelibs4-devel
BuildRequires:	libnspr-devel
BuildRequires:	gtk2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	desktop-file-utils
Obsoletes:	kde4-%{name} < 0.11.0-0.rc2.5
Suggests:	mplayer

%description
KMPlayer can play all the audio/video supported by mplayer/phonon from local
file or url, be embedded inside Konqueror and KHTML and play DVD's.

%files -f %{name}.lang
%defattr(-,root,root)
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

#--------------------------------------------------------------------

%package	npplayer
Group:		Video
Summary:	Kmplayer netscape plugin player
Requires:	%{name}

%description	npplayer
Kmplayer netscape plugin player.

%files npplayer
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_kde_bindir}/knpplayer

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

# fix .desktop file
desktop-file-install \
		--vendor="" \
		--remove-mime-type="uri/mms;uri/pnm;uri/rtspt;uri/rtspu" \
		--dir %{buildroot}%{_kde_applicationsdir} %{buildroot}%{_kde_applicationsdir}/%{name}.desktop

%{find_lang} %{name} --with-html

%check
for f in %{buildroot}%{_kde_datadir}/applications/kde4/*.desktop ; do
     desktop-file-validate $f
done

%clean
rm -rf %{buildroot}
