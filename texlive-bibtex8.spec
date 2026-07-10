%global tl_name bibtex8
%global tl_revision 75712

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	BibTeX variant supporting 8-bit encodings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/bibtex-x
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex8.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex8.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(bibtex8.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An enhanced, portable C version of BibTeX. Enhanced by conversion to
larger (32-bit) capacity, addition of run-time selectable capacity and
8-bit support extensions. National character set and sorting order are
controlled by an external configuration file. Various examples are
included. Originally written by Niel Kempson and Alejandro Aguilar-
Sierra, it is now maintained as part of TeX Live.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex/csf
%dir %{_datadir}/texmf-dist/texmf-dist/doc/bibtex8
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex/csf/base
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex/csf/polish-csf
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man/man1
%{_datadir}/texmf-dist/texmf-dist/bibtex/csf/base/88591lat.csf
%{_datadir}/texmf-dist/texmf-dist/bibtex/csf/base/88591sca.csf
%{_datadir}/texmf-dist/texmf-dist/bibtex/csf/base/README.TEXLIVE
%{_datadir}/texmf-dist/texmf-dist/bibtex/csf/base/ascii.csf
%{_datadir}/texmf-dist/texmf-dist/bibtex/csf/base/cp437lat.csf
%{_datadir}/texmf-dist/texmf-dist/bibtex/csf/base/cp850lat.csf
%{_datadir}/texmf-dist/texmf-dist/bibtex/csf/base/cp850sca.csf
%{_datadir}/texmf-dist/texmf-dist/bibtex/csf/base/cp866rus.csf
%{_datadir}/texmf-dist/texmf-dist/bibtex/csf/base/csfile.txt
%{_datadir}/texmf-dist/texmf-dist/bibtex/csf/polish-csf/88592pl.csf
%{_datadir}/texmf-dist/texmf-dist/bibtex/csf/polish-csf/cp1250pl.csf
%{_datadir}/texmf-dist/texmf-dist/bibtex/csf/polish-csf/cp852pl.csf
%{_datadir}/texmf-dist/texmf-dist/bibtex/csf/polish-csf/iso8859-7.csf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex8/00bibtex8-history.txt
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex8/00bibtex8-readme.txt
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex8/csfile.txt
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex8/file_id.diz
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/bibtex8.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/bibtex8.man1.pdf
