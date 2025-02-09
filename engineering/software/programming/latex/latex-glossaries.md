# Glossaries

- Although glossaries can be created in the main file itself, It is ideal to have all of it in a seperate file and include it while compiling. This is followed in this documentation.

- Create a tex file for glossaries.
  ```
  └── glossary.tex
  └── chapter.tex
  └── main.tex
  ```

* Add the glossaries as follows, Here angle is the label that is to be used in the documents and which will be replaced by thetha!

  ```tex
  % glossaries.tex
  \newglossaryentry{angle}{name={thetha},description={it represents the angle of inclination.}}
  % Add more glossary entries here if needed
  ```

* An example chapter.tex file:

  ```tex
  %chapter.tex
  \chapter{Background Theory and Literature Review}
  \label{chap:litrev}

  \section{Math Equations}

  The angle \gls{angle} gives us what we want.
  ```

* The main.tex file would be like:

  ```tex
  %main.tex
  \usepackage{glossaries} % For glossaries

  % Define the glossary
  \makeglossaries

  % Load glossary entries from the external file
  \loadglsentries{glossaries.tex}

  \begin{document}
  \include{chapter}

  % Glossaries
  \printglossary

  \end{document}
  ```

* After compiling, everything must work except that the list of glossaries aren't printed in a seperate page. For that we have to do the following:
  - Open the terminal(In a VS Code like environment) and run `makeglossaries main`.
  - Recompile everything.
