exam32
  -- make the hosts definition in one folder called inventory. All files under this folder can include hosts/group definition
  -- create one dynamic inventory python file under folder inventory. This script will automatically find all webservers in the amazon ap-southeast-1 region based on tag:UsageType
  -- dynamic inventory script need to reponse two argument call --list and --host. --list returns the group definition, in our example, it will return all web servers under "webservers" group. --host will return the detail information for a host, in our example, we return ansible_ssh_host and ansible_ssh_port

chap04
  -- regsiter variable for task whoami.yml, ignore_errors will not stop the running of ansible, then you have chance to output the return from command to find out what's going wrong
  -- facts.yml print out some information the ansible gets from the target host
     -- return all facts gathered by ansible: ansible webserver1 -m setup, ansible webserver1 -m setup -a 'filter=ansible-eth*'
     -- any task returns a dictionary whose contans ansible_facts, all keys under this dictionary will be stored as a variable in mem, see ec2facts.yml
        ansible-playbook ec2facts.yml -vvv
     -- you can use the set_facts module to expose some information as a variable. set_facts: <variable_name>=<value>
  -- global available variables: hostvars, inventory_hostname, groups(dict, key is groupname, value is hosts list), group_names(list), play_hosts (list), ansible_version
  -- set variable in command line using "-e" option, check "ansible-playbook greeting.yml -e greeting=hiya" or ansible-playbook greeting.yml -e 'greeting="hi there"'
