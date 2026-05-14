# **$\textcolor{blue}{ArchArm7v-Rpi3B+ DHT11 }$**

> 🇵🇱 Polish version: [README_pl.md](README_pl.md)

## 1. Arch Linux Configuration:
### The Arch Linux ARM installation guide can be found at:

https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-3


> [!WARNING]
> - default login:
>   - user: **alarm** password **alarm**
>   - **root** password **root**
> - creating a new user:
>   - `useradd -m -g users -G wheel,storage,power -s /bin/bash -d /home/[userName] [userName]`
>   - `passwd [userName]`
> - setting timezone:
>   - `ln -sf /usr/share/zoneinfo/Europe/Warsaw /etc/localtime`
>
> After booting the Raspberry Pi, manually update the current date using _`timedatectl`_, and only then execute:
```bash
wifi-menu

pacman-key --init && pacman-key --populate archlinuxarm
```

Then edit the `pacman.conf` file:
```bash
sudo nano /etc/pacman.conf
```

> [!TIP]
> ![pacmanCONF](https://github.com/user-attachments/assets/c6ec226d-c0f7-4192-9173-cb4888888d40)

Install required dependencies:  
_(you may need to perform a full system upgrade first using `pacman -Syu`)_

```bash
sudo pacman -Sy
sudo pacman -S base base-devel linux linux-firmware git wget openssh networkmanager network-manager-applet iw
               wpa_supplicant dialog lshw unzip btop
```

### 2. **YAY**

The Arch User Repository (AUR) contains a huge number of software packages maintained by the community, therefore AUR helper tools were created to simplify this process.

**yay** is one of the most popular AUR helpers:

```bash
mkdir temp && cd temp
sudo git clone https://aur.archlinux.org/yay-bin.git
sudo chmod +x [USER:GROUP] yay-bin
cd yay-bin
makepkg -si
```

Then update the system using `yay -Syyuu` and synchronize the system clock using `sudo ntpdate pool.ntp.org`  
(_install missing package if required:_ `yay -S ntp`, `timedatectl set-ntp true`)

### 3. zsh + oh-my-zsh + p10k

- `yay -S zsh`

```bash
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```

- Powerlevel10k  
https://github.com/romkatv/powerlevel10k?tab=readme-ov-file#oh-my-zsh

Then log out or even reboot the Raspberry Pi.

> [!TIP]
> `tmux` replaces non-ASCII characters with `_` symbols if it was launched without the `-u` option and the locale was not configured for UTF-8 at startup.
> The best solution is to install and enable UTF-8 locales in the system.

`tmux`

![tmux](https://github.com/user-attachments/assets/096c1625-6ff6-4196-96ca-b689a1c5c0bf)

`tmux -u`

![tmux-u](https://github.com/user-attachments/assets/d2db76f1-274c-4726-ba59-1009536fe099)


## 2. Adafruit_DHT 11

I recommend installing the driver directly from the repository:

```bash
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
```

More details can be found at:

https://github.com/adafruit/Adafruit_Python_DHT


> [!TIP]
> If any packages are missing, you can search for them using `yay` with the `-Ss` parameter, for example:
> `yay -Ss setuptools`
>
> Then install the selected package.


Final result

![Adafruit](https://github.com/user-attachments/assets/b5d5172f-c0dc-45fc-994a-f1ebdf0488b8)