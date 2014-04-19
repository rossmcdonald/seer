#!/usr/bin/env python

from cmd import Cmd
from ConfigParser import ConfigParser
from shlex import split
from sys import exit
from aws import aws
import re

class Shell(Cmd, object):
    config = None
    
    def __init__(self):
        super(Shell, self).__init__()
        self.load_credentials()
        self.aws_context = aws.Aws(self.config.get('aws', 'access_key'), self.config.get('aws', 'secret_key'))
        self.intro = "Welcome to Seer. Type `help` to get started."
        self.prompt = "(seer) "
    
    def empty_line(self):
        pass
    
    def precmd(self, line):
        return line
    
    def preloop(self):
        pass
    
    def do_list(self, params):
        reg = None
        if len(params) != 0:
            exp = ''
            for i in params:
                exp += ' '.join(str(i))
            try:
                reg = re.compile(exp)
            except re.error:
                print 'Invalid regex expression [%s].\n' % exp
                reg = None
        for i, instance in self.aws_context.get_instances():
            details = '%s | %s | %s | %s | %s' % (i,
                                                instance.id, 
                                                instance.public_dns_name, 
                                                instance.instance_type,
                                                instance.key_name)
            if reg == None:
                print details
            else:
                try:
                    for s in split(details):
                        if reg.match(s):
                            print details
                except re.error:
                    pass
    
    def do_quit(self, params):
        exit("Exiting...")
        
    def do_exit(self, params):
        exit("Exiting...")
    
    def load_credentials(self):
        self.config = ConfigParser()
        self.config.read("credentials")

if __name__ == "__main__":
    app = Shell()
    try:
        app.cmdloop()
    except (KeyboardInterrupt, SystemExit):
        print "Stopping..."
