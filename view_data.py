import pandas as pd

def read_epidemic_data(file_path):
    """
    读取疫情数据 Excel 文件并显示前 5 行
    """
    try:
        # 读取 Excel 文件
        df = pd.read_excel(file_path)
        
        # 打印前 5 行
        print(f"成功读取文件: {file_path}")
        print("-" * 30)
        print(df.head())
        print("-" * 30)
        
        return df
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return None

if __name__ == "__main__":
    file_name = '香港各区疫情数据_20250322.xlsx'
    read_epidemic_data(file_name)
