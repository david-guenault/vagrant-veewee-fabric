# -*- coding: utf-8 -*-

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
    "local" : ["localhost"]
}

""" vagrant related """

@roles("local")
def install_rvm4user(user=False,password=False):

    if not user or not password:
        print "user and password are mandatory"
        print "fab install_rvm4user:user=username,password=*******"
        sys.exit(2)

    env.user = root
    run("apt-get update")
    run("apt-get -y install curl git-core  build-essential openssl libreadline6 libreadline6-dev curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-0 libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf libc6-dev ncurses-dev automake libtool bison subversion")


    HOME = "/home/%s" % user
    env.user = user
    env.password = password

    with cd(HOME):
        run("curl -sS https://raw.githubusercontent.com/wayneeseguin/rvm/master/binscripts/rvm-installer > %s/rvm.sh" % HOME,shell=True)
        run("chmod +x %s/rvm.sh " % HOME)
        run("%s/rvm.sh" % HOME)
        files.append("%s/.profile" % HOME,"source %s/.rvm/scripts/rvm" % HOME)
        run("source %s/.profile && rvm install 1.9.2" % HOME)
        files.append("%s/profile" % HOME,"rvm use 1.9.2 --default")    
        run("rm -f %s/rvm.sh" % HOME)


@roles("local")
def install_vagrant(clean=False):
    # """ virtualbox """
    env.user = "root"
    run("apt-get -y install virtualbox")        

    # """ vagrant """
    run("cd /tmp && wget https://dl.bintray.com/mitchellh/vagrant/vagrant_1.6.2_x86_64.deb")
    with settings(warn_only=True):
         run("cd /tmp && dpkg -i vagrant_1.6.2_x86_64.deb")
         run("apt-get -y install -f")

    # """ prerequisites """
    # run("apt-get -y install curl libxslt1-dev libxml2-dev build-essential")


    # """ install veewee """
    # with cd("/home/%s" % user):
    #     sudo("git clone https://github.com/jedi4ever/veewee.git",user=user)
    
    # with cd("/home/%s/veewee" % user):
    #     sudo("rvm use 1.9.2@veewee --create",user=user)
    #     sudo("gem install bundler",user=user)
    #     sudo("bundle install",user=user)

@roles("local")
def enable_virtualbox4user(user=False):
    if not user:
        print "user is mandatory"
        sys.exit(2)

    run("usermod -a -G vboxusers %s" % user)

@roles("local")
def buildbox(name=False,template=False,user=False):
    if not name or not template or not user:
        print "You must provide a box name, a template and a target user"
        sys.exit(2)
    else:
        with cd("/root/veewee"):
            run("bundle exec veewee vbox define '%s' '%s'" % (name,template))
            run("bundle exec veewee vbox build %s" % name)

