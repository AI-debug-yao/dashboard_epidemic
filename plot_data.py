import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 设置中文字体（适配 macOS）
try:
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # macOS 常用中文字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
except Exception:
    pass

def plot_epidemic_trends(file_path):
    """
    绘制疫情趋势折线图
    """
    try:
        # 读取数据
        df = pd.read_excel(file_path)
        df['报告日期'] = pd.to_datetime(df['报告日期'])
        
        # 按日期汇总全港数据
        daily_summary = df.groupby('报告日期').agg({
            '新增确诊': 'sum',
            '累计确诊': 'sum'
        }).reset_index().sort_values('报告日期')
        
        # 创建画布
        fig, ax1 = plt.subplots(figsize=(12, 6))
        
        # 绘制每日新增（左轴）
        color_new = 'tab:red'
        ax1.set_xlabel('日期')
        ax1.set_ylabel('每日新增确诊', color=color_new)
        ax1.plot(daily_summary['报告日期'], daily_summary['新增确诊'], color=color_new, label='每日新增确诊')
        ax1.tick_params(axis='y', labelcolor=color_new)
        
        # 创建第二个 Y 轴绘制累计确诊（右轴）
        ax2 = ax1.twinx()
        color_total = 'tab:blue'
        ax2.set_ylabel('累计确诊', color=color_total)
        ax2.plot(daily_summary['报告日期'], daily_summary['累计确诊'], color=color_total, label='累计确诊', linestyle='--')
        ax2.tick_params(axis='y', labelcolor=color_total)
        
        # 添加标题和布局优化
        plt.title('香港疫情趋势图 (2022)')
        fig.tight_layout()
        
        # 添加图例
        lines, labels = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc='upper left')
        
        # 保存图片
        output_file = 'epidemic_trends.png'
        plt.savefig(output_file, dpi=300)
        print(f"图表已成功保存至: {output_file}")
        
        return output_file
        
    except Exception as e:
        print(f"绘制图表时出错: {e}")
        return None

if __name__ == "__main__":
    file_name = '香港各区疫情数据_20250322.xlsx'
    plot_epidemic_trends(file_name)
