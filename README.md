<div align="center">
     <h1> 🌸 Shen ~ NordicBreeze Dotfiles 🌸</h1>
 </div>
 
![Logotype](/assets/bsp.png "a logo")

# 🌿Sections

- 🌸 [Presentations](https://github.com/Shentxt/NordicBreeze/tree/main#system)
- 🌸 [Galery](https://github.com/Shentxt/NordicBreeze/tree/main#galery)
- 🌸 [Intructions](https://github.com/Shentxt/NordicBreeze/tree/main#download)
- 🌸 [Informations](https://github.com/Shentxt/NordicBreeze/tree/main#contact-me)

## 🌿Presentation

Don't you think a system should be visually beautiful but just as fast? Simple yet elegant setup based on the BSPWM graphics system.
This setup aims for visual elegance and fluidity.

Read carefully: As not everything computers have the same features and kernel. I ask you to clarify any problem that I present in the download or post of this one. This is in order to have feedback and be able to improve.

## 🌿Keys-Map

|     Info     |    Keys      |
| :----------: | :----------: |
|  Keys-Map    |  Win+Ctrl+D  |

## 🌿System

|    Distro    |                [EndevourOS](https://endeavouros.com/)                          |
| :----------: | :----------------------------------------------------------------------------: |
|     WM       |                 [BSPWM](https://github.com/baskerville/bspwm)                  |
|   Terminal   | [Wezterm](https://github.com/wez/wezterm)-[Alacritty](https://alacritty)       |
|   Widgets    |            [ElKowars wacky widgets](https://github.com/elkowar/eww)            |
|     Bar      |            [Polybar](https://github.com/polybar/polybar)                       |
|    Shell     |                [Starship](https://github.com/starship/starship)                |
|   Launcher   |                   [Rofi](https://github.com/davatorium/rofi)                   |
|  Clipboard   |              [Copyq](https://github.com/hluk/CopyQ)                            |
|    Editor    | [Neovim](https://github.com/neovim/neovim)-[Vs](https://code.visualstudio.com/)|
|  Compositor  |              [Picom](https://github.com/FT-Labs/picom)                         |
| Music/Player |             [Amberol](https://apps.gnome.org/es/Amberol/)                      |
| File Manager |              [Thunar](https://github.com/xfce-mirror/thunar)                   |
| Notification |              [Dunst](https://github.com/dunst-project/dunst)                   |
| Theme Brow   |              [Firefox-gx](https://github.com/Godiesc/firefox-gx)               |
| Lockscreen   | [Betterlocksreen](https://github.com/betterlockscreen/betterlockscreen)        |
| Sesion UI    |   [Glorius](https://github.com/thecmdrunner/lightdm-glorious-webkit2)          |
|   Grub       |          [Minecraft](https://github.com/Lxtharia/minegrub-theme)               |
| statepage    |          [Tartarus](https://alljavi.github.io/tartarus-startpage/)             |
      

# 🌿Galery

<details>
<summary><b><code>Desktop</code></b></summary>

|Desk|Update|packer|
|--|--|--|
|![demo](/assets/Screen/desk.png "demo")|![demo](/assets/Screen/update.png "demo")|![demo](/assets/Screen/pack.png "demo")|

</details>

<details>
<summary><b><code>Firefox</code></b></summary>

|Home|Lateral-bar|
|--|--|
|![demo](/assets/Screen/firefox.png "demo")|![demo](/assets/Screen/firebing.png "demo")|
</details>

<details>
<summary><b><code>Rofi</code></b></summary>

|Launcher|Wall|Power|window|
|--|--|--|--|
|![demo](/assets/Screen/launch.png "demo")|![demo](/assets/Screen/wall.png "demo")|![demo](/assets/Screen/power.png "demo")|![demo](/assets/Screen/window.png "demo")|

</details>

<details>
<summary><b><code>Popup</code></b></summary>

|Notify|Tray|Clipboard|dl-Music|Music|
|--|--|--|--|--|
|![demo](/assets/Screen/notify.png "demo")|![demo](/assets/Screen/tray.png "demo")|![demo](/assets/Screen/clip.png "demo")|![demo](/assets/Screen/downloadmusic.png "demo")|![demo](/assets/Screen/info.png "demo")|

</details>

<details>
<summary><b><code>Extra</code></b></summary>

|iconpack|minegrub|
|--|--|
|![demo](/assets/Screen/icon.png "demo")|![demo](/assets/Screen/mine.webp "demo")|

</details>

# 💾Download

soon I will have an automatic installer/ 
 └── cd NordicBreeze/
      ├── cp -r config/* ~/.config/
      ├── cp -r firefox/* ~/.mozilla/firefox # More informations "about:support" only firefox
      ├── cp -r fonts/* /usr/share/fonts
      ├── cp -r icons/* /usr/share/icons
      ├── cp -r slice/* /usr/share/sddm/themes # Only sddm theme 
      ├── cp -r glorius/* /usr/share/lightdm-webkit/themes/ # Only Lighdm 
      ├── cp -r minegrub/* /boot/grub/themes/
      ├── cp -r eww/* ~/.local/bin/
      └── cp -r .zshrc/* ~/

## 💾Removed

<div style="background-color: black; color: white; padding: 10px;">
<pre><code>
 delete only the git directory/ 
 └──  sudo rm -r NordicBreeze  

 delete everything and even the directories for the theme/
 └──  to delete everything do install but using "rm -r"  
</code></pre>
</div>

## 📦Packages

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
    ├── Physlock
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
    ├── betterlocksreen 
    ├── lightdm (Glorious)
    ├── Archcraft
    └── themes/
        └── nordic-bluish-accent-theme/
</code></pre>
</div>

# 🌿Contact Me

- [Github](https://github.com/Shentxt)
- [Linkelind](https://www.linkedin.com/in/federico-p-065a42217/)

## 🌿Thanks

- 🌸 [Bing-IA](https://www.bing.com/?setlang=es)
- 🌸 [Arch](https://archlinux.org/)
- 🌸 [Unixporn](https://www.reddit.com/r/unixporn/)
- 🌸 [Persona](https://www.tumblr.com/jakku-san/620012944745512960/noosey-woosey-noosey-woosey-noosey-woosey)
- 🌸 [Icon](https://iconos8.es/icons)

## 🌿Based in 

- 🌸 [AlphaTecnolog](https://github.com/AlphaTechnolog/dotfiles)
- 🌸 [Juminai](https://github.com/juminai/dotfiles)
- 🌸 [Gh0stzk](https://github.com/gh0stzk/dotfiles)
- 🌸 [Ryan](https://github.com/hidayry/dotfiles-bspwm)
