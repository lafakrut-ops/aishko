
class Engine:
    def __init__(self, power):
        self.power = power  
    def start_engine(self):
        return f"Двигун потужністю {self.power}запущено."


class Body:
    def __init__(self, color):
        self.color = color  

    def change_color(self, new_color):
        self.color = new_color
        return f"Колір  {self.color}."
class Car(Engine, Body):
    def __init__(self, power, color, model):
        
        Engine.__init__(self, power)
        Body.__init__(self, color)
        self.model = model  
    def drive(self):
        status = self.start_engine()
        return f"{self.model} ({self.color}) рушає з місця. {status}"
