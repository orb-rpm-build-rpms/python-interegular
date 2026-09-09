Name:           python-interegular
Version:        0.3.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        a regex intersection checker

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/MegaIng/regex_intersections
Source:         %{pypi_source interegular}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'interegular' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-interegular
Summary:        %{summary}

%description -n python3-interegular %_description


%prep
%autosetup -p1 -n interegular-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files -l interegular


%check
%pyproject_check_import


%files -n python3-interegular -f %{pyproject_files}


%changelog
%autochangelog
