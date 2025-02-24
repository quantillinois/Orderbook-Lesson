
from enum import Enum
from dataclasses import dataclass
import heapq
from typing import List


class Side(Enum):
    BUY = "buy"
    SELL = "sell"

@dataclass
class Order:
    price: float
    quantity: float
    side: Side
    order_id: str
    timestamp: int

@dataclass
class Trade:
    price: float
    quantity: float

class OrderBook():

    def __init__(self):
        pass

    def submitOrder(self, order: Order) -> List[Trade]:
        pass

    def cancelOrder(self, order_id: str) -> None:
        pass

    def getPriceLevels(self) -> List[float]:
        pass
    
    def getVolumeAtPrice(self, priceLevel: float) -> int:
        pass
