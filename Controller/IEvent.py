from abc import ABC, abstractmethod

class IEvent(ABC):
    @abstractmethod
    def handle(ui_instacne):
        pass