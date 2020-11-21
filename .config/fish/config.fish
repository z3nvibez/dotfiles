set fish_greeting ""
set TERM "xterm-256color"
set EDITOR "/usr/bin/nvim"

# name: sashimi
function fish_prompt
  set -l last_status $status
  set -l cyan (set_color -o cyan)
  set -l yellow (set_color -o yellow)
  set -g red (set_color -o red)
  set -g blue (set_color -o blue)
  set -l green (set_color -o green)
  set -g normal (set_color normal)

  set -l ahead (_git_ahead)
  set -g whitespace ' '

  if test $last_status = 0
    set initial_indicator "$green◆"
    set status_indicator "$normal❯$cyan❯$green❯"
  else
    set initial_indicator "$red✖ $last_status"
    set status_indicator "$red❯$red❯$red❯"
  end
  set -l cwd $cyan(basename (prompt_pwd))

  if [ (_git_branch_name) ]

    if test (_git_branch_name) = 'master'
      set -l git_branch (_git_branch_name)
      set git_info "$normal git:($red$git_branch$normal)"
    else
      set -l git_branch (_git_branch_name)
      set git_info "$normal git:($blue$git_branch$normal)"
    end

    if [ (_is_git_dirty) ]
      set -l dirty "$yellow ✗"
      set git_info "$git_info$dirty"
    end
  end

  # Notify if a command took more than 5 minutes
  if [ "$CMD_DURATION" -gt 300000 ]
    echo The last command took (math "$CMD_DURATION/1000") seconds.
  end

  echo -n -s $initial_indicator $whitespace $cwd $git_info $whitespace $ahead $status_indicator $whitespace
end

function _git_ahead
  set -l commits (command git rev-list --left-right '@{upstream}...HEAD' ^/dev/null)
  if [ $status != 0 ]
    return
  end
  set -l behind (count (for arg in $commits; echo $arg; end | grep '^<'))
  set -l ahead  (count (for arg in $commits; echo $arg; end | grep -v '^<'))
  switch "$ahead $behind"
    case ''     # no upstream
    case '0 0'  # equal to upstream
      return
    case '* 0'  # ahead of upstream
      echo "$blue↑$normal_c$ahead$whitespace"
    case '0 *'  # behind upstream
      echo "$red↓$normal_c$behind$whitespace"
    case '*'    # diverged from upstream
      echo "$blue↑$normal$ahead $red↓$normal_c$behind$whitespace"
  end
end

function _git_branch_name
  echo (command git symbolic-ref HEAD ^/dev/null | sed -e 's|^refs/heads/||')
end

function _is_git_dirty
  echo (command git status -s --ignore-submodules=dirty ^/dev/null)
end


#aliases
alias mytime="tty-clock -ct"
alias update="sudo pacman -Syyu && yay -Syyu --noconfirm"
#alias cleanup="sudo pacman -Rns $(pacman -Qtdq)"
alias vimrc="nvim .config/nvim/init.vim"
alias v="nvim"
alias utar="tar -zxvf"
alias ls="exa -al --color=always --group-directories-first"
alias la="exa -a --color=always --group-directories-first"
alias cp="cp -i"
alias ff="fanficfare -p"
alias i3con="nvim .config/i3/config"
alias zsh="nvim .zshrc"
alias backup="rsync -auv --delete /home /run/media/drmdub/Big\ Boy/Backups/2020/middle3"
alias skel="cp -rf /etc/skel/* ~"
#alias bupskel="cp -Rf /etc/skel ~/.skel-backup-$(date +%Y.%m.%d-%H.%M.%S)"
#alias buconfig="cp -Rf ~/.config ~/.configbackup-$(date +%Y.%m.%d-%H.%M.%S)"
alias ducks='du -cks * | sort -rn | head'
alias samba="sudo smbd start"
alias c="clear"
alias sprint="termdown 20m && echo SPRINT DONE && paplay /usr/share/sounds/freedesktop/stereo/complete.oga"
alias sprint30="termdown 30m && echo SPRINT DONE && paplay /usr/share/sounds/freedesktop/stereo/complete.oga"
alias poly="nvim .config/polybar/config"
alias wpm="wpm --stats-file stats"





