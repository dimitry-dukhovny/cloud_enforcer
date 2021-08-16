"""Console script for cloud_enforcer."""
import sys
import click
try:
    import cloud_enforcer.cloud_enforcer as ce
except:
    import cloud_enforcer as ce


@click.command()
@click.option('--reinstall', '-r',
    type=click.BOOL, default=False,
    help='Force PYPI dependency reinstallation in user namespace.')
@click.option('--config', '-c', default='cloud_enforcer.yml',
    help='Specify a YAML-formatted config file')
@click.option('--ansible_user', '-u', default='root',
    help='Remote user name.')
@click.option('--ssh_key_path', '-s', type=click.PATH, default='.ssh/id_rsa',
    help='SSH key location.')
@click.option('--password_file', '-f', type=click.PATH, default='',
    help='Password file location.')
@click.option('--password_prompt', '-P', type=click.BOOL, default=False,
    help='Prompt for a password.')
@click.option('--inventory_limit', '-l', default='all',
    help='Host or group run limit.')
@click.option('--playbook', '-p', default='.local/ansible/playbooks/wholecycle.yml',
    help='Host or group run limit.')
@click.option('--boot', '-n', type=click.BOOL, default=False,
    help='Allow reboots.')

def main(args=None,
    config='',
    ansible_user='',
    ssh_key_path='',
    password_file='',
    password_prompt=False,
    inventory_limit='',
    playbook='',
    boot=False):
    """Console script for cloud_enforcer."""
    click.echo("Enforcement dependencies and wrapper.")
    if password_file and password_prompt:
        ERR("You specified a password file.  Skipping password prompt.")
        password_prompt=False
    ce.main(config=config,
        ansible_user=ansible_user,
        ssh_key_path=ssh_key_path,
        password_file=password_file,
        password_prompt=password_prompt,
        inventory_limit=inventory_limit,
        playbook=playbook,
        boot=boot)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
