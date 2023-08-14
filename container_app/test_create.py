import uuid
from container_app.create import Create

def test_should_create_container_app(mocker):
    
    subscription_id = uuid.uuid4()
    resource_group = "test-rg"
    location = "uksouth"
    app_name = "container-app"
    env_name = "env"
    
    mocker.patch("container_app.create.Create.app", return_value = True)
    
    container_app = Create.container_app(subscription_id, resource_group, location, app_name, env_name)
    
    assert container_app == True