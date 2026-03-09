# 该文件包含 tool/config/__init__.py 模块的相关功能实现，提供给外部调用。
from pathlib import Path

HERE = Path(__file__).parent
# 数据缓存文件存储目录
DATA_DIR = HERE / "../data"
# 创建数据缓存文件目录
DATA_DIR.mkdir(parents=True, exist_ok=True)
# 搜索词缓存位置
SEARCH_RESULT_CACHE_PATH = str(DATA_DIR / "search-cache.json")

MAX_CONNECTIONS = 50
