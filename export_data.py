import pandas as pd
import json
import os

def export_data_for_dashboard(file_path):
    try:
        df = pd.read_excel(file_path)
        df['报告日期'] = pd.to_datetime(df['报告日期'])
        
        # 1. 每日趋势数据
        daily_summary = df.groupby('报告日期').agg({
            '新增确诊': 'sum',
            '累计确诊': 'sum',
            '新增死亡': 'sum',
            '新增康复': 'sum'
        }).reset_index().sort_values('报告日期')
        
        # 计算增长率 ( (今日-昨日)/昨日 )
        daily_summary['增长率'] = daily_summary['新增确诊'].pct_change().fillna(0) * 100
        
        daily_trend = {
            'dates': daily_summary['报告日期'].dt.strftime('%Y-%m-%d').tolist(),
            'new_cases': daily_summary['新增确诊'].tolist(),
            'total_cases': daily_summary['累计确诊'].tolist(),
            'growth_rates': daily_summary['增长率'].round(2).tolist(),
            'total_deaths': daily_summary['新增死亡'].cumsum().tolist(),
            'total_recovereds': daily_summary['新增康复'].cumsum().tolist()
        }
        
        # 2. 各区域所有日期的数据 (支持日期选择)
        all_district_data = {}
        for date in df['报告日期'].unique():
            date_str = date.strftime('%Y-%m-%d')
            date_df = df[df['报告日期'] == date]
            district_data = []
            for _, row in date_df.iterrows():
                district_data.append({
                    'name': row['地区名称'],
                    'value': int(row['累计确诊']),
                    'new_cases': int(row['新增确诊']),
                    'risk': row['风险等级']
                })
            all_district_data[date_str] = district_data
            
        # 3. 总体统计（所有日期）
        all_summaries = {}
        for idx, row in daily_summary.iterrows():
            date_str = row['报告日期'].strftime('%Y-%m-%d')
            all_summaries[date_str] = {
                'total_confirmed': int(row['累计确诊']),
                'total_new': int(row['新增确诊']),
                'total_death': int(daily_summary.loc[:idx, '新增死亡'].sum()),
                'total_recovered': int(daily_summary.loc[:idx, '新增康复'].sum()),
                'date': date_str
            }
        
        final_data = {
            'all_summaries': all_summaries,
            'all_district_data': all_district_data,
            'daily_trend': daily_trend,
            'available_dates': daily_summary['报告日期'].dt.strftime('%Y-%m-%d').tolist()
        }
        
        with open('dashboard_data.json', 'w', encoding='utf-8') as f:
            json.dump(final_data, f, ensure_ascii=False, indent=4)
            
        print("数据已成功导出为 dashboard_data.json")
        return True
        
    except Exception as e:
        print(f"导出数据时出错: {e}")
        return False

if __name__ == "__main__":
    export_data_for_dashboard('香港各区疫情数据_20250322.xlsx')
