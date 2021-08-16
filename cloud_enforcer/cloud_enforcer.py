"""Main module."""
import pip
import yaml
import ansible.runner

class LocalConfig:
    """
    Config construction.
    """
    def __init__(self, **entries):
        self.__dict__.update(entries)

def doconfig():
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

def enforce():
    """
    Run Ansible playbook with specified parameters.
    """
    


def main(args=None,
    config='',
    ansible_user='',
    ssh_key_path='',
    password_file='',
    password_prompt=False,
    inventory_limit='',
    playbook='',
    boot=False):
    """
    Replaces previous execution with Makefiles.
    """
    conf = doconfig()
    


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover


if __name__=='__main__':
    main()
