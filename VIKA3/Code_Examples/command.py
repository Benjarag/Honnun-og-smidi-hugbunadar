from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class Light:
    def on(self):
        print("Lights are now on")
    
    def off(self):
        print("Lights are now off")

class LightsONCommand(Command):
    def __init__(self, light: Light) -> None:
        self.__light = light
    
    def execute(self) -> None:
        self.__light.on()

class LightsOFFCommand(Command):
    def __init__(self, light: Light) -> None:
        self.__light = light
    
    def execute(self) -> None:
        self.__light.off()

class SimpleRemote:
    def set_command(self, command: Command) -> None:
        self.__command = command
    
    def press_button(self) -> None:
        self.__command.execute()

if __name__ == '__main__':
    remote = SimpleRemote()
    light = Light()
    
    lights_on_command = LightsONCommand(light)
    lights_off_command = LightsOFFCommand(light)

    # Turn the lights on
    remote.set_command(lights_on_command)
    remote.press_button()

    # Turn the lights off
    remote.set_command(lights_off_command)
    remote.press_button()
    
