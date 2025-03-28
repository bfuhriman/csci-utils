#!/usr/bin/expect

if { [llength $argv] == 0 } {
    puts "Usage: vcf <node>"
    exit 1
}

set node [lindex $argv 0]

set username $env(ODIN_USERNAME)
set password $env(ODIN_PASSWORD)

spawn ssh -q $username@vcf$node.cs.uga.edu
expect "password:" { send "$password\r" }
interact
