from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

class Create:
    
    def __init__(self, subscription_id, name, location):
        self.subscription_id = subscription_id
        self.name = name
        self.location = location
    
    def new_resource_group(subscription_id, name, location):
        
        configuration = Create(subscription_id, name, location)
                
        resource_group = Create.if_not_exists(configuration)
                
        return resource_group
    
    def if_not_exists(configuration):
        
        resource_group_client = Create.resource_group_client(configuration.subscription_id)
        
        resource_group_client.create_or_update(
            resource_group_name = configuration.name,
            parameters = {f"location": {configuration.location}}
        )
        
        return resource_group_client.check_existence(configuration.name)
    
    def resource_group_client(subscription_id):
        
        client = ResourceManagementClient(
            credential = DefaultAzureCredential(),
            subscription_id = subscription_id
        )
        
        resource_group_client = client.resource_groups
        
        return resource_group_client