#!/usr/bin/env python

import boto.ec2

class Ec2(object):
    
    connection_pool = []
    instances = []
    
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key
        #self.connect_to_all_regions()
        self.connect_to_region("us-east-1")
        self.connect_to_region("us-west-1")
        self.connect_to_region("us-west-2")
        self.update_all_instances()
    
    def region_connected(self, region):
        for r, _ in self.connection_pool:
            if r == region:
                return True
        return False
    
    def connect_to_all_regions(self):
        available_regions = boto.ec2.regions()
        for region in available_regions:
            self.connect_to_region(region.name)
    
    def connect_to_region(self, region):
        if not self.region_connected(region):
            conn = boto.ec2.connect_to_region(region, 
                    aws_access_key_id=self.access_key, 
                    aws_secret_access_key = self.secret_key)
            self.connection_pool.append([region, conn])
    
    def update_instances_from_connection(self, connection):
        reservations = connection.get_all_reservations()
        for r in reservations:
            instances = r.instances
            for i in instances:
                self.instances.append(i)
    
    def update_all_instances(self):
        for region, conn in self.connection_pool:
            self.update_instances_from_connection(conn)

    
