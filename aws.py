#!/usr/bin/env python

import boto.ec2
from ec2 import Ec2

class Aws(object):
    
    def __init__(self, access_key, secret_key):
        print "Initiating AWS configuration..."
        self.access_key = access_key
        self.secret_key = secret_key
        self.ec2_context = Ec2(self.access_key, self.secret_key)
    
    def print_active_instances(self, index=None):
        print "Found {} instance(s)\n".format(len(self.ec2_context.instances))
        print "#\tInstance ID\tPublic IP\tSize\t\tStatus"
        if index != None:
            pass
        for i, instance in enumerate(self.ec2_context.instances):
            print "{}\t{}\t{}\t{}\t{}".format(i, instance.id, instance.ip_address, instance.instance_type, instance.state)
        print ''
