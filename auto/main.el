(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("ctexbook" "a4paper" "titlepage" "UTF8" "openany")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("hyperref" "colorlinks" "linkcolor=red")))
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "chapter1"
    "chapter2"
    "chapter3"
    "chapter4"
    "ctexbook"
    "ctexbook10"
    "xeCJK"
    "hyperref"
    "xcolor"
    "listings"
    "fontspec"
    "geometry")
   (LaTeX-add-xcolor-definecolors
    "mygreen"))
 :latex)

