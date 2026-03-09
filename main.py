# 该文件是项目的统一入口，代理了 tool 包下的各个子模块，供外部调用
# 您可以通过导入此文件来使用股票、基金、债券、期货等行情获取功能

from tool import stock
from tool import fund
from tool import bond
from tool import futures

__all__ = ['stock', 'fund', 'bond', 'futures']

# 以下是一些简单的调用示例，如果作为模块导入时不会执行
if __name__ == "__main__":
    print("=== 测试调用股票模块: 获取贵州茅台的实时行情 ===")
    try:
        quote = stock.get_realtime_quotes()
        print(quote.head())
    except Exception as e:
        print(f"调用股票模块时发生错误: {e}")

    print("\n=== 测试调用基金模块: 获取某基金的实时估值 ===")
    try:
        fund_quote = fund.get_realtime_increase_rate('161725')
        print(fund_quote)
    except Exception as e:
        print(f"调用基金模块时发生错误: {e}")
