# 该文件包含 tool/common/__init__.py 模块的相关功能实现，提供给外部调用。
from .getter import (
    get_base_info,
    get_deal_detail,
    get_history_bill,
    get_latest_quote,
    get_quote_history,
    get_realtime_quotes_by_fs,
    get_today_bill,
)

__all__ = []
