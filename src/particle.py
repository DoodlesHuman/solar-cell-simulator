class Carrier:
    def __init__(self, charge_type, position, velocity):
        self.charge_type = charge_type # electron or hole
        self.position = position
        self.velocity = velocity

    def move(self, field, dt):
        q = -1 if self.charge_type == 'electron' else 1
        force = q * field.value_at(self.position)
        acceleration = force / 1  # unit mass is assumed
        self.velocity =  self.velocity + (acceleration * dt)
        self.position = self.position + (self.velocity * dt)
        