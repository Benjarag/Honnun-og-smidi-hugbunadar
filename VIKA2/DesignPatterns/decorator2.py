from abc import ABC, abstractmethod


class NoiseMaker(ABC):
    @abstractmethod
    def make_noise(self) -> str:
        pass

class Dog(NoiseMaker):
    def make_noise(self) -> str:
        return "Bark"

    
class NoiseMakerConsoleDecorator(ABC):
    def __init__(self, noise_maker: NoiseMaker):
        self.noise_maker = noise_maker

    def make_noise(self) -> str:
        noise = self.noise_maker.make_noise()
        print(noise)
        return noise
    

if __name__ == "__main__":
    dog = Dog()
    noisy_dog = NoiseMakerConsoleDecorator(dog)
    noisy_dog.make_noise()