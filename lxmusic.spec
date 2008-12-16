Summary:	Lightweight XMMS2 GUI frontend
Name:     	lxmusic
Version:	0.2.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel xmms2-devel
Requires:	xmms2

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
%{_datadir}/applications/*.desktop
%{_iconsdir}/*/*/*/*
