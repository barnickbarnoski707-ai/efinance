# EFinance 工具接口使用文档

本文档详细介绍了通过 `main.py` 暴露出来的所有金融数据获取接口及其参数说明。

> **引入方式**
> 在同一目录下，您可以通过以下方式引入本工具：
> ```python
> from main import api
> ```
> `api` 对象内置了四大模块：`api.stock`（股票）、`api.fund`（基金）、`api.bond`（债券）、`api.futures`（期货）。

---

## 1. 股票模块 (`api.stock`)

### 1.1 `get_realtime_quotes(fs: Union[str, List[str]] = None, **kwargs) -> pd.DataFrame`
获取某个市场的最新实时行情。
- **参数**:
  - `fs`: 市场简称或列表，如 `'沪A'`、`'深A'`、`'美股'`、`'港股'` 等。默认为 `None`（返回沪深京 A 股行情）。
- **返回**: 包含代码、名称、涨跌幅、最新价等维度的 `DataFrame`。

### 1.2 `get_quote_history(stock_codes: Union[str, List[str]], beg: str = "19000101", end: str = "20500101", klt: int = 101, fqt: int = 1, **kwargs) -> Union[pd.DataFrame, Dict[str, pd.DataFrame]]`
获取单只或多只股票的历史 K 线数据。
- **参数**:
  - `stock_codes`: 股票代码字符串，或代码组成的列表。
  - `beg`: 开始日期，格式 `YYYYMMDD`。
  - `end`: 结束日期，格式 `YYYYMMDD`。
  - `klt`: 时间粒度。`1`=分钟, `5`=5分钟, `101`=日线, `102`=周线。
  - `fqt`: 复权方式。`0`=不复权, `1`=前复权, `2`=后复权。

### 1.3 `get_base_info(stock_codes: Union[str, List[str]]) -> Union[pd.Series, pd.DataFrame]`
获取股票的基本面信息（市盈率、市净率、总市值、净利润等）。

### 1.4 `get_latest_quote(stock_codes: Union[str, List[str]], **kwargs) -> pd.DataFrame`
获取指定股票（支持美股、港股）的实时行情快照。

### 1.5 `get_history_bill(stock_code: str) -> pd.DataFrame`
获取历史单子（主力、大单、中单、小单）的资金净流入流出日线数据。

### 1.6 `get_today_bill(stock_code: str) -> pd.DataFrame`
获取当天盘中各级别单子资金的分钟级流入流出情况。

### 1.7 `get_top10_stock_holder_info(stock_code: str, top: int = 4) -> pd.DataFrame`
获取个股前十大流通股东数据。

### 1.8 `get_all_report_dates() -> pd.DataFrame`
获取沪深市场的全部股票报告期信息（例如各种季报的名称和日期）。

### 1.9 `get_all_company_performance(date: str = None) -> pd.DataFrame`
获取全市场公司指定季度的业绩表现（如 2021-06-30）。

### 1.10 `get_latest_holder_number(date: str = None) -> pd.DataFrame`
获取沪深A股市场最新公开的或指定报告期的股东数目变化情况。

### 1.11 `get_daily_billboard(start_date: str = None, end_date: str = None) -> pd.DataFrame`
获取指定日期区间的龙虎榜详情数据（席位买卖净额等）。

### 1.12 `get_members(index_code: str) -> pd.DataFrame`
获取某个指数（例如 `000300` 沪深300）的成分股及其权重信息。

### 1.13 `get_latest_ipo_info() -> pd.DataFrame`
获取企业 IPO 的审核状态、保荐机构及基本信息。

### 1.14 `get_quote_snapshot(stock_code: str) -> pd.Series`
获取沪深市场股票最新五档盘口行情的快照数据。

### 1.15 `get_deal_detail(stock_code: str, max_count: int = 1000000, **kwargs) -> pd.DataFrame`
获取股票最新交易日逐笔成交明细。

### 1.16 `get_belong_board(stock_code: str) -> pd.DataFrame`
查询某只股票所属的板块信息（如行业、概念板块、地区等）。

---

## 2. 基金模块 (`api.fund`)

### 2.1 `get_realtime_increase_rate(fund_codes: Union[str, List[str]]) -> pd.DataFrame`
获取单只或多只基金实时盘中估算涨跌幅。

### 2.2 `get_quote_history(fund_code: str, pz: int = 40000) -> pd.DataFrame`
获取单只基金的历史净值（单位净值、累计净值）信息。

### 2.3 `get_quote_history_multi(fund_codes: List[str], pz: int = 40000, **kwargs) -> Dict[str, pd.DataFrame]`
获取多只基金的历史净值信息。

### 2.4 `get_base_info(fund_codes: Union[str, List[str]]) -> Union[pd.Series, pd.DataFrame]`
获取基金公司、成立日期、简介等基本信息。

### 2.5 `get_fund_codes(ft: str = None) -> pd.DataFrame`
获取天天基金网公开的全部公募基金名单代码与简称。
- **参数**:
  - `ft`: `gp`(股票), `hh`(混合), `zq`(债券) 等。

### 2.6 `get_fund_manager(ft: str) -> pd.DataFrame`
获取指定基金代码的基金经理任职信息。

### 2.7 `get_invest_position(fund_code: str, dates: Union[str, List[str]] = None) -> pd.DataFrame`
获取基金公开重仓股持仓比例。

### 2.8 `get_industry_distribution(fund_code: str, dates: Union[str, List[str]] = None) -> pd.DataFrame`
获取基金持仓的行业分布比例（如制造业、金融业占比）。

### 2.9 `get_types_percentage(fund_code: str, dates: Union[List[str], str, None] = None) -> pd.DataFrame`
获取基金的大类资产配置比例（股票、债券、现金比重）。

### 2.10 `get_period_change(fund_code: str) -> pd.DataFrame`
获取基金阶段涨跌幅度（如近一周、近一月、近一年）。

### 2.11 `get_public_dates(fund_code: str) -> List[str]`
获取某只基金历史上更新持仓情况的公开报告日期列表。

### 2.12 `get_pdf_reports(fund_code: str, max_count: int = 12, save_dir: str = "pdf") -> None`
下载指定基金的最新公开 PDF 报告（默认保存到同级目录下的 `pdf/` 文件夹中）。

---

## 3. 债券模块 (`api.bond`)

### 3.1 `get_realtime_quotes() -> pd.DataFrame`
获取全市场可转债实时行情。

### 3.2 `get_all_base_info() -> pd.DataFrame`
获取所有可转债的基础信息。返回数据包括：正股代码、债券评级、申购日期、发行规模、到期日期等。

### 3.3 `get_base_info(bond_code: str) -> pd.Series`
获取单个可转债的基础信息快照。

### 3.4 `get_quote_history(bond_code: str, beg: str = "19000101", end: str = "20500101", klt: int = 101, fqt: int = 1, **kwargs) -> pd.DataFrame`
获取单个可转债历史 K 线数据（参数格式同股票历史 K 线）。

### 3.5 `get_history_bill(bond_code: str) -> pd.DataFrame`
获取可转债单只债券的历史资金净流入流出记录。

### 3.6 `get_today_bill(bond_code: str) -> pd.DataFrame`
获取可转债单只债券今天的分钟级资金净流入流出。

### 3.7 `get_deal_detail(bond_code: str, max_count: int = 1000000, **kwargs) -> pd.DataFrame`
获取可转债最新交易日逐笔成交明细。

---

## 4. 期货模块 (`api.futures`)

### 4.1 `get_realtime_quotes() -> pd.DataFrame`
获取国内四大期货交易所（郑商所、大商所、上期所、中金所等）的实时行情总体情况。

### 4.2 `get_futures_base_info() -> pd.DataFrame`
获取各大交易所期货基础信息。其中包含极为关键的 `行情ID`，这是调用期货 K 线的必要参数。

### 4.3 `get_quote_history(quote_ids: Union[str, List[str]], beg: str = "19000101", end: str = "20500101", klt: int = 101, fqt: int = 1, **kwargs) -> pd.DataFrame`
获取期货历史 K 线数据。
- **参数**:
  - `quote_ids`: 从 `get_futures_base_info` 取得的期货 `行情ID` 字符串或列表。

### 4.4 `get_deal_detail(quote_id: str, max_count: int = 1000000) -> pd.DataFrame`
获取期货最新交易日的逐笔成交明细。需要提供 `行情ID`。
