# Equations

- An example code showing the syntax to write equations.

  ```tex
  \usepackage{amsmath} % For equations

  \begin{document}

  \begin{equation}
  \text{slope} = \tan(\theta)
  \end{equation}

  \end{document}
  ```

<br>
<br>
<br>

# Equations with glossaries

- The crude way I do is

  ```tex
  % glossaries.tex
  \newglossaryentry{angle}{name={thetha},description={it represents the angle of inclination.}}
  % Add more glossary entries here if needed
  ```

  ```tex
  % in main.tex or chapter.tex
  \begin{equation}
    \text{slope} = \tan(\thetha)
  \end{equation}

  where:
  \begin{itemize}
      \item \gls{angle} is the angle of inclination.
  \end{itemize}
  ```
