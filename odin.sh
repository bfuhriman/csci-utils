#!/usr/bin/expect

set username $env(ODIN_USERNAME)
set password $env(ODIN_PASSWORD)

spawn ssh $username@odin.cs.uga.edu
expect "password:" { send "$password\r" }
interact
