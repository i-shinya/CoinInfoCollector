from enum import Enum


class TradeCode(Enum):
    BIT_FLYER = ("BIT_FLYER", "bit_flyer")
    ZAIF = ("ZAIF", "zaif")


class CoinType(Enum):
    BIT_COIN = ("BIT_COIN", "ビットコイン")


class TradeStatus(Enum):
    ORDER = ("ORDER", "注文中")
    CONTRACT = ("CONTRACT", "約定済")
    FINISH = ("FINISH", "反対売買成立")
    CANCEL = ("CANCEL", "取消")
