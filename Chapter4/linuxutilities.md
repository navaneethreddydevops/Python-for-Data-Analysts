dd
iostat
fio

# SSH Tunneling
ssh -L 9998:localhost:15672 -p 22 navaneethreddydevops@10.201.127.0 -N -f

-L flag for port forwarding enabling

LocalPort 9998

Bind Remote Port 15672
22 SSH PORT
-f to put the process into background