from celery.task.control import inspect

i = inspect()
print i.scheduled()
print '--'
active = i.active()
# import pdb; pdb.set_trace()
print '---'
print i.reserved()