# 该文件是项目的统一入口，封装了股票、基金、债券、期货等所有数据抓取功能。
from typing import Union, List, Dict
import pandas as pd

from tool.stock import getter as stock_getter
from tool.fund import getter as fund_getter
from tool.bond import getter as bond_getter
from tool.futures import getter as futures_getter


class StockAPI:
    """股票相关数据接口"""

    @staticmethod
    def get_realtime_quotes(fs: Union[str, List[str]] = None, **kwargs) -> pd.DataFrame:
        """获取沪深A股/港股/美股等市场的实时行情信息。"""
        return stock_getter.get_realtime_quotes(fs=fs, **kwargs)

    @staticmethod
    def get_quote_history(stock_codes: Union[str, List[str]], beg: str = "19000101", end: str = "20500101", klt: int = 101, fqt: int = 1, **kwargs) -> Union[pd.DataFrame, Dict[str, pd.DataFrame]]:
        """获取个股历史 K 线数据。"""
        return stock_getter.get_quote_history(stock_codes=stock_codes, beg=beg, end=end, klt=klt, fqt=fqt, **kwargs)

    @staticmethod
    def get_base_info(stock_codes: Union[str, List[str]]) -> Union[pd.Series, pd.DataFrame]:
        """获取单只或多只股票的基本面信息。"""
        return stock_getter.get_base_info(stock_codes=stock_codes)

    @staticmethod
    def get_latest_quote(stock_codes: Union[str, List[str]], **kwargs) -> pd.DataFrame:
        """获取指定股票代码的实时快照。"""
        return stock_getter.get_latest_quote(stock_codes=stock_codes, **kwargs)

    @staticmethod
    def get_history_bill(stock_code: str) -> pd.DataFrame:
        """获取单只股票历史单子（主力、大单、小单）净流入流出数据。"""
        return stock_getter.get_history_bill(stock_code=stock_code)

    @staticmethod
    def get_today_bill(stock_code: str) -> pd.DataFrame:
        """获取个股当天盘中分钟级的资金净流入流出数据。"""
        return stock_getter.get_today_bill(stock_code=stock_code)

    @staticmethod
    def get_top10_stock_holder_info(stock_code: str, top: int = 4) -> pd.DataFrame:
        """获取股票前十大流通股东数据。"""
        return stock_getter.get_top10_stock_holder_info(stock_code=stock_code, top=top)

    @staticmethod
    def get_all_report_dates() -> pd.DataFrame:
        """获取沪深市场的全部股票报告期信息。"""
        return stock_getter.get_all_report_dates()

    @staticmethod
    def get_all_company_performance(date: str = None) -> pd.DataFrame:
        """获取全市场公司指定季度的业绩表现（如 2021-06-30）。"""
        return stock_getter.get_all_company_performance(date=date)

    @staticmethod
    def get_latest_holder_number(date: str = None) -> pd.DataFrame:
        """获取沪深A股市场最新公开的或指定报告期的股东数目变化情况。"""
        return stock_getter.get_latest_holder_number(date=date)

    @staticmethod
    def get_daily_billboard(start_date: str = None, end_date: str = None) -> pd.DataFrame:
        """获取指定日期区间的龙虎榜详情数据。"""
        return stock_getter.get_daily_billboard(start_date=start_date, end_date=end_date)

    @staticmethod
    def get_members(index_code: str) -> pd.DataFrame:
        """获取指数（如 '000300'）成分股信息。"""
        return stock_getter.get_members(index_code=index_code)

    @staticmethod
    def get_latest_ipo_info() -> pd.DataFrame:
        """获取企业 IPO 审核状态。"""
        return stock_getter.get_latest_ipo_info()

    @staticmethod
    def get_quote_snapshot(stock_code: str) -> pd.Series:
        """获取沪深市场股票最新五档盘口行情快照。"""
        return stock_getter.get_quote_snapshot(stock_code=stock_code)

    @staticmethod
    def get_deal_detail(stock_code: str, max_count: int = 1000000, **kwargs) -> pd.DataFrame:
        """获取股票最新交易日逐笔成交明细。"""
        return stock_getter.get_deal_detail(stock_code=stock_code, max_count=max_count, **kwargs)

    @staticmethod
    def get_belong_board(stock_code: str) -> pd.DataFrame:
        """获取股票所属板块信息。"""
        return stock_getter.get_belong_board(stock_code=stock_code)


class FundAPI:
    """基金相关数据接口"""

    @staticmethod
    def get_realtime_increase_rate(fund_codes: Union[str, List[str]]) -> pd.DataFrame:
        """获取单只或多只基金实时估算涨跌幅。"""
        return fund_getter.get_realtime_increase_rate(fund_codes=fund_codes)

    @staticmethod
    def get_quote_history(fund_code: str, pz: int = 40000) -> pd.DataFrame:
        """获取单只基金的历史净值信息。"""
        return fund_getter.get_quote_history(fund_code=fund_code, pz=pz)

    @staticmethod
    def get_quote_history_multi(fund_codes: List[str], pz: int = 40000, **kwargs) -> Dict[str, pd.DataFrame]:
        """获取多只基金的历史净值信息。"""
        return fund_getter.get_quote_history_multi(fund_codes=fund_codes, pz=pz, **kwargs)

    @staticmethod
    def get_base_info(fund_codes: Union[str, List[str]]) -> Union[pd.Series, pd.DataFrame]:
        """获取基金公司、成立日期、简介等基本信息。"""
        return fund_getter.get_base_info(fund_codes=fund_codes)

    @staticmethod
    def get_fund_codes(ft: str = None) -> pd.DataFrame:
        """获取天天基金网公开的全部公募基金名单。可选 'gp'(股票), 'hh'(混合) 等。"""
        return fund_getter.get_fund_codes(ft=ft)

    @staticmethod
    def get_fund_manager(ft: str) -> pd.DataFrame:
        """获取基金经理任职信息。"""
        return fund_getter.get_fund_manager(ft=ft)

    @staticmethod
    def get_invest_position(fund_code: str, dates: Union[str, List[str]] = None) -> pd.DataFrame:
        """获取基金公开重仓股持仓比例。"""
        return fund_getter.get_invest_position(fund_code=fund_code, dates=dates)

    @staticmethod
    def get_industry_distribution(fund_code: str, dates: Union[str, List[str]] = None) -> pd.DataFrame:
        """获取基金持仓的行业分布情况。"""
        return fund_getter.get_industry_distribution(fund_code=fund_code, dates=dates)

    @staticmethod
    def get_types_percentage(fund_code: str, dates: Union[List[str], str, None] = None) -> pd.DataFrame:
        """获取基金资产配置类型（股票、债券、现金）比例。"""
        return fund_getter.get_types_percentage(fund_code=fund_code, dates=dates)

    @staticmethod
    def get_period_change(fund_code: str) -> pd.DataFrame:
        """获取基金阶段涨跌幅度（如近一周、近一月、近一年）。"""
        return fund_getter.get_period_change(fund_code=fund_code)

    @staticmethod
    def get_public_dates(fund_code: str) -> List[str]:
        """获取历史上更新持仓情况的公开日期列表。"""
        return fund_getter.get_public_dates(fund_code=fund_code)

    @staticmethod
    def get_pdf_reports(fund_code: str, max_count: int = 12, save_dir: str = "pdf") -> None:
        """下载指定基金的最新 PDF 报告。"""
        return fund_getter.get_pdf_reports(fund_code=fund_code, max_count=max_count, save_dir=save_dir)


class BondAPI:
    """债券（可转债）相关数据接口"""

    @staticmethod
    def get_realtime_quotes() -> pd.DataFrame:
        """获取可转债市场实时行情。"""
        return bond_getter.get_realtime_quotes()

    @staticmethod
    def get_all_base_info() -> pd.DataFrame:
        """获取所有可转债的基础信息（评级、规模、正股代码等）。"""
        return bond_getter.get_all_base_info()

    @staticmethod
    def get_base_info(bond_code: str) -> pd.Series:
        """获取单个可转债的基础信息。"""
        return bond_getter.get_base_info(bond_code=bond_code)

    @staticmethod
    def get_quote_history(bond_code: str, beg: str = "19000101", end: str = "20500101", klt: int = 101, fqt: int = 1, **kwargs) -> pd.DataFrame:
        """获取可转债历史 K 线数据。"""
        return bond_getter.get_quote_history(bond_code=bond_code, beg=beg, end=end, klt=klt, fqt=fqt, **kwargs)

    @staticmethod
    def get_history_bill(bond_code: str) -> pd.DataFrame:
        """获取可转债单只债券的历史资金净流入流出。"""
        return bond_getter.get_history_bill(bond_code=bond_code)

    @staticmethod
    def get_today_bill(bond_code: str) -> pd.DataFrame:
        """获取可转债单只债券今天的分钟级资金净流入流出。"""
        return bond_getter.get_today_bill(bond_code=bond_code)

    @staticmethod
    def get_deal_detail(bond_code: str, max_count: int = 1000000, **kwargs) -> pd.DataFrame:
        """获取可转债最新交易日逐笔成交明细。"""
        return bond_getter.get_deal_detail(bond_code=bond_code, max_count=max_count, **kwargs)


class FuturesAPI:
    """期货相关数据接口"""

    @staticmethod
    def get_realtime_quotes() -> pd.DataFrame:
        """获取期货市场最新行情总体情况。"""
        return futures_getter.get_realtime_quotes()

    @staticmethod
    def get_futures_base_info() -> pd.DataFrame:
        """获取各大交易所期货基础信息。"""
        return futures_getter.get_futures_base_info()

    @staticmethod
    def get_quote_history(quote_ids: Union[str, List[str]], beg: str = "19000101", end: str = "20500101", klt: int = 101, fqt: int = 1, **kwargs) -> pd.DataFrame:
        """获取期货历史 K 线数据。"""
        return futures_getter.get_quote_history(quote_ids=quote_ids, beg=beg, end=end, klt=klt, fqt=fqt, **kwargs)

    @staticmethod
    def get_deal_detail(quote_id: str, max_count: int = 1000000) -> pd.DataFrame:
        """获取期货最新交易日逐笔成交明细。"""
        return futures_getter.get_deal_detail(quote_id=quote_id, max_count=max_count)


class EFinanceTool:
    """统一聚合网关，供调用各类金融数据。"""
    stock = StockAPI
    fund = FundAPI
    bond = BondAPI
    futures = FuturesAPI

# 实例化单例供外部直接导入使用
api = EFinanceTool()

if __name__ == "__main__":
    print("=== 测试统一封装接口 ===")
    try:
        print(api.stock.get_latest_quote("INTC"))
    except Exception as e:
        print("调用失败: ", e)
