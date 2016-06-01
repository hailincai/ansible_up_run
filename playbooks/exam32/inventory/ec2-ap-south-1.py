#!/usr/bin/env python
# Adapted from Mark Mandel's implementation
# https://github.com/ansible/ansible/blob/devel/plugins/inventory/vagrant.py
import argparse
import json
import paramiko
import subprocess
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="ec2 inventory script")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', action='store_true')
    group.add_argument('--host')
    return parser.parse_args()


def list_running_hosts():
    cmd = '/usr/local/bin/aws ec2 describe-instances --profile neulion --region ap-southeast-1 --filters file://filters.json'
    status = subprocess.check_output(cmd.split()).rstrip()
    hosts = []
    cmdReturn = json.loads(status)
    for reservation in cmdReturn['Reservations']:
    	for instance in reservation['Instances']:
            if (instance['State']['Name'] == 'running'):
            	hosts.append(instance['PublicIpAddress'])
    return hosts


def get_host_details(host):
    return {'ansible_ssh_host': c[host],
            'ansible_ssh_port': c[22]}


def main():
    args = parse_args()
    if args.list:
        hosts = list_running_hosts()
        json.dump({'webservers': hosts}, sys.stdout)
    else:
        details = get_host_details(args.host)
        json.dump(details, sys.stdout)

if __name__ == '__main__':
    main()