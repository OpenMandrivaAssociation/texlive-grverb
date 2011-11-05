# revision 17368
# category Package
# catalog-ctan /language/greek/grverb
# catalog-date 2010-03-06 16:54:30 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-grverb
Version:	1.0
Release:	1
Summary:	Typesetting Greek verbatim
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/greek/grverb
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grverb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grverb.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grverb.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides verbatim typsetting, in the context of the
Greek option in babel. The package uses the public domain
Greek-CourierPlain font, and the font itself (in Type 1
format), metrics and a font map entry for its use are provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/grverb/grkcurp.afm
%{_texmfdistdir}/fonts/map/dvips/grverb/grverb.map
%{_texmfdistdir}/fonts/tfm/public/grverb/grcour7t.tfm
%{_texmfdistdir}/fonts/tfm/public/grverb/grcour8a.tfm
%{_texmfdistdir}/fonts/type1/public/grverb/grkcurp.pfb
%{_texmfdistdir}/fonts/vf/public/grverb/grcour7t.vf
%{_texmfdistdir}/tex/latex/grverb/grverb.sty
%doc %{_texmfdistdir}/doc/latex/grverb/README
%doc %{_texmfdistdir}/doc/latex/grverb/grv.ps
%doc %{_texmfdistdir}/doc/latex/grverb/grv.tex
%doc %{_texmfdistdir}/doc/latex/grverb/grverb.pdf
#- source
%doc %{_texmfdistdir}/source/latex/grverb/grcour7t.vpl
%doc %{_texmfdistdir}/source/latex/grverb/grverb.dtx
%doc %{_texmfdistdir}/source/latex/grverb/grverb.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
