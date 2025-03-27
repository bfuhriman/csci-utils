#!/usr/bin/expect

set username $env(ODIN_USERNAME)
set password $env(ODIN_PASSWORD)

spawn sudo openconnect --protocol anyconnect --user=$username https://remote.uga.edu
expect "Please enter your username and password." { send "01 Default\r" }
expect "Please enter your username and password." { send "$password\r" }
expect "Password:" { send "phone\r" }
interact
