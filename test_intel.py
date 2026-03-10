from tool.stock import getter as stock
from tool.utils import core as utils
import pandas as pd

# 设置显示选项，防止输出被截断
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print("=== 尝试搜索 英特尔 的行情 ID ===")
try:
    quote = utils.search_quote("英特尔", count=1)
    if quote:
        print(f"搜索结果: 代码={quote.code}, 名称={quote.name}, 市场类型={quote.market_type}")
    else:
        print("未搜索到 英特尔")
except Exception as e:
    import traceback
    traceback.print_exc()

print("\n=== 尝试获取 英特尔 (INTC) 的实时行情快照 ===")
try:
    # 东方财富美股的行情通常可以通过 get_latest_quote 获取，或者根据 code 模糊搜索
    quotes = stock.get_latest_quote("INTC")
    print(quotes)
except Exception as e:
    import traceback
    traceback.print_exc()

print("\n=== 尝试获取 英特尔 (INTC) 的基础信息 ===")
try:
    info = stock.get_base_info("INTC")
    print(info)
except Exception as e:
    import traceback
    traceback.print_exc()
