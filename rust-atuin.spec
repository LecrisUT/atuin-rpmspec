# Generated by rust2rpm 26
%bcond_without check

%global crate atuin

Name:           rust-atuin
Version:        18.1.0
Release:        %autorelease
Summary:        magical shell history

License:        MIT
URL:            https://crates.io/crates/atuin
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Atuin replaces your existing shell history with a SQLite database, and records additional context for your commands. Additionally, it provides optional and fully encrypted synchronisation of your history between machines, via an Atuin server.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        MIT
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/atuin
%{_datadir}/bash-completion/completions/atuin
%{_datadir}/fish/completions/atuin
%{_datadir}/zsh/site-functions/atuin
%config %{_sysconfdir}/profile.d/atuin.sh

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install
# Generate all of the shell-completions
for completion in bash fish zsh; do
  %{buildroot}%{_bindir}/atuin gen-completions --shell $completion -o .
done
install -Dpm 644 atuin.bash %{buildroot}%{_datadir}/bash-completion/completions/atuin
install -Dpm 644 atuin.fish %{buildroot}%{_datadir}/fish/completions/atuin
install -Dpm 644 _atuin %{buildroot}%{_datadir}/zsh/site-functions/atuin

# Add atuin to default profile
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/atuin.sh <<EOF
$(%{buildroot}%{_bindir}/atuin init bash)
EOF

%if %{with check}
%check
# * These tests are skipped because they required a Postgres database to be
#   running, which is not possible in the build environment.
%cargo_test -- -- --skip sync --skip change_password --skip multi_user_test --skip registration
%endif

%changelog
%autochangelog
