---
Author: shen
Githu: https://github.com/Shentxt
Readme: any problem or package error contact me
---

## redirect the link so eww can find your directory (use you dir)
ln -s ~/.config/bspwm/bar ~/.config/eww

## Main Applications
### just copy and paste the following sequence (remember to change yay for your specific package). Extra information, as this is an arch distro, verify that in your distro there are said applications called the same way

<div style="background-color: black; color: white; padding: 10px;">
<pre><code>

yay -S bspwm sxhkd eww rofi picom-ftlabs-git ttf-jetbrains-mono-nerd ttf-roboto-mono-nerd nerd-fonts-git ttf-font-awesome ttf-dejavu zsh zsh-history-substring-search zsh-syntax-highlighting zsh-autosuggestions kitty wezterm jgmenu dunst betterlockscreen feh 

</code></pre>
</div>

# ━────────────━────────────━━────────────━━────────────━━────────────━━

## Extra Aplications
### If you do not install this, some scripts do not work, but they are not essential for the graphical environment or the aesthetics.

<div style="background-color: black; color: white; padding: 10px;">
<pre><code>

yay -S neofetch btop amdctl bsp-layout copyq stalonetray xrandr xclip xprop ffmpeg maim xautolock xsetroot plank qrcp jq yt-dlp 

</code></pre>
</div>

# ━────────────━────────────━━────────────━━────────────━━────────────━━

## Copy Files

<div style="background-color: black; color: white; padding: 10px;">
<pre><code>

## Firefox Conf 

use about:support and copy the files

## Copy Paste 

cp -r .zshrc ~/
cp -r .config ~/
cp -r .local/bin ~/.local/bin
cp -r .local/share ~/.local/share
cp -r boot/grub /boot/grub/themes
cp -r usr/share/applications /usr/share/applications
cp -r usr/share/fonts /usr/share/fonts
cp -r usr/share/icons /usr/share/icons

### Use the one you like the most, there are different configurations for the session manager
## Glorious

cp -r usr/share/glorious /usr/share/glorious 

## Sddm

cp -r usr/share/slice /usr/share/sddm/themes 

</code></pre>
</div>
