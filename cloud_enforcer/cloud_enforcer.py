"""Main module."""
import pip
import yaml
import ansible_runner
import colorama

def OUT(outstring=''):
    '''
    Simple output printer.
    Will halt the program if it fails to write to stdout.

    Args:
        outstring: a string or anything that can become one
    Returns:
        None
    '''
    try:
        outstring = str(outstring)
    except:
        outstring = ''
    #sys.stdout.write(outstring + '\n')
    print(colorama.Fore.GREEN + outstring + colorama.Style.RESET_ALL, file=sys.stdout, flush=True)

def ERR(outstring=''):
    '''
    Simple error printer.
    Will halt the program if it fails to write to stderr.

    Args:
        outstring: a string or anything that can become one
    Returns:
        None
    '''
    try:
        outstring = str(outstring)
    except:
        outstring = ''
    #sys.stderr.write(outstring + '\n')
    print(colorama.Fore.RED + outstring + colorama.Style.RESET_ALL, file=sys.stderr, flush=True)


class LocalConfig:
    """
    Config construction.
    """
    def __init__(self, **entries):
        self.__dict__.update(entries)

def doconfig(config):
    """
    Return config object from YAML file read with '-c' parameter.
    """
    try:
        with open(config) as FH:
            configmap = yaml.safe_load(FH)
    except:
        ERR('Could not open configuration file.')
    conf = LocalConfig(**configmap)
    return(conf)

def saveconfig(config):
    """
    Save config as entered on the commandline
    """
    pass
    

def enforce(conf):
    """
    Run Ansible playbook with specified parameters.
    """
    play = ansible.runner.run(
        conf.playbook='',
        conf.inventory='',
        conf.host_pattern='all',
        conf.extravars=extravars)
    OUT("{}: {}".format(play.status, play.rc))
    # successful: 0
    for each_host_event in play.events:
        OUT(each_host_event['event'])
    print("Final status:")
    print(play.stats)
    return(play)

def main(args=None,
    config='',
    ansible_user='',
    ssh_key_path='',
    password_file='',
    password_prompt=False,
    inventory_limit='',
    playbook='',
    boot=False,
    argument='play'):
    """
    Replaces previous execution with Makefiles.
    """
    os.environ['ANSIBLE_CONFIG'] = "%s/ansible.cfg" % (ansible_tree)
    extravars = {}
    conf = doconfig()
    conf.ansible_user = ansible_user
    conf.ssh_key_path = ssh_key_path
    conf.password_file = password_file
    conf.password_prompt = password_prompt
    conf.inventory_limit = inventory_limit
    conf.playbook=conf.playbook,
    conf.inventory="%s/inventory" % (ansible_tree)
    conf.host_pattern=inventory_limit
    conf.extravars=extravars
    conf.extravars['accept_boot'] = boot

    if conf.password_file:
        try:
            with open(conf.password_file) as FH:
                conf.extravars['ansible_password'] = FH.read()
        except:
            ERR('Could not read %s' % (str(conf.password_file)))

    if conf.password_prompt:
        try:
            conf.extravars['ansible_password'] = getpass(
                "Password for %s: " % (conf.ansible_user))
        except:
            ERR('Could not parse user entry for password.')

    conf.extravars['ansible_sudo_password'] = conf.extravars['ansible_password']
    if argument == 'play':
        enforce(conf)
    elif argument == 'save':
        saveconfig(conf)
    else:
        ERR('Options are "play" or "save ," not "%s .' % (argument))


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover


if __name__=='__main__':
    main()
