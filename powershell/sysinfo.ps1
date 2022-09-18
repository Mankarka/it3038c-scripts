Function getIP{
(Get-NetIPAddress).ipv4address | select-string "192*"
}

write-host(getIP)