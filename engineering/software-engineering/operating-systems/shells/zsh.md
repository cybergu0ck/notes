# ZSH

<br>
<br>

## My ZSH Customisations

- Open the zshrc file using the command.

  ```
  code ~/.zshrc
  ```

- Add the following lines.

  ```bashrc
  #following are my customisations--------------------------------

  autoload -Uz vcs_info
  precmd() { vcs_info}

  zstyle ':vcs_info:git:*' formats '(%b)'
  setopt PROMPT_SUBST
  # PROMPT='%F{green}%1~/ ${vcs_info_msg_0_} %\u2190 ->%f'
  PROMPT=$'%F{green}%1~/ ${vcs_info_msg_0_} → %f'

  # PROMPT="%1~  ${vcs_info_msg_0_}  -> "


  export NVM_DIR="$HOME/.nvm"
  [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
  [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

  #---------------------------------------------------------ends here
  ```

<br>
<br>
