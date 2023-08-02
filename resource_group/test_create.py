import uuid
from resource_group.create import Create

def test_should_create_resource_group(mocker):
    
    subscription_id = uuid.uuid4()
    name = "test-rg"
    location = "uksouth"
    
    mocker.patch("resource_group.create.Create.if_not_exists", return_value = True)
    
    resource_group = Create.new_resource_group(subscription_id, name, location)
    
    assert resource_group == True