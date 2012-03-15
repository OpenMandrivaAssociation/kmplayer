Name:		kmplayer
Version:	0.11.3c
Release:	%mkrel 1
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
