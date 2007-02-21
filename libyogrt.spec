Summary: Your One Get Remaining Time library.
Name: See META file
Version: See META file
Release: See META file
License: Proprietary
Group: System Environment/Base
#URL: 
Packager: Christopher J. Morrone <morrone2@llnl.gov>
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A simple wrapper library that provides a unified get-remaining-time
interface for multiple parallel job scheduling systems.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
DESTDIR="$RPM_BUILD_ROOT" make install

# Now determine file lists for each subpackage
for subpackage in none slurm lcrm moab; do
	touch ${subpackage}.files
	if [ -d $RPM_BUILD_ROOT%{_libdir}/libyogrt/${subpackage} ]; then
		cat > ${subpackage}.files << ENDOFLIST
%defattr(-,root,root,-)
%doc
%{_includedir}/yogrt.h
%{_libdir}/libyogrt/${subpackage}/*
ENDOFLIST
	fi
done

%clean
rm -rf $RPM_BUILD_ROOT

######################################################################
# none subpackage 
%package none
Summary: libyogrt none implementation
Group: System Environment/Base
Provides: libyogrt
Conflicts: libyogrt-slurm libyogrt-lcrm

%description none
A simple wrapper library that provides a unified get-remaining-time
interface for multiple parallel job scheduling systems.  This package
provides the "none" libyogurt wrapper.

%files -f none.files none

%post none
# Create the symlinks to the library
subpackage=none
lib_names=$(. %{_libdir}/libyogrt/${subpackage}/libyogrt.la; echo -n $library_names)
for name in $lib_names; do
	lib=%{_libdir}/libyogrt/${subpackage}/${name}
	if [ -L $lib ]; then
		ln -sf `readlink $lib` %{_libdir}/${name}
	elif [ -e $lib ]; then
		ln -sf $lib %{_libdir}/${name}
	fi
done

%preun none
# Remove the symlinks to the library
subpackage=none
lib_names=$(. %{_libdir}/libyogrt/${subpackage}/libyogrt.la; echo -n $library_names)
for name in $lib_names; do
	rm -f %{_libdir}/${name}
done

######################################################################
# slurm subpackage 
%package slurm
Summary: libyogrt SLURM implementation
Group: System Environment/Base
Provides: libyogrt
Conflicts: libyogrt-none libyogrt-lcrm

%description slurm
A simple wrapper library that provides a unified get-remaining-time
interface for multiple parallel job scheduling systems.  This package
provides the SLURM libyogurt wrapper.

%files -f slurm.files slurm

%post slurm
# Create the symlinks to the library
subpackage=slurm
lib_names=$(. %{_libdir}/libyogrt/${subpackage}/libyogrt.la; echo -n $library_names)
for name in $lib_names; do
	lib=%{_libdir}/libyogrt/${subpackage}/${name}
	if [ -L $lib ]; then
		ln -sf `readlink $lib` %{_libdir}/${name}
	elif [ -e $lib ]; then
		ln -sf $lib %{_libdir}/${name}
	fi
done

%preun slurm
# Remove the symlinks to the library
subpackage=slurm
lib_names=$(. %{_libdir}/libyogrt/${subpackage}/libyogrt.la; echo -n $library_names)
for name in $lib_names; do
	rm -f %{_libdir}/${name}
done

######################################################################
# lcrm subpackage 
%package lcrm
Summary: libyogrt LCRM implementation
Group: System Environment/Base
Provides: libyogrt
Conflicts: libyogrt-none libyogrt-slurm

%description lcrm
A simple wrapper library that provides a unified get-remaining-time
interface for multiple parallel job scheduling systems.  This package
provides the LCRM libyogurt wrapper.

%files -f lcrm.files lcrm

%post lcrm
# Create the symlinks to the library
subpackage=lcrm
lib_names=$(. %{_libdir}/libyogrt/${subpackage}/libyogrt.la; echo -n $library_names)
for name in $lib_names; do
	lib=%{_libdir}/libyogrt/${subpackage}/${name}
	if [ -L $lib ]; then
		ln -sf `readlink $lib` %{_libdir}/${name}
	elif [ -e $lib ]; then
		ln -sf $lib %{_libdir}/${name}
	fi
done

%preun lcrm
# Remove the symlinks to the library
subpackage=lcrm
lib_names=$(. %{_libdir}/libyogrt/${subpackage}/libyogrt.la; echo -n $library_names)
for name in $lib_names; do
	rm -f %{_libdir}/${name}
done

%changelog
* Mon Feb 12 2007 Christopher J. Morrone <morrone@conon.llnl.gov> - 
- Initial build.

