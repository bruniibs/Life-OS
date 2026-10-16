
# função de criar uma tarefa
def add_task(tasks, next_id, title):
    task = {
        "id": next_id,
        "title": title,
        "completed": False
        }
    tasks.append(task)
    return next_id + 1

def complete_task(tasks, task_id):
    for task in tasks:
        if task_id == task['id']:
            task['completed'] = True
            return True
    
    return False


def remove_task(tasks, task_id):
    for task in tasks:
        if task_id == task['id']:
            tasks.remove(task)
            return True
    
    return False


def list_tasks(tasks):
    return tasks