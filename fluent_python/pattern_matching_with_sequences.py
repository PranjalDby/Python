import winsound
class InvalidException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Robot:
    def __init__(self,fact_id) -> None:
        self.fact_id = fact_id

    def __beep(self,times,frequency):
        winsound.PlaySound('Pandmonium❤️❤️.mp3',winsound.SND_NOWAIT)

    def handle_command(self,command):

        match command.split(" "):
            case ['BEEPER',frequency,times]:
                self.__beep(int(times),int(frequency))
            case _:
                raise InvalidException("Message Error")
            
robot_jarvis = Robot(5236)
robot_jarvis.handle_command("BEEPER 540 3")

def phone_country_code_verifier(phone_number):
    if phone_number == None:
        raise InvalidException("Phone number is Empty")
    
    if '-' not in phone_number:
        raise InvalidException("Phone number without '-' seprated country code")
    
    new_number = phone_number.split('-')
    print(new_number[0])
    match str(new_number[0]):
        case "+91":
            print("Country is India ")

        case '+1':
            print("Country is US ")

phone_country_code_verifier("+1-552423")

metro_areas = [
 ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
 ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
 ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
 ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
 ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

# this process is advance unpacking or destructing
for record in metro_areas:
    match record:
        case (name,_,_,(lat,lon)) if lon <= 9:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

