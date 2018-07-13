%define debug_package %{nil}

Name:           ocaml-rrd-transport
Version:        1.8.0
Release:        4%{?dist}
Summary:        Shared-memory protocols for transmitting RRD data
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/rrd-transport/
Source0:        https://code.citrite.net/rest/archive/latest/projects/XSU/repos/rrd-transport/archive?at=v%{version}&format=tar.gz&prefix=rrd-transport-%{version}#/rrd-transport-%{version}.tar.gz
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/rrd-transport/archive?at=v1.8.0&format=tar.gz&prefix=rrd-transport-1.8.0#/rrd-transport-1.8.0.tar.gz) = df2da8ed1c9572e597c160503931ab8349424f0b
BuildRequires:  xs-opam-repo
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  xen-dom0-libs-devel
Requires:       ocaml

%global _use_internal_dependency_generator 0
%global __requires_exclude *caml*

%description
Shared-memory protocol for transmitting RRD data, supporting in-memory files
and shared Xen pages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       xs-opam-repo
Requires:       xen-dom0-libs-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%global ocaml_dir    /usr/lib/opamroot/system
%global ocaml_libdir %{ocaml_dir}/lib
%global ocaml_docdir %{ocaml_dir}/doc
%global build_ocaml_dir %{buildroot}%{ocaml_dir}
%global build_ocaml_libdir %{buildroot}%{ocaml_libdir}
%global build_ocaml_docdir %{buildroot}%{ocaml_docdir}

%prep
%autosetup -p1 -n rrd-transport-%{version}

%build
eval $(opam config env --root=/usr/lib/opamroot)
make

%install
eval $(opam config env --root=/usr/lib/opamroot)
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{build_ocaml_libdir}
mkdir -p %{build_ocaml_docdir}

make install OPAM_PREFIX=%{build_ocaml_dir} OPAM_LIBDIR=%{build_ocaml_libdir} BINDIR=%{buildroot}%{_bindir}

%files
%doc LICENSE
%doc README.md
%{ocaml_libdir}/rrd-transport/META
%{ocaml_libdir}/rrd-transport/rrd_transport.cma
%{ocaml_libdir}/rrd-transport/*.cmi

%files devel
%exclude %{ocaml_libdir}/rrd-transport/opam
%exclude %{ocaml_libdir}/rrd-transport/*.cmt
%exclude %{ocaml_libdir}/rrd-transport/*.cmti
%exclude %{ocaml_libdir}/rrd-transport/*.dune
%{ocaml_dir}/doc/*
%{ocaml_libdir}/rrd-transport/*.a
%{ocaml_libdir}/rrd-transport/*.cmxa
%{ocaml_libdir}/rrd-transport/*.cmxs
%{ocaml_libdir}/rrd-transport/*.cmx
%{ocaml_libdir}/rrd-transport/*.ml
%exclude %{ocaml_libdir}/rrd-transport/*.mli

%{_bindir}/rrdreader
%{_bindir}/rrdwriter

%changelog
* Wed Apr 04 2018 Marcello Seri <marcello.seri@citrix.com> - 1.8.0-4
- Update SPEC file to get rid of rpmbuild warnings

* Thu Mar 22 2018 Marcello Seri <marcello.seri@citrix.com> - 1.8.0-1
- rrd-transport: update to use new xen-gnt-unix
- lib/rrd_protocol_v2: make safe-string safe

* Wed Mar 21 2018 Christian Lindig <christian.lindig@citrix.com> - 1.7.0-3
- Trigger rebuild

* Thu Feb 22 2018 Christian Lindig <christian.lindig@citrix.com> - 1.7.0-1
- Remove redundant definition of (|>) pipe

* Tue Feb 13 2018 Christian Lindig <christian.lindig@citrix.com> - 1.6.0-1
- Update maintainers and authors in opam file
- Update all opam files, enclose authors in strings

* Fri Feb 09 2018 Christian Lindig <christian.lindig@citrix.com> - 1.5.0-1
- Use String.lowercase_ascii as String.lowercase is deprecated
- Coverage: fix use of bash arrays
- Remove constraint on cstruct version
- Replace maintainers list with link to mailing list

* Mon Dec 18 2017 Marcello Seri <marcello.seri@citrix.com> - 1.4.0-1
- CA-276795: Trim null terminators that can be incorrectly part of the rrd metadata

* Fri Dec 15 2017 Marcello Seri <marcello.seri@citrix.com> - 1.3.0-1
- Port to jbuilder

* Thu May 11 2017 Marcello Seri <marcello.seri@citrix.com> - 1.2.0-1
- CA-253704: Force a memory re-mapping of mapped files with 0 length

* Mon Mar 13 2017 Marcello Seri <marcello.seri@citrix.com> - 1.1.1-2
- Update OCaml dependencies and build/install script after xs-opam-repo split

* Tue Aug 09 2016 Christian Lindig <christian.lindig@citrix.com> - 1.1.1-1
- install rrdreader, rrdwriter, update to 1.1.1

* Mon Aug 08 2016 Christian Lindig <christian.lindig@citrix.com> - 1.1.0-1
- Update to 1.1.0 after change of JSON format in f276692

* Mon Apr 25 2016 Euan Harris <euan.harris@citrix.com> - 1.0.0-1
- Update to 1.0.0

* Sat Apr 26 2014 David Scott <dave.scott@citrix.com> - 0.7.1-1
- Update to 0.7.1

* Mon Dec 16 2013 John Else <john.else@citrix.com> - 0.5.0-1
- Initial package
