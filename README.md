# Ansible to upgrade|precheck|postcheck for Robin CNP Platform 
## Make sure ansible,python,pip is installed on the control node
## Update host details on inventory/hosts.ini file. 

# Examples

## Set up ansible
Install python 3.9
pip3 install ansible
pip3 install paramiko
   
## To download robin binaries
1. Update config.yaml file in main dir
2. Run ansible cmd:
   -ask-become-pass option sudo access
   ansible-playbook robin-upgrade.yml  --ask-pass --ask-become-pass --tags download-robin-bin --extra-vars "@config.yaml" -c paramiko
3. If passwordless authentication is enabled
   ansible-playbook robin-upgrade.yml --tags download --extra-vars "@config.yaml"     
  


## To do prechecks before upgrade
  ansible-playbook robin-upgrade.yml  --ask-pass --ask-become-pass --tags pre-check --extra-vars "@config.yaml" -c paramiko

## Capture cluster state before upgrade
  ansible-playbook robin-upgrade.yml  --ask-pass --ask-become-pass --tags cluster-status --extra-vars "@config.yaml" -c paramiko 

## Preupgrade tasks
1. ansible-playbook robin-upgrade.yml  --tags pre-upgrade-tasks-550  --ask-pass --ask-become-pass -e "@config.yaml" -c paramiko 

## To upgrade
1. Update config.yaml file with correct robin version
2. Run ansible cmd:
   ansible-playbook robin-upgrade.yml  --ask-pass --ask-become-pass --tags upgrade --extra-vars "@config.yaml" -c paramiko

## post upgrade tasks
1. ansible-playbook robin-upgrade.yml  --tags postcheck  --ask-pass --ask-become-pass -e "@config.yaml" -c paramiko
2. ansible-playbook robin-upgrade.yml  --tags post-upgrade-tasks-550  --ask-pass --ask-become-pass -e "@config.yaml" -c paramiko


## To run single task
ansible-playbook robin-upgrade.yml --list-tags

1. playbook: robin-upgrade.yml

   play #1 (all): Apply roles to hosts	TAGS: []
      TASK TAGS: [always, artifactory-cleanup, cluster-state, cluster-status, copy-kubeconfig-all, download-robin-bin, ha-install, host-script-install, host-uninstall, k8s-script-install-all-worker, k8s-script-install-primary, k8s-uninstall, k8splus-script-install-primary, k8splus-uninstall, non-ha-install, precheck, reboot_check, robin-app-cleanup, robin-cnp-uninstall, robin-script-install-primary, uninstall, upgrade, upgrade-precheck, v5.3, v5.4]

2. ansible-playbook robin-upgrade.yml -u root --ask-pass --tags host-script-install  --extra-vars "@config.yaml" -c paramiko



## Skip single tag for e.g you want to skip host-install ,you can run as below
ansible-playbook robin-upgrade.yml -u root --ask-pass --skip-tags k8s-script-install-all-worker,k8s-script-install-primary,k8splus-script-install-primary --extra-vars "@config.yaml"

## Adhoc command
ansible all -m ansible.builtin.yum -a "name=bind-utils state=present" -u root  --ask-pass
ansible all -m shell -a "echo 'anupkumar:test123' | chpasswd" -u root --ask-pass


## Run as su user for all tags like  below cmd
ansible-playbook robin-upgrade.yml  --ask-pass --ask-become-pass -u anupkumar   --tags download-robin-bin  --extra-vars "@config.yaml"

# For macos:
## Install python3  and run below cmds
pip install ansible
pip install paramiko

## Use ansible cmds as belwow from macos:
ansible-playbook robin-upgrade.yml -c paramiko --ask-pass --tags non-ha-install --extra-vars "@config.yaml"
ansible all -m ansible.builtin.yum -a "name=bind-utils state=present" -u root  --ask-pass -c paramiko
ansible all -m shell -a uptime  -u root --ask-pass
