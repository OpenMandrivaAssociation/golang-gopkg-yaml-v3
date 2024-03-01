%global debug_package %{nil}

# Run tests in check section
%bcond_with check

# https://github.com/go-yaml/yaml
%global goipath		gopkg.in/yaml.v3
%global forgeurl	https://github.com/go-yaml/yaml
Version:			3.0.1

%gometa

Summary:	YAML support for the Go language
Name:		golang-gopkg-yaml-v3

Release:	1
Source0:	https://github.com/go-yaml/yaml/archive/v%{version}/yaml-%{version}.tar.gz
URL:		https://github.com/go-yaml/yaml
License:	GPL
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
%if %{with check}
BuildRequires:	golang(gopkg.in/check.v1)
%endif

%description
The yaml package enables Go programs to comfortably encode
and decode YAML values. It was developed within Canonical
as part of the juju project, and is based on a pure Go port
of the well-known libyaml C library to parse and generate
YAML data quickly and reliably.

Specifically, as of v3 of the yaml package:

 *  YAML 1.1 bools (yes/no, on/off) are supported as long as
    they are being decoded into a typed bool value. Otherwise
    they behave as a string. Booleans in YAML 1.2 are true/false
    only.
 *  Octals encode and decode as 0777 per YAML 1.1, rather than
    0o777 as specified in YAML 1.2, because most parsers still
    use the old format. Octals in the 0o777 format are supported
    though, so new files work.
 *  Does not support base-60 floats. These are gone from YAML 1.2,
    and were actually never supported by this package as it's
    clearly a poor choice.

The yaml package supports most of YAML 1.2, but preserves
some behavior from 1.1 for backwards compatibility.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc NOTICE

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n yaml-%{version}

%build
%gobuildroot
for cmd in $(ls -1 cmd) ; do
	%gobuild -o _bin/$cmd %{goipath}/cmd/$cmd
done

%install
%goinstall
for cmd in $(ls -1 _bin) ; do
  install -Dpm 0755 _bin/$cmd %{buildroot}%{_bindir}/$cmd
done

%check
%if %{with check}
%gochecks
%endif

