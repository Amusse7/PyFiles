#Ali Khaleel
#Abdulkadir Musse
#Abel Teklemariam
#Asad Zaheer

import random
import matplotlib.pyplot as plt

class TemperatureSensorSimulator:
    def __init__(self, baseline=20.0, fluctuation=2.0, noise=0.2):
        self.baseline = baseline
        self.fluctuation = fluctuation
        self.noise = noise
        self.phase = 0

    def _normalized_value(self):
        # Base value using a sine function to simulate daily temperature fluctuations
        base = self.fluctuation * random.choice([-1, 1]) * random.random()
        self.phase += random.uniform(0.005, 0.015)

        # Add some noise to the value for minute-by-minute variations
        variation = (random.random() - 0.5) * self.noise
        return self.baseline + base + variation

    @property
    def value(self):
        # Get a simulated temperature reading
        return self._normalized_value()

def main():
    simulator = TemperatureSensorSimulator()
    values = [simulator.value for _ in range(500)]

    plt.plot(values)
    plt.title("Simulated Indoor Temperature Data")
    plt.xlabel("Time (Minutes)")
    plt.ylabel("Temperature (°C)")
    plt.show()

if __name__ == "__main__":
    main()
