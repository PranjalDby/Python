import platform 
mysys = platform.uname()
print(f'System: {mysys.system}')
print(f'Node Name: {mysys.node}')
print(f'Release Ver: {mysys.release}')
print(f'System Ver: {mysys.version}')
print(f'Machine: {mysys.machine}')
print(f'Processor: {mysys.processor}')
