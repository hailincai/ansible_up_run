exam32
  -- make the hosts definition in one folder called inventory. All files under this folder can include hosts/group definition
  -- create one dynamic inventory python file under folder inventory. This script will automatically find all webservers in the amazon ap-southeast-1 region based on tag:UsageType
  -- dynamic inventory script need to reponse two argument call --list and --host. --list returns the group definition, in our example, it will return all web servers under "webservers" group. --host will return the detail information for a host, in our example, we return ansible_ssh_host and ansible_ssh_port
