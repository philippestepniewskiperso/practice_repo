from message_bus.message_bus import MessageBus, Listener


class NotificationService(Listener):

    def __init__(self,message_bus:MessageBus) -> None:
        self.message_bus = message_bus
        self.message_bus.subscribe(self)

    def on_message(self, message):
        if message.name == "CapacityExceeded":
            self.notify()

    def notify(self):
        print("deso bro")
