<div align="center">
     <h1>󰣇 Shen ~ NordicBreeze Dotfiles ⭐</h1>
 </div>
 
![Logotype](/assets/bsp.png "a logo")
** 🌿Sections**

- 🌸 [System and Directory]()
- 🌸 [Galery]()
- 🌸 [Keys-Maps]()
- 🌸 [Install and Desintall]()
- 🌸 [Informations]()

** 🌿Presentation**

Don't you think a system should be visually beautiful but just as fast? Simple yet elegant setup based on the BSPWM graphics system.
This setup aims for visual elegance and fluidity.

Read carefully: As not everything computers have the same features and kernel. I ask you to clarify any problem that I present in the download or post of this one. This is in order to have feedback and be able to improve.

** 🌿Presentation**

# 🌿System

|    Distro    |                        [Archcraft](https://github.com/archcraft-os)            |
| :----------: | :----------------------------------------------------------------------------: |
|      WM      |                 [BSPWM](https://github.com/baskerville/bspwm)                  |
|   Terminal   | [Wezterm](https://github.com/wez/wezterm)-[Alacritty](https://alacritty)       |
|   Widgets    |            [ElKowars wacky widgets](https://github.com/elkowar/eww)            |
|    Shell     |                [Starship](https://github.com/starship/starship)                |
|   Launcher   |                   [Rofi](https://github.com/davatorium/rofi)                   |
|  Clipboard   |              [Rofi-Greenclip](https://github.com/erebe/greenclip)              |
|    Editor    | [Neovim](https://github.com/neovim/neovim)-[Vs](https://code.visualstudio.com/)|
|  Compositor  |              [Picom](https://github.com/yshui/picom)                           |
| Music/Player | [Amberol](https://apps.gnome.org/es/Amberol/)-ytmusic                          |
| File Manager |              [Thunar](https://github.com/xfce-mirror/thunar)                   |
| Notification |              [Dunst](https://github.com/dunst-project/dunst)                   |
| Theme Brow   |              [Firefox-gx](https://github.com/Godiesc/firefox-gx)               |
| Lockscreen   | [Betterlocksreen](https://github.com/betterlockscreen/betterlockscreen)        |

** 🌿Directory**

NordicBreeze/ 
 └── .config/
      ├── bspwm
          ├── assets
              ├── effects
              ├── icons
              └── walls
          ├── bar
              ├── scripts
              ├── src 
              ├── config.ini 
              ├── gylphs.ini 
              └── modules.ini 
          ├── scripts 
              ├── autokill
              ├── brightnes
              ├── Brightness
              ├── BspHideNode
              ├── bsproot
              ├── colorpicker
              ├── colors.ini
              ├── ExternalRules
              ├── HideBar
              ├── KeybindingsHelp
              ├── MediaControl
              ├── Menu.txt
              ├── Notes
              ├── Opacity
              ├── OpenApps
              ├── Run_jgmenu
              ├── Screenshot
              ├── SetsVars
              ├── System.ini
              ├── Temp.sh 
              ├── Update
              ├── Volume
              ├── Wallselect
              ├── Weather
              ├── Welcome
              └── ytmp3
          ├── bspwmrc
          ├── dunstrc 
          ├── jgmenurc 
          ├── picom.conf 
          ├── stalonetrayrc 
          └── sxhkdrc
      ├── alacritty
          ├── alacritty.toml
          └── fonts.toml
      ├── cava
          └── config
      ├── corectrl
          └── corectrl
      ├── gtk-3.0
          ├── widgets
          ├── _apps.scss 
          ├── _colors.scss
          ├── _colors-public.scss
          ├── _common.scss
          ├── _drawing.scss
          ├── _elementary-colors.scss
          ├── gtk.css
          ├── gtk.scss 
          ├── gtk-dark.css
          ├── gtk-dark.scss
          ├── _nord.scss
          ├── thumbail.png
          └── _widgets.scss
      ├── gtk-4.0
          ├── apps
          ├── widgets 
          ├── _apps.scss 
          ├── _common.scss 
          ├── _drawing.scss
          ├── gtk.css
          ├── gtk.scss 
          ├── gtk-dark.scss
          ├── thumbail.png
          └── _widgets.scss 
      ├── kvantum
          ├── nordic-bluish
          └── kvantum.kvconfig 
      ├── neofetch
          ├── assets
          └── config.conf 
      ├── nvim 
          ├── lua
          ├── init.lua
          └── lazy-lock.json
      ├── quotes
          └── quotes.json
      ├── ranger
          ├── colorschemes
          ├── plugins
          ├── rc.conf
          └── rifle.conf 
      ├── rofi
          ├── images
          ├── themes
          └── config.rasi
      ├── starship
          └── starship.toml
      ├── wezterm
          └── wezterm.lua
      └── betterlockscreen
          ├── betterlockscreenrc
          └── corrupter

## 🌿Galery

<details>
<summary><b><code>Desktop</code></b></summary>

|Desk|Update|
|--|--|
|![demo](/assets/Screen/desk.png "demo")|![demo](/assets/Screen/update.png "demo")|

</details>

<details>
<summary><b><code>Firefox</code></b></summary>

|Home|Lateral-bar|
|--|--|
|![demo](/assets/Screen/firefox.png "demo")|![demo](/assets/Screen/firebing.png "demo")|

</details>

<details>
<summary><b><code>Rofi</code></b></summary>

|Desk|Update|
|--|--|--|
|![demo](/assets/Screen/launch.png "demo")|![demo](/assets/Screen/wall.png "demo")|![demo](/assets/Screen/power.png "demo")|

</details>

<details>
<summary><b><code>Extra</code></b></summary>

|Desk|Update|
|--|--|--|
|![demo](/assets/Screen/notify.png "demo")|![demo](/assets/Screen/tray.png "demo")|![demo](/assets/Screen/clip.png "demo")|

</details>

## 🌿Keys-Map

- **Win+Shift+D:** Open the key display. This key combination can be useful to access various functions in my settings.

## 💾Download

<div style="background-color: black; color: white; padding: 10px;">
<pre><code>
 Git/ 
 └── cd NordicBreeze/
      ├── cp -r config/* ~/.config/
      ├── cp -r firefox/* ~/.mozilla/firefox # More informations "about:support" only firefox
      ├── cp -r fonts/* /usr/share/fonts
      ├── cp -r icons/* /usr/share/icons
      ├── cp -r slice/* /usr/share/sddm/themes # Only sddm theme 
      ├── cp -r glorius/* /usr/share/lightdm-webkit/themes/ # "https://github.com/thecmdrunner/lightdm-glorious-webkit2" 
      └── cp -r .zshrc/* /home/user/
</code></pre>
</div>

** 💾Removed**

<div style="background-color: black; color: white; padding: 10px;">
<pre><code>
 delete only the git directory/ 
 └──  sudo rm -r NordicBreeze  

 delete everything and even the directories for the theme/
 └──  to delete everything do install but using "rm -r"  
</code></pre>
</div>

** 📦Packages**

<div style="background-color: black; color: white; padding: 10px;">
<pre><code>
# use paru or your package manager (Possibly it only works in arch, if you try it in another distro let me know)
Packages/
├── BSPWM/
│   ├── Sxhkdrc
    ├── Dunst
    ├── Polybar
    ├── Eww
    ├── Feh
    ├── Picom
    ├── Firefox
├── Terminal/
│   ├── Wezterm
    ├── Alacritty
├── Menu/
│   ├── Rofi
    ├── Jgmenu
├── AMD/
│   ├── AMDctl
    ├── Corectrl
    ├── Supergfxctl
├── Features/
    ├── Grimblast
    ├── Stalonetra
    ├── Xclip
    ├── Notify-send
    ├── Copyq
    ├── yt-dlp
    ├── Xblacklight
    └── themes/
        └── nordic-bluish-accent-theme/
</code></pre>
</div>

## 🌿Informations

- [Github](https://github.com/Shentxt)

** 🌿Inspirations**

- 🌸 [Unixporn](https://www.reddit.com/r/unixporn/)
- 🌸 [Cenunix](https://github.com/cenunix)
- 🌸 [AlphaTecnolog](https://github.com/AlphaTechnolog/dotfiles)
- 🌸 [Juminai](https://github.com/juminai/dotfiles)
- 🌸 [Gh0stzk](https://github.com/gh0stzk/dotfiles)
- 🌸 [Aylur](https://github.com/Aylur/dotfiles)
- 🌸 [Ryan](https://github.com/hidayry)

** 🌿Thanks**

- 🌸 [Bing-IA](https://www.bing.com/?setlang=es)
- 🌸 [Arch](https://archlinux.org/)
