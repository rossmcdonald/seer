#!/usr/bin/env python

import boto.ec2
from ec2 import Ec2

class Aws(object):
    
    def __init__(self, access_key, secret_key):
        print "Initiating AWS configuration..."
        self.access_key = access_key
        self.secret_key = secret_key
        self.ec2_context = Ec2(self.access_key, self.secret_key)
    
    def get_instances(self):
        return enumerate(self.ec2_context.instances)
        #print "Found {} instance(s)\n".format(len(self.ec2_context.instances))
        #print "#\tInstance ID\tPublic IP\tSize\t\tStatus"
        #summary=[]
        #for i in enumerate(self.ec2_context.instances):
            # TODO, figure out how to make this more extensible (specific attributes, etc.)
            # Will most likely need to create a class that represents a universal instance type
        #    info={  'id': i.id,
        #            'state': i.state, 
        #            'public-ip': i.ip_address, 
        #            'type': i.instance_type,
        #            }
        #    summary.append(info)
            #print "{}\t{}\t{}\t{}\t{}".format(i, instance.id, instance.ip_address, instance.instance_type, instance.state)
        #print ''
        #return summary
