# **$\textcolor{blue}{ArchArm7v-Rpi3B+}$**

## 1. Konfiguracja arch`a: 
### Sposób instalacji Arch'a ARM można znaleźć pod adresem:


https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-3


> [!WARNING]
> - domyślne logowanie:
>   - użytownik: **alarm** hasło **alarm**
>   - **root** hasło **root**
> - utowrzenie nowego użytkownika:
>   - `useradd -m -g users -G wheel,storage,power -s /bin/bash -d /home/[userName] [userName]`
>   - `passwd [userName]`
> - przypisanie strefy czasowej
>   - `ln -sf /usr/share/zoneinfo/Europe/Warsaw /etc/localtime`
>
> Po uruchomieniu maliny należy zmienić ręcznie datę na aktualną przy pomocy _`timedatectl`_, a nastepnie dopiero wykonać:
```
wifi-menu

pacman-key --init && pacman-key --populate archlinuxarm
```

następnie edytować plik `pacman.conf`
```
sudo nano /etc/pacman.conf
```

> [!TIP]
> ![pacmanCONF](https://github.com/user-attachments/assets/c6ec226d-c0f7-4192-9173-cb4888888d40)

doinstalowanie niezbędnych zależności:
_(możliwe, że trzeba będzie wykonać pełną aktualizację `pacman -Syu`)_

```
sudo pacman -Sy
sudo pacman -S base base-devel linux linux-firmware git wget openssh dhcpd networkmanager network-manager-applet iw
               wpa_supplicant dialog git lshw unzip btop
```

### 2. **YAY**

W Arch User Repository (AUR) znajdziesz ogromną liczbę pakietów oprogramowania, przygotowanych przez członków społeczności, dlatego stworzono narzędzia pomocnicze AUR, które ułatwiaja ten proces.

**yay** jest jednym z najpopularniejszych pomocników AUR:

```
mkdir temp && cd temp
sudo git clone https://aur.archlinux.org/yay-bin.git
sudo chmod +x [USER:GROUP] yay-bin
cd yay-bin
makepkg -si
```
a następnie zaktualizować system `yay -Syyuu` i zsynchronizować zegar systemowy `sudo ntpdate pool.ntp.org` (_nstalacja brakującego pakietu_ `yay -S  ntp`, `timedatectl set-ntp true`)

### 3. zsh + oh-my-zsh + p10k

- `yay -S zsh`

       
```
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```
  - Powerlevel10k
https://github.com/romkatv/powerlevel10k?tab=readme-ov-file#oh-my-zsh

nastepnie się przelogować, lub nawet zrestartować maline.


> [!TIP]
> `tmux` zastępuje znaki nie-ASCII symbolem _, jeśli został uruchomiony bez opcji `-u`, a ustawienia lokalne w momencie jego uruchomienia nie były ustawione na UTF-8.
> Najlepszym sposobem na rozwiązanie tego problemu jest zainstalowanie i włączenie lokalizacji UTF-8 w systemie

`tmux`                                                                                   

![tmux](https://github.com/user-attachments/assets/096c1625-6ff6-4196-96ca-b689a1c5c0bf)  


`tmux -u`

![tmux-u](https://github.com/user-attachments/assets/d2db76f1-274c-4726-ba59-1009536fe099)


## 2. Adafruit_DHT 11

Zalecam instalację sterownika z repo:

`git clone https://github.com/adafruit/Adafruit_Python_DHT.git`

szczegóły można znaleźć pod adresem:

https://github.com/adafruit/Adafruit_Python_DHT



>[!TIP]
> w razie brakujących pakietów, można je wyszukać za pomocą `yay` i parametru` -Ss`, np `yay -Ss setuptools`, a następnie instalacja wyszukanego pakietu




efekt koncowy

![Adafruit](https://github.com/user-attachments/assets/b5d5172f-c0dc-45fc-994a-f1ebdf0488b8)
