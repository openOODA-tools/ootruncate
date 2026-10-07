Name:           ootruncate
Version:        0.1.0
Release:        1%{?dist}
Summary:        Shrinks or extends the length of specified files to exact byte counts.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ootruncate
Source0:        ootruncate-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ootruncate is a sovereign, capability-bounded FILE RESIZER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ootruncate
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ootruncate-uninstall

%files
/usr/bin/ootruncate
/usr/bin/ootruncate-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
