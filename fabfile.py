import os
from fabric.api import run
from fabric.api import local
from fabric.api import settings
from fabric.api import env
from fabric.api import task
from fabric.api import roles
from fabric.api import sudo
from fabric.api import cd
from fabric.contrib import files

env.docker = ['ubuntu']

env.roledefs = {
    "local" : ["root@localhost"]
}

""" vagrant related """

@roles("local")
def install_vagrant(clean=False,user=False):

    # if not user:
    #     print "you must provide your user name"
    #     sys.exit(2)

    # run("apt-get update")

    # if clean == "true":
    #     run("apt-get -y -f remove virtualbox* vagrant")
    #     run("apt-get -y autoremove")

    # """ virtualbox """
    # run("apt-get -y install virtualbox git-core")        
    # run("usermod -a -G vboxusers %s" % user)

    # """ vagrant """
    # run("cd /tmp && wget https://dl.bintray.com/mitchellh/vagrant/vagrant_1.6.2_x86_64.deb")
    # with settings(warn_only=True):
    #     run("cd /tmp && dpkg -i vagrant_1.6.2_x86_64.deb")
    #     run("apt-get -y install -f")

    # """ prerequisites """
    # run("apt-get -y install curl libxslt1-dev libxml2-dev build-essential")

    """ rvm """
    with cd("/home/%s" % user):
        #run("apt-get -y install curl git-core  build-essential openssl libreadline6 libreadline6-dev curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-0 libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf libc6-dev ncurses-dev automake libtool bison subversion")
        sudo("curl -sS https://get.rvm.io > /home/%s/rvm.sh" % user,user=user,shell=True)
        sudo("chmod +x /home/%s/rvm.sh " % user)
        sudo("/home/%s/rvm.sh" % user)

    #     files.append("/home/%s/.profile" % user,"source /usr/local/rvm/scripts/rvm")
    #     sudo("source /etc/profile && rvm install 1.9.2")
    #     files.append("/etc/profile","rvm use 1.9.2 --default")    

    # """ install veewee """
    # with cd("/home/%s" % user):
    #     sudo("git clone https://github.com/jedi4ever/veewee.git",user=user)
    
    # with cd("/home/%s/veewee" % user):
    #     sudo("rvm use 1.9.2@veewee --create",user=user)
    #     sudo("gem install bundler",user=user)
    #     sudo("bundle install",user=user)

@roles("local")
def buildbox(name=False,template=False,user=False):
    if not name or not template or not user:
        print "You must provide a box name, a template and a target user"
        sys.exit(2)
    else:
        with cd("/root/veewee"):
            run("bundle exec veewee vbox define '%s' '%s'" % (name,template))
            run("bundle exec veewee vbox build %s" % name)

