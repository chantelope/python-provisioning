import uuid
from container_registry.create import Create

def test_should_create_container_registry(mocker):
    
    subscription_id = uuid.uuid4()
    resource_group = "test-rg"
    location = "uksouth"
    name = "container-registry"
    sku = "standard"
    
    mocker.patch("container_registry.create.Create.registry", return_value = True)
    
    container_registry = Create.container_registry(subscription_id, resource_group, location, name, sku)
    
    assert container_registry == True