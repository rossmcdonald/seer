#!/usr/bin/env python

from cmd import Cmd
from ConfigParser import ConfigParser
from shlex import split
from sys import exit
from aws import Aws

class Shell(Cmd, object):
    config = None
    
    def __init__(self):
        super(Shell, self).__init__()
        self.load_credentials()
        self.aws_context = Aws(self.config.get('aws', 'access_key'), self.config.get('aws', 'secret_key'))
        self.intro = "Welcome to Seer. Type `help` to get started."
        self.prompt = "(seer) "
    
    def empty_line(self):
        pass
    
    def precmd(self, line):
        return line
    
    def preloop(self):
        pass
    
    def do_list(self, params):
        self.aws_context.print_active_instances()
    
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