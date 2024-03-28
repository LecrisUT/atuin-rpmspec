# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate tiny-bip39

Name:           rust-tiny-bip39
Version:        1.0.0
Release:        %autorelease
Summary:        Fork of the bip39 crate with fixes to v0.6

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tiny-bip39
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          tiny-bip39-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A fork of the bip39 crate with fixes to v0.6. Rust implementation of
BIP-0039.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+chinese-simplified-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+chinese-simplified-devel %{_description}

This package contains library source intended for building other packages which
use the "chinese-simplified" feature of the "%{crate}" crate.

%files       -n %{name}+chinese-simplified-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+chinese-traditional-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+chinese-traditional-devel %{_description}

This package contains library source intended for building other packages which
use the "chinese-traditional" feature of the "%{crate}" crate.

%files       -n %{name}+chinese-traditional-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+french-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+french-devel %{_description}

This package contains library source intended for building other packages which
use the "french" feature of the "%{crate}" crate.

%files       -n %{name}+french-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+italian-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+italian-devel %{_description}

This package contains library source intended for building other packages which
use the "italian" feature of the "%{crate}" crate.

%files       -n %{name}+italian-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+japanese-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+japanese-devel %{_description}

This package contains library source intended for building other packages which
use the "japanese" feature of the "%{crate}" crate.

%files       -n %{name}+japanese-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+korean-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+korean-devel %{_description}

This package contains library source intended for building other packages which
use the "korean" feature of the "%{crate}" crate.

%files       -n %{name}+korean-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+spanish-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+spanish-devel %{_description}

This package contains library source intended for building other packages which
use the "spanish" feature of the "%{crate}" crate.

%files       -n %{name}+spanish-devel
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
