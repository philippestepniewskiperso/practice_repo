from message_bus.message_bus import MessageBus, Listener, Event


class BookingService(Listener):
    def __init__(self, message_bus:MessageBus) -> None:
        self.message_bus = message_bus
        self.message_bus.subscribe(self)

    def on_message(self, message: Event):
        pass

    def request_booking(self, number_of_seats: int) -> None:
        # collect validate
        print("BookingRequested")
        message : Event = Event(name="BookingRequested", value=number_of_seats)
        self.message_bus.publish(message)
        self.message_bus.publish(message)

