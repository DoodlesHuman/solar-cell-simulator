class Carrier:
    def __init__(self, charge_type, position, velocity):
        self.charge_type = charge_type # electron or hole
        self.positon = position
        self.velocity = velocity

    def move(self, field, dt):
        q = -1 if self.charge_type == 'electron' else 1
        force = q * field.value_at(self.positon)
        acceleration = force / 1  # unit mass is assumed
        self.velocity =  self.velocity + (acceleration * dt)
        self.positon = self.positon + (self.velocity * dt)
        