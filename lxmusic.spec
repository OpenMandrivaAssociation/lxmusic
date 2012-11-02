Summary:	Lightweight XMMS2 GUI frontend
Name:     	lxmusic
Version:	0.4.5
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
Patch1:		lxmusic-0.4.5-libnotify-0.7.0.patch
# https://sourceforge.net/tracker/?func=detail&atid=894869&aid=3038938&group_id=180858
# Patch at http://paste.lisp.org/display/116965/1,1/raw
Patch2:		lxmusic-0.4.4-fix-segfault-in-xmmsv_get_int.patch
URL:		http://www.lxde.org/
BuildRequires:	gtk+2-devel >= 2.0
Buildrequires:	xmms2-devel >= 0.8
BuildRequires:	intltool
Requires:	xmms2 >= 0.8

%description
LXMusic is a simple GUI XMMS2 client with minimal functionality.
It can do nothing more than playing music files.

%prep
%setup -q
%patch1 -p1 -b .libnotify-0.7.0~
%patch2 -p1 -b .segfault-in-xmmsv_get_int~

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
