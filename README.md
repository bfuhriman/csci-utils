## About
Programming on Odin can be annoying. Make it easier with csci-utils, featuring:

`vpn.sh` - A script that allows you to connect to UGA's remote access VPN with a single command. You'll still need to answer your phone to verify your identity (the script can be easily altered if you prefer a different form of 2FA).

`odin.sh` - A script that allows you to connect to UGA's Odin server with a single command.

`ctest.py` - A python script that looks for an assignment PDF in the current directory and automatically executes any commands in the "Examples" section, making testing your program significantly easier. Specifically designed for CSCI 1730 (Systems Programming), but might work for some other courses.

## Setup
Navigate to your home directory and clone the repository:
```
git clone https://github.com/bfuhriman/csci-utils
```
Then, add the following to your `~/.bashrc` file, replacing `your_username` and `your_password` with your UGA credentials (your username is what comes before `@uga.edu` in your email). Make sure to update these file paths if you move `csci-utils` out of the home directory.
```
alias vpn="~/csci-utils/vpn.sh"
alias odin="~/csci-utils/odin.sh"
alias ctest="python ~/csci-utils/ctest.py"
export ODIN_USERNAME="your_username"
export ODIN_PASSWORD="your_password"
```
Congrats! You may now use `vpn`, `odin`, and `ctest` from anywhere on your system.
