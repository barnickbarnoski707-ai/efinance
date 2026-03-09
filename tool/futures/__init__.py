# 该文件包含 tool/futures/__init__.py 模块的相关功能实现，提供给外部调用。
from .getter import (
    get_deal_detail,
    get_futures_base_info,
    get_quote_history,
    get_realtime_quotes,
)

__all__ = [
    "get_futures_base_info",
    "get_quote_history",
    "get_realtime_quotes",
    "get_deal_detail",
]
