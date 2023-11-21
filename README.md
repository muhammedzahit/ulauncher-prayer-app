# Ulauncher - Prayer Times

![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-green.svg)

## Description

This extension allows you to get prayer times for your location. This extension uses Presendency of Religious Affairs of Turkey's website to get prayer times.

Actually Presendency of Religious Affairs of Turkey's has official API for getting prayer times. But this API only allows 5 request per day. And requires authentication. So I decided to use their website to get prayer times with web scraping method.

## Demo

![demo](video.gif)

## Requirements

- [Ulauncher](https://ulauncher.io/)
- [Python >= 3](https://www.python.org/)
- PIP Requirements:
    - [bs4](https://pypi.org/project/beautifulsoup4/)
    - [retrying](https://pypi.org/project/retrying/)
    - [requests](https://pypi.org/project/requests/)

## Install

First install PIP and check is succesfully installed

```
sudo apt install python3-pip && pip3 --version
```

Then install required packages via PIP (If you have PEP 668 "externally managed" error click [here](#pep-668))

```
pip install beautifulsoup4 retrying requests 
```

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/muhammedzahit/ulauncher-prayer-app
```

In extension preferences, you can set your location. Generally location is COUNTRY/CITY/PROVINCE or COUNTRY/CITY. For example: FRANCE/PARIS or TÜRKİYE/SAMSUN/ÇARŞAMBA

If you dont set your location, you can look up [sorted_cities.txt](https://github.com/muhammedzahit/ulauncher-prayer-app/blob/main/sorted_cities.txt) file and find your location. Then you can set Text ID or Numeric ID of your location.

## Usage

- Open ulauncher and type `prayer` or keyword that you set.

## Errors

### PEP 668

Some distros (like debian) don't trust PIP and gives you PEP 668 error. There is two solution for that error.

## 1 - Blindly Trust Packages :

This is not a recommened way to go. If you certain that this packages safe you can use this method. Add `--break-system-packages` at the end of pip command.
```
pip3 install beautifulsoup4 retrying requests  --break-system-packages
```

## 2 - Create a virtual enviroment :

You can create a virtual enviroment and use this enviroment for your system. This is the way recommend but tedious.

2.1 - First create [virtual enviroment](https://docs.python.org/3/library/venv.html). 
```
sudo apt install python3-venv
cd && python3 -m venv .venv
```

2.2 - Since ULauncher always use default python path we must change it. Easiest way to change python3 path is creating [alias](https://www.baeldung.com/linux/create-alias).
```
cd  && nano .bashrc
```

2.3 Add to end of the file python3 and pip3 aliases
```
alias python3='~/.venv/bin/python3'
alias pip3='~/.venv/bin/pip3'
```

2.4 Exit with `Ctrl+X` and say `Y` for saving file question. Update system settings.
```
source .bashrc
```

2.5 We changed default python path to virtual enviroment path. If you want to go back to original python just delete aliases from .bashrc and update system settings. 

2.6 Try pip command it will work
