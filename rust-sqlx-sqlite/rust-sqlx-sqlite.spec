# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate sqlx-sqlite

Name:           rust-sqlx-sqlite
Version:        0.7.4
Release:        %autorelease
Summary:        SQLite driver implementation for SQLx

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sqlx-sqlite
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
SQLite driver implementation for SQLx. Not for direct use; see the
`sqlx` crate for details.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
# FIXME: no license files detected
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+any-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+any-devel %{_description}

This package contains library source intended for building other packages which
use the "any" feature of the "%{crate}" crate.

%files       -n %{name}+any-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+chrono-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+chrono-devel %{_description}

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%files       -n %{name}+chrono-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+json-devel %{_description}

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%files       -n %{name}+json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+migrate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+migrate-devel %{_description}

This package contains library source intended for building other packages which
use the "migrate" feature of the "%{crate}" crate.

%files       -n %{name}+migrate-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+offline-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+offline-devel %{_description}

This package contains library source intended for building other packages which
use the "offline" feature of the "%{crate}" crate.

%files       -n %{name}+offline-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+regexp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regexp-devel %{_description}

This package contains library source intended for building other packages which
use the "regexp" feature of the "%{crate}" crate.

%files       -n %{name}+regexp-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+time-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+time-devel %{_description}

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%files       -n %{name}+time-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+uuid-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+uuid-devel %{_description}

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%files       -n %{name}+uuid-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
