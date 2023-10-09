import datetime
class Events:
    def __init__(self,name,date,user,evnt_type) -> None:
        self.name = name
        self.date = date
        self.user = user
        self.evnt_type = evnt_type

    def login(self):
        print("{} is logged in by {}" + self.name,self.user)

def get_event_date(events):
    return events.date
        
def current_user(events):
    events.sort(key = get_event_date)
    machines = {}
    for i in event_list:
        if i.name not in machines:
            machines[i.name] = set()

        if i.evnt_type == "login":
            machines[i.name].add(i.user)
        else:
            machines[i.name].remove(i.user)

    return machines

def generate_report(machines):
    for key,va in machines.items():
        if len(va) > 0:
            user_list = " ".join(va)
            print("{} {}".format(key,user_list))

event_list = [Events("Machine1","22-02-2003","Pranjal","login"),
              Events("Machine2","30-02-2004","Joseph","login")]


machines = current_user(event_list)
generate_report(machines)


