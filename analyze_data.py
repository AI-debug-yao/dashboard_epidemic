import pandas as pd

def analyze_epidemic_data(file_path):
    """
    分析疫情数据：计算全港每日新增与累计确诊数据
    """
    try:
        # 读取 Excel 文件
        df = pd.read_excel(file_path)
        
        # 确保日期格式正确
        df['报告日期'] = pd.to_datetime(df['报告日期'])
        
        # 1. 计算全港每日汇总数据（按日期分组）
        daily_summary = df.groupby('报告日期').agg({
            '新增确诊': 'sum',
            '累计确诊': 'sum'
        }).reset_index()
        
        # 排序
        daily_summary = daily_summary.sort_values('报告日期')
        
        print(f"成功分析文件: {file_path}")
        print("\n=== 全港每日新增与累计确诊汇总 (最后 5 天) ===")
        print(daily_summary.tail())
        
        # 2. 计算各区最近一天的累计确诊
        latest_date = df['报告日期'].max()
        district_summary = df[df['报告日期'] == latest_date][['地区名称', '新增确诊', '累计确诊']]
        
        print(f"\n=== 各地区最新数据 ({latest_date.strftime('%Y-%m-%d')}) ===")
        print(district_summary.sort_values('累计确诊', ascending=False).head())
        
        return daily_summary, district_summary
        
    except Exception as e:
        print(f"处理数据时出错: {e}")
        return None, None

if __name__ == "__main__":
    file_name = '香港各区疫情数据_20250322.xlsx'
    analyze_epidemic_data(file_name)
