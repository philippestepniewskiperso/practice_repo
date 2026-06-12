import abc
from dataclasses import dataclass
from typing import List


@dataclass
class Event:
    name: str
    value: int


class Listener(abc.ABC):
    @abc.abstractmethod
    def on_message(self, message: Event):
        pass


class MessageBus:
    def __init__(self):
        self._subs: List[Listener] = []

    def subscribe(self, l: Listener):
        self._subs.append(l)

    def publish(self, message: Event):
        for l in self._subs:
            l.on_message(message)
