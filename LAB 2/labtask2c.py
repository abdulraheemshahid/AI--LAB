class ClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):

        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"

        if target_mode != self.previous_mode:
            send_command = True
        else:
            send_command = False

        previous_mode = self.previous_mode
        self.previous_mode = target_mode

        return previous_mode, target_mode, send_command
agent = ClassroomAgent()
percepts = [
    (29, True),
    (29, True),
    (20, True),
    (26, True),
    (19, True),
    (29, False),
    (29, False)
]
print("Step | Previous | Percept | Target | Command")

for step, percept in enumerate(percepts, 1):
    previous, target, send = agent.act(*percept)

    if send:
        command = "SEND"
    else:
        command = "NO"
    print(step, previous, percept, target, command)