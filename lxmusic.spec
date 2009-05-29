Summary:	Lightweight XMMS2 GUI frontend
Name:     	lxmusic
Version:	0.3.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
URL:		http://www.lxde.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel >= 2.0
Buildrequires:	xmms2-devel >= 0.6
BuildRequires:	intltool
Requires:	xmms2 >= 0.6

%description
LXMusic is a simple GUI XMMS2 client with minimal functionality.
It can do nothing more than playing music files.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %buidlroot
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf %buidlroot

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
