from django.db import models
from mymodule.myenums import TradeCode, CoinType, TradeStatus

# ユーザ情報
class UserInfo(models.Model):
    userId = models.CharField(verbose_name="ユーザID", max_length=50)
    exchangeCode = models.CharField(
        verbose_name="取引所コード", max_length=3, choices=[e.value for e in TradeCode]
    )


# ユーザ残高管理
class UserBalanceManage(models.Model):
    balanceMgtNo = models.IntegerField(primary_key=True, verbose_name="残高管理番号")
    userInfo = models.ForeignKey(
        UserInfo, verbose_name="ユーザ情報", on_delete=models.PROTECT
    )
    registerDate = models.CharField(verbose_name="登録日", max_length=8)
    registerTime = models.CharField(verbose_name="登録時刻", max_length=12)


# ユーザ残高
class UserBalance(models.Model):
    UserBalanceManage = models.ForeignKey(
        UserBalanceManage, verbose_name="ユーザ残高情報", on_delete=models.PROTECT
    )
    coinType = models.CharField(
        verbose_name="通貨種別", max_length=3, choices=[e.value for e in CoinType]
    )
    amount = models.FloatField(verbose_name="単位数")
    unitPrice = models.FloatField(verbose_name="終値")


# 取引管理
class TradeManage(models.Model):
    tradeMgtNo = models.IntegerField(primary_key=True, verbose_name="取引管理番号")
    userInfo = models.ForeignKey(
        UserInfo, verbose_name="ユーザ情報", on_delete=models.PROTECT
    )
    coinType = models.CharField(
        verbose_name="通貨種別", max_length=3, choices=[e.value for e in CoinType]
    )
    tradeStatus = models.CharField(
        verbose_name="取引ステータス", max_length=3, choices=[e.value for e in TradeStatus]
    )
    orderDate = models.CharField(verbose_name="注文日", max_length=8)
    orderTime = models.CharField(verbose_name="注文時刻", max_length=12)
    finishDate = models.CharField(verbose_name="完了日", max_length=8)
    finishTime = models.CharField(verbose_name="完了時刻", max_length=12)
    amount = models.FloatField(verbose_name="単位数")
    orderPrice = models.FloatField(verbose_name="注文価格")
    contractPrice = models.FloatField(verbose_name="約定価格")
