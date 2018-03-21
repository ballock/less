Name:       less
Summary:    A text file browser similar to more, but better
Version:    436
Release:    7.33
Group:      Applications/Text
License:    GPLv3+
URL:        http://www.greenwoodsoftware.com/less/
Source0:    http://www.greenwoodsoftware.com/less/%{name}-%{version}.tar.gz
Source1:    lesspipe.sh
Source2:    less.sh
Source3:    less.csh
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
The less utility is a text file browser that resembles more, but has
more capabilities.  Less allows you to move backwards in the file as
well as forwards.  Since less doesn't have to read the entire input file
before it starts, less starts up more quickly than text editors (for
example, vi). 

You should install less because it is a basic utility for viewing text
files, and you'll use it frequently.

%prep
%setup -q -n %{name}-%{version}

%build

%configure --disable-static
# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

# splitted post-install part by auto-parsing
strip -R .comment $RPM_BUILD_ROOT/%{_bindir}/less
mkdir -p $RPM_BUILD_ROOT/etc/profile.d
install -p -c -m 755 %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}
install -p -c -m 644 %{SOURCE2} $RPM_BUILD_ROOT/etc/profile.d
install -p -c -m 644 %{SOURCE3} $RPM_BUILD_ROOT/etc/profile.d
ls -la $RPM_BUILD_ROOT/etc/profile.d

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
/etc/profile.d/*
%{_bindir}/*
%{_mandir}/man1/*
