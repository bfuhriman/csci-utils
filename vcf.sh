#!/usr/bin/expect

if [ $# -eq 0 ]; then
  echo "Usage: vcf <node>"
  exit 1
fi

node=$1

set username $env(ODIN_USERNAME)
set password $env(ODIN_PASSWORD)

spawn ssh $username@vcf$node.cs.uga.edu
expect "password:" { send "$password\r" }
interact
