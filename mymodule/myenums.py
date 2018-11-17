from enum import Enum


class TradeCode(Enum):
    BIT_FLYER = (1, "bit_flyer")
    ZAIF = (2, "zaif")


class CoinType(Enum):
    BIT_COIN = (1, "ビットコイン")


class TradeStatus(Enum):
    ORDER = (1, "注文中")
    CONTRACT = (2, "約定済")
    FINISH = (3, "反対売買成立")
    CANCEL = (4, "取消")
