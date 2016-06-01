ansible testserver -m ping
ansible testserver -m command -a uptime
ansible testserver -a "tail /var/log/dmesg"
ansible testserver -s -a "tail /var/log/syslog"
