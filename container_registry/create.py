from azure.mgmt.containerregistry import ContainerRegistryManagementClient
from azure.identity import DefaultAzureCredential

class Create:
    
    def __init__(self, subscription_id, resource_group, location, name, sku):
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.location = location
        self.name = name
        self.sku = sku
    
    def container_registry(subscription_id, resource_group, location, name, sku):
        
        configuration = Create(subscription_id, resource_group, location, name, sku)
        
        registry = Create.registry(configuration)
        
        return registry
    
    def registry(configuration):
        
        client = Create.container_registry_client(configuration.subscription_id)
        
        client.registries.begin_create(
            resource_group_name = configuration.resource_group,
            registry_name = configuration.name,
            registry = {
                "location": f"{configuration.location}",
                "properties": { "adminUserEnabled": True},
                "sku": f"{configuration.sku}"
            }
        )
        
        registry_exists = client.registries.get(configuration.resource_group, configuration.name)
        
        if registry_exists.id is not None:
            
            return True
        
        return False
    
    def container_registry_client(subscription_id):
        
        client = ContainerRegistryManagementClient(
            credential = DefaultAzureCredential(),
            subscription_id = subscription_id
        )
        
        return client