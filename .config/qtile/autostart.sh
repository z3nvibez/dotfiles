#! /bin/bash 
picom &
nitrogen --restore &
urxvtd -q -o -f &
sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc
