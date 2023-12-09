from databricks_workspace.get import Get
from databricks.sdk.service.jobs import Task, NotebookTask

class Create:
    
    def __init__(self, host, token, job_name, task_list):
        self.host = host
        self.token = token
        self.name = job_name    
        self.task_list = task_list     
        
    
    def new_workflow_job(host, token, job_name, task_list):
                             
        configuration = Create(host, token, job_name, task_list)
        
        job = Create.workflow_configuration(configuration)
        
        return job
    
    def job_task(task_key):
        
        task_list = list()
    
        task = Task(
            task_key = task_key     
        )
        task_list.append(task)   
        
        return task_list
    
    def workflow_configuration(configuration):
        
        workspace = Get.databricks_workspace(configuration.host, configuration.token)
        
        workflow = workspace.jobs.create(
            name = configuration.name,
            tasks = configuration.task_list
        )
        
        return workflow