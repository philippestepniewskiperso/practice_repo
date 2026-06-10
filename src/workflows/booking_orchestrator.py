from booking.inventory_service import InventoryService
from booking.notification_service import NotificationService
from booking.ticketing_service import TicketingService


class BookingOrchestrator:
    def __init__(self, inventory_service: InventoryService, ticketing_service: TicketingService,
                 notification_service: NotificationService) -> None:
        self.inventory_service = inventory_service
        self.ticketing_service = ticketing_service
        self.notification_service = notification_service

    def start(self, number_of_seats: int) -> None:
        if self.inventory_service.reserve_inventory(number_of_seats):
            self.ticketing_service.print_tickets(number_of_seats)
        else:
            self.notification_service.notify()
