from django.conf import settings
from alipay import AliPay
from alipay.utils import AliPayConfig
from datetime import datetime


class AliPaySDK(AliPay):
    """支付宝接口sdk工具类"""
    def __init__(self, config=None):
        """
        参考文档：https://github.com/fzlee/alipay/blob/master/docs/init.zh-hans.md
        """
        if config is None:
            self.config = settings.ALIPAY
        else:
            self.config = config

        # 应用私钥
        app_private_key_string = open(self.config["app_private_key_path"]).read()
        # 支付宝公钥
        alipay_public_key_string = open(self.config["alipay_public_key_path"]).read()

        super().__init__(
            appid=self.config["appid"],
            app_notify_url=self.config["notify_url"],  # 默认全局回调 url
            app_private_key_string=app_private_key_string,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            alipay_public_key_string=alipay_public_key_string,
            sign_type=self.config["sign_type"],  # RSA 或者 RSA2
            debug=self.config["debug"],  # 默认 False，沙箱模式下必须设置为True
            verbose=self.config["verbose"],  # 输出调试数据
            config=AliPayConfig(timeout=self.config["timeout"])  # 可选，请求超时时间，单位：秒
        )

    def page_pay(self, out_trade_no, total_amount, subject):
        """
        生成支付链接
        @parmas out_trade_no: 商户订单号
        @parmas total_amount: 订单金额
        @parmas subject: 订单标题
        @return 支付链接
        """
        order_string = self.client_api(
            "alipay.trade.page.pay",
            biz_content={
                "out_trade_no": out_trade_no,  # 订单号
                "total_amount": float(total_amount),  # 订单金额
                "subject": subject,   # 订单标题
                "product_code": "FAST_INSTANT_TRADE_PAY",
            },
            return_url = self.config["return_url"],  # 可选，同步回调地址，必须填写客户端的路径
            notify_url = self.config["notify_url"]  # 可选，不填则使用采用全局默认notify_url，必须填写服务端的路径
        )

        return f"{self.config['gateway']}?{order_string}"

    def check_sign(self, data):
        """
        验证返回的支付结果中的签证信息
        @params data: 支付平台返回的支付结果，字典格式
        """
        signature = data.pop("sign")
        success = self.verify(data, signature)
        return success

    def query(self, out_trade_no):
        """
        根据订单号查询订单状态
        @params out_trade_no: 订单号
        """
        return self.server_api(
            "alipay.trade.query",
            biz_content={
                "out_trade_no": out_trade_no
            }
        )

    def refund(self, out_trade_no, refund_amount):
        """
        原路退款
        @params out_trade_no: 退款的订单号
        @params refund_amount: 退款的订单金额
        """
        self.server_api(
            "alipay.trade.refund",
            biz_content={
                "out_trade_no": out_trade_no,
                "refund_amount": refund_amount
            }
        )

    def transfer(self, account, amount):
        """
        转账给个人
        @params account: 收款人的支付宝账号
        @params amount: 转账金额
        """
        return self.server_api(
            "alipay.fund.trans.toaccount.transfer",
            biz_content={
                "out_biz_no": datetime.now().strftime("%Y%m%d%H%M%S"),
                "payee_type": "ALIPAY_LOGONID",
                # ALIPAY_USERID: 支付宝账号对应的支付宝唯一用户号。以2088开头的16位纯数字组成。
                # # ALIPAY_LOGONID: 支付宝登录号，支持邮箱和手机号格式。
                "payee_account": account,  # 账号
                "amount": amount  # 金额
            }
        )

    def query_transfer(self, trans_time):
        """
        查询转账记录
        @params trans_time: 转账时间[datetime对象]
        """
        return self.server_api(
            "alipay.fund.trans.order.query",
            biz_content={
                "out_biz_no": trans_time.strftime("%Y%m%d%H%M%S"),
            }
        )