# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate primes

Name:           rust-primes
Version:        0.3.0
Release:        %autorelease
Summary:        Package for calculating primes using the Sieve of Eratosthenes, and using that to check if a number is prime and calculating factors

License:        BSD-3-Clause
URL:            https://crates.io/crates/primes
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A package for calculating primes using the Sieve of Eratosthenes, and
using that to check if a number is prime and calculating factors.
Includes an iterator over all primes.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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
