Name:           hello_project
Version:        1.0.1
Release:        1%{?dist}
Summary:        Test task in RAIDIX
BuildArch:      x86_64

License:        X11 License
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc g++       

%description
Test Task

%prep
%{__rm} -rf %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
%{__tar} -xzvf %{SOURCE0} -C %{_builddir}/%{name}-%{version} --strip-components 1


%build
cd %{name}-%{version}
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
cp %{name}-%{version}/%{name} $RPM_BUILD_ROOT/usr/local/bin

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
/usr/local/bin/%{name}

%changelog
* Wed Oct 19 2022 nikita
- 
