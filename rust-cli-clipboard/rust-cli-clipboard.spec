# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate cli-clipboard

Name:           rust-cli-clipboard
Version:        0.4.0
Release:        %autorelease
Summary:        Cross-platform library for getting and setting the contents of the OS-level clipboard

# Upstream license specification: MIT / Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cli-clipboard
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          cli-clipboard-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Cli-clipboard is a cross-platform library for getting and setting the
contents of the OS-level clipboard.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.apache2
%license %{crate_instdir}/LICENSE.mit
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