%define	fontname	tibetan-machine-uni

Name:		%{fontname}-fonts
Version:	1.901
Release:	5%{?dist}
Summary:	Tibetan Machine Uni font for Tibetan, Dzongkha and Ladakhi

Group:		User Interface/X
# .ttf file now states GPLv3+ with fonts exceptions
License:	GPLv3+ with exceptions
URL:		http://www.thlib.org/tools/#wiki=/access/wiki/site/26a34146-33a6-48ce-001e-f16ce7908a6a/tibetan%20machine%20uni.html
Source0:	https://collab.itc.virginia.edu/access/content/group/26a34146-33a6-48ce-001e-f16ce7908a6a/Tibetan%20fonts/Tibetan%20Unicode%20Fonts/TibetanMachineUnicodeFont.zip
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
Tibetan Machine Uni is an TrueType OpenType, Unicode font released by THDL
project. The font supports Tibetan, Dzongkha and Ladakhi in dbu-can script
with full support for the Sanskrit combinations found in chos skad text.

%prep
%setup -q -c

%build
# Empty build section

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

tr -d '\r' < gpl.txt > COPYING
tr -d '\r' < ReadMe.txt > README

%clean
rm -fr %{buildroot}

%_font_pkg *.ttf
%doc COPYING README
%dir %{_fontdir}

%changelog
* Thu Feb 11 2010 Jens Petersen <petersen@redhat.com> - 1.901-5
- license in the font is now GPLv3+ (with fonts exception) (#563834)

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.901-4.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.901-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 15 2009 Marcin Garski <mgarski[AT]post.pl> 1.901-3
- Update to 1.901b
- Update URL
- Update to new fonts guidelines, thanks to Rajeesh (#477467)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.901-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 29 2007 Marcin Garski <mgarski[AT]post.pl> 1.901-1
- Update to 1.901

* Fri Aug 31 2007 Marcin Garski <mgarski[AT]post.pl> 1.0-2
- Fix license tag
- Update URL

* Mon Mar 12 2007 Marcin Garski <mgarski[AT]post.pl> 1.0-1
- Initial specfile
