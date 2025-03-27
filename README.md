## About
Programming on Odin can be annoying. Make it easier with csci-utils, featuring:

`vpn.sh` - A script that allows you to connect to UGA's remote access VPN with a single command. You'll still need to answer your phone to verify your identity (the script can be altered if you prefer a different form of 2FA).

`odin.sh` - A script that allows you to connect to UGA's Odin server with a single command.

`ctest.py` - A python script that looks for an assignment PDF in the current directory and automatically executes any commands in the "Examples" section, making testing your program significantly easier. Specifically designed for CSCI 1730 (Systems Programming), but might work for some other courses.

## Setup
Navigate to your home directory and clone the repository:
```
git clone https://github.com/bfuhriman/csci-utils
```

### VPN and SSH Scripts
Add the following to your `~/.bashrc` file, replacing `your_username` and `your_password` with your UGA credentials (your username is what comes before `@uga.edu` in your email).
```
alias vpn="~/csci-utils/vpn.sh"
alias odin="~/csci-utils/odin.sh"
export ODIN_USERNAME="your_username"
export ODIN_PASSWORD="your_password"
```
Run the following command to update `~/.bashrc`.
```
source ~/.bashrc
```
You may now use the `vpn` and `odin` commands from anywhere on your system.

### ctest
Add the following line somewhere in your `~/.bashrc` file.
```
alias ctest="python3 ~/csci-utils/ctest.py"
```
Run the following commands to update `~/.bashrc` and install `pymupdf`.
```
source ~/.bashrc
pip install pymupdf
```
You may now use the `ctest` command in any directory that contains a C executable and an assignment PDF. You'll need to do this process twice if you want to use `ctest` on both Odin and your personal computer.
