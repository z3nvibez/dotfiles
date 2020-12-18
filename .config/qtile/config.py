# -*- coding: utf-8 -*-
#  ____ _____
# |  _ \_   _|  Derek Taylor (DistroTube)
# | | | || |    http://www.youtube.com/c/DistroTube
# | |_| || |    http://www.gitlab.com/dwt1/
# |____/ |_|
#
# A customized config.py for Qtile window manager (http://www.qtile.org)
# Modified by Derek Taylor (http://www.gitlab.com/dwt1/ )
#
# The following comments are the copyright and licensing information from the default
# qtile config. Copyright (c) 2010 Aldo Cortesi, 2010, 2014 dequis, 2012 Randall Ma,
# 2012-2014 Tycho Andersen, 2012 Craig Barnes, 2013 horsik, 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.

##### IMPORTS #####
import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401

##### DEFINING SOME VARIABLES #####
mod = "mod4"  # Sets mod key to SUPER/WINDOWS
myTerm = "termite"  # My terminal of choice
myConfig = "/home/drmdub/.config/qtile/config.py"  # The Qtile config file location

##### KEYBINDINGS #####
keys = [
    ### The essentials
    Key(
        [mod], "Return", lazy.spawn(myTerm), desc="Launches My Terminal With Fish Shell"
    ),
    #     Key(
    #       [mod, "shift"], "Return",
    #      lazy.spawn("dmenu_run -p 'Run: '"),
    #     desc='Dmenu Run Launcher'
    #    ),
    #    Key([mod], "d", lazy.spawn("rofi -show run"), desc="Dmenu Run Launcher"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle through layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill active window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "x", lazy.shutdown(), desc="Shutdown Qtile"),
    ### Switch focus to specific monitor (out of three)
    Key([mod], "w", lazy.to_screen(0), desc="Keyboard focus to monitor 1"),
    Key([mod], "e", lazy.to_screen(1), desc="Keyboard focus to monitor 2"),
    #       Key([mod], "r",
    #          lazy.to_screen(2),
    #         desc='Keyboard focus to monitor 3'
    #        ),
    ### Switch focus of monitors
    Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
    Key([mod], "comma", lazy.prev_screen(), desc="Move focus to prev monitor"),
    ### Treetab controls
    Key(
        [mod, "control"],
        "k",
        lazy.layout.section_up(),
        desc="Move up a section in treetab",
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.section_down(),
        desc="Move down a section in treetab",
    ),
    ### Window controls
    Key([mod], "k", lazy.layout.down(), desc="Move focus down in current stack pane"),
    Key([mod], "j", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [mod],
        "h",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="Expand window (MonadTall), increase number in master pane (Tile)",
    ),
    Key(
        [mod],
        "l",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Shrink window (MonadTall), decrease number in master pane (Tile)",
    ),
    Key([mod], "n", lazy.layout.normalize(), desc="normalize window size ratios"),
    Key(
        [mod],
        "m",
        lazy.layout.maximize(),
        desc="toggle window between minimum and maximum sizes",
    ),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="toggle floating"),
    ### Stack controls
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Switch which side main pane occupies (XmonadTall)",
    ),
    Key(
        [mod],
        "space",
        lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack",
    ),
    Key(
        [mod, "control"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    ### Dmenu scripts launched with ALT + CTRL + KEY
    Key(
        ["mod1", "control"],
        "e",
        lazy.spawn("./.dmenu/dmenu-edit-configs.sh"),
        desc="Dmenu script for editing config files",
    ),
    Key(
        ["mod1", "control"],
        "m",
        lazy.spawn("./.dmenu/dmenu-sysmon.sh"),
        desc="Dmenu system monitor script",
    ),
    Key(["mod1", "control"], "p", lazy.spawn("passmenu"), desc="Passmenu"),
    Key(
        ["mod1", "control"],
        "r",
        lazy.spawn("./.dmenu/dmenu-reddio.sh"),
        desc="Dmenu reddio script",
    ),
    Key(
        ["mod1", "control"],
        "s",
        lazy.spawn("./.dmenu/dmenu-surfraw.sh"),
        desc="Dmenu surfraw script",
    ),
    Key(
        ["mod1", "control"],
        "t",
        lazy.spawn("./.dmenu/dmenu-trading.sh"),
        desc="Dmenu trading programs script",
    ),
    Key(
        ["mod1", "control"],
        "i",
        lazy.spawn("./.dmenu/dmenu-scrot.sh"),
        desc="Dmenu scrot script",
    ),
    ### My applications launched with SUPER + ALT + KEY
    Key(["mod1"], "a", lazy.spawn("amixer -D pulse sset Master '3%-'")),
    Key(["mod1"], "d", lazy.spawn("amixer -D pulse sset Master '3%+'")),
    Key(
        [mod, "mod1"],
        "b",
        lazy.spawn("tabbed -r 2 surf -pe x '.surf/html/homepage.html'"),
        desc="lynx browser",
    ),
    Key(
        [mod, "mod1"],
        "l",
        lazy.spawn(myTerm + " -e lynx gopher://distro.tube"),
        desc="lynx browser",
    ),
    Key([mod, "mod1"], "n", lazy.spawn(myTerm + " -e newsboat"), desc="newsboat"),
    Key(
        [mod, "mod1"],
        "r",
        lazy.spawn(myTerm + " -e rtv"),
        desc="reddit terminal viewer",
    ),
    Key([mod, "mod1"], "e", lazy.spawn(myTerm + " -e neomutt"), desc="neomutt"),
    Key(
        [mod, "mod1"],
        "m",
        lazy.spawn(myTerm + " -e sh ./scripts/toot.sh"),
        desc="toot mastodon cli",
    ),
    Key(
        [mod, "mod1"],
        "t",
        lazy.spawn(myTerm + " -e sh ./scripts/tig-script.sh"),
        desc="tig",
    ),
    Key(
        [mod, "mod1"],
        "f",
        lazy.spawn(myTerm + " -e sh ./.config/vifm/scripts/vifmrun"),
        desc="vifm",
    ),
    Key([mod, "mod1"], "j", lazy.spawn(myTerm + " -e joplin"), desc="joplin"),
    Key([mod, "mod1"], "c", lazy.spawn(myTerm + " -e cmus"), desc="cmus"),
    Key([mod, "mod1"], "i", lazy.spawn(myTerm + " -e irssi"), desc="irssi"),
    Key(
        [mod, "mod1"],
        "y",
        lazy.spawn(myTerm + " -e youtube-viewer"),
        desc="youtube-viewer",
    ),
    Key([mod, "mod1"], "a", lazy.spawn(myTerm + " -e ncpamixer"), desc="ncpamixer"),
]

##### GROUPS #####
group_names = [
    ("WWW", {"layout": "monadtall"}),
    ("DEV", {"layout": "monadtall"}),
    ("WORD", {"layout": "monadtall"}),
    ("MAIL", {"layout": "monadtall"}),
    ("CHAT", {"layout": "monadtall"}),
    ("MUS", {"layout": "monadtall"}),
    ("VID", {"layout": "monadtall"}),
    ("FILES", {"layout": "monadtall"}),
    ("GFX", {"layout": "floating"}),
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(
        Key([mod], str(i), lazy.group[name].toscreen())
    )  # Switch to another group
    keys.append(
        Key([mod, "shift"], str(i), lazy.window.togroup(name))
    )  # Send current window to another group

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {
    "border_width": 2,
    "margin": 6,
    "border_focus": "e1acff",
    "border_normal": "1D2330",
}

##### THE LAYOUTS #####
layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    layout.TreeTab(
        font="Ubuntu",
        fontsize=10,
        sections=["FIRST", "SECOND"],
        section_fontsize=11,
        bg_color="141414",
        active_bg="90C435",
        active_fg="000000",
        inactive_bg="384323",
        inactive_fg="a0a0a0",
        padding_y=5,
        section_top=10,
        panel_width=320,
    ),
    layout.Floating(**layout_theme),
]

##### COLORS #####
colors = [
    ["#282a36", "#282a36"],  # panel background
    ["#434758", "#434758"],  # background for current screen tab
    ["#ffffff", "#ffffff"],  # font color for group names
    ["#ff5555", "#ff5555"],  # border line color for current tab
    ["#8d62a9", "#8d62a9"],  # border line color for other tab and odd widgets
    ["#668bd7", "#668bd7"],  # color for the even widgets
    ["#e1acff", "#e1acff"],
]  # window name

##### PROMPT #####
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono Nerd Font", fontsize=12, padding=2, background=colors[2]
)
extension_defaults = widget_defaults.copy()

##### WIDGETS #####


def init_widgets_list():
    widgets_list = [
        widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize=9,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=5,
            borderwidth=3,
            active=colors[2],
            inactive=colors[2],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[3],
            this_screen_border=colors[4],
            other_current_screen_border=colors[0],
            other_screen_border=colors[0],
            foreground=colors[2],
            background=colors[0],
        ),
        widget.Prompt(
            prompt=prompt,
            font="Ubuntu Mono",
            padding=10,
            foreground=colors[3],
            background=colors[1],
        ),
        widget.Sep(linewidth=0, padding=40, foreground=colors[2], background=colors[0]),
        widget.WindowName(foreground=colors[6], background=colors[0], padding=0),
        widget.TextBox(
            text=" 🌡",
            padding=2,
            foreground=colors[5],
            background=colors[0],
            fontsize=11,
        ),
        widget.ThermalSensor(foreground=colors[5], background=colors[0], padding=5),
        widget.TextBox(
            text=" ⟳",
            padding=2,
            foreground=colors[6],
            background=colors[0],
            fontsize=14,
        ),
        widget.TextBox(
            text="Updates", padding=5, foreground=colors[6], background=colors[0]
        ),
        widget.TextBox(
            text=" 🖬",
            foreground=colors[5],
            background=colors[0],
            padding=0,
            fontsize=14,
        ),
        widget.Memory(foreground=colors[5], background=colors[0], padding=5),
        widget.TextBox(
            text=" Vol:", foreground=colors[6], background=colors[0], padding=0
        ),
        widget.Volume(foreground=colors[6], background=colors[0], padding=5),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[5],
            background=colors[0],
            padding=0,
            scale=0.7,
        ),
        widget.CurrentLayout(foreground=colors[5], background=colors[0], padding=5),
        widget.Clock(
            foreground=colors[6], background=colors[0], format="%A, %B %d  [ %I:%M%p ]"
        ),
        widget.Sep(linewidth=0, padding=10, foreground=colors[0], background=colors[0]),
        widget.Systray(background=colors[0], padding=5),
    ]
    return widgets_list


##### SCREENS ##### (TRIPLE MONITOR SETUP)


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1  # Slicing removes unwanted widgets on Monitors 1,3


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2  # Monitor 2 will display all widgets in widgets_list


def init_screens():
    return [
        Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.95, size=20)),
        Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=0.95, size=20)),
        Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.95, size=20)),
    ]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

##### DRAG FLOATING WINDOWS #####
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True

##### FLOATING WINDOWS #####
floating_layout = layout.Floating(
    float_rules=[
        {"wmclass": "confirm"},
        {"wmclass": "dialog"},
        {"wmclass": "download"},
        {"wmclass": "error"},
        {"wmclass": "file_progress"},
        {"wmclass": "notification"},
        {"wmclass": "splash"},
        {"wmclass": "toolbar"},
        {"wmclass": "confirmreset"},  # gitk
        {"wmclass": "makebranch"},  # gitk
        {"wmclass": "maketag"},  # gitk
        {"wname": "branchdialog"},  # gitk
        {"wname": "pinentry"},  # GPG key password entry
        {"wmclass": "ssh-askpass"},  # ssh-askpass
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"

##### STARTUP APPLICATIONS #####
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
