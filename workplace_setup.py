from subprocess import STDOUT, check_call
import os

def install_packages(package_names):
    for package_name in package_names:
        print('Installing package {}'.format(package_name))
        check_call(['sudo', 'apt-get', 'install', '-y', package_name],
                   stdout=open(os.devnull, 'wb'), stderr=STDOUT)
    print('Completed')


def create_directory(dir_name):
    # вот такой вот вариант я нашел как создать папочку)
    print('Creating directory'.format(dir_name))
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def change_rights(dir_name):
    print('Changing directory rights and owner...')


def get_linux_version():
    print('Checking linux distrib version')
    return 'Ubuntu14.04'


def edit_fstab(linux_version, dir_name):
    print('Editing /etc/fstab..')
    pass


def nfs_mount():
    print('Mounting nfs..')
    pass


def main():
    print("Starting to setup workplace...")

    # 1. apt-get install portmap nfs-common
    package_names = ['portmap', 'nfs-common']
    install_packages(package_names)

    # 2. sudo mkdir /qtapps
    dir_name = '/qtapps'
    create_directory(dir_name)

    # 3.1. sudo chown madmin:root /qtapps
    # 3.2  sudo chmod -R g+w /qtapp
    change_rights(dir_name)

    # 4 sudo nano /etc/fstab
    # # QT APPS
    # qtsoft.lege.grp/lege-soft/qt5-x64-Ubuntu14.04 /qtapps nfs ro,hard,intr 0 0
    # or
    # qtsoft.lege.grp/lege-soft/qt5-x64-Ubuntu16.04 /qtapps nfs ro,hard,intr 0 0
    linux_version = get_linux_version()
    edit_fstab(linux_version, dir_name)

    # 5. sudo mount -a
    nfs_mount()




if __name__ == '__main__':
    main()