# 香港疫情数据可视化大屏

一个用于可视化香港疫情数据的交互式大屏项目，包含数据处理、分析和可视化功能。

## 项目结构

```
dashboard_epidemic/
├── view_data.py          # 查看数据文件
├── analyze_data.py       # 分析疫情数据
├── plot_data.py          # 绘制趋势图
├── export_data.py        # 导出数据供大屏使用
├── serve_dashboard.py    # 启动本地 HTTP 服务器
├── index.html            # 可视化大屏页面（支持日期选择）
├── bouncing_ball.html    # 红色小球三角形反弹动画
├── 香港各区疫情数据_20250322.xlsx  # 原始数据文件
├── dashboard_data.json   # 处理后的数据（运行 export_data.py 生成）
└── epidemic_trends.png   # 趋势图（运行 plot_data.py 生成）
```

## 功能模块

### 1. view_data.py - 数据查看
读取并显示 Excel 数据文件的前 5 行，快速预览数据结构。

```bash
python view_data.py
```

### 2. analyze_data.py - 数据分析
分析全港每日新增与累计确诊数据，以及各地区最新数据。

```bash
python analyze_data.py
```

### 3. plot_data.py - 图表绘制
绘制香港疫情趋势折线图（双轴显示每日新增和累计确诊），保存为 `epidemic_trends.png`。

```bash
python plot_data.py
```

### 4. export_data.py - 数据导出
处理原始数据并导出为 JSON 格式，供可视化大屏使用，生成 `dashboard_data.json`。包含所有日期的数据。

```bash
python export_data.py
```

### 5. serve_dashboard.py - 启动服务器
启动本地 HTTP 服务器，在浏览器中自动打开可视化大屏。

```bash
python serve_dashboard.py
```

### 6. index.html - 可视化大屏（支持日期选择）
一个交互式的疫情数据监控大屏，使用 ECharts 图表库展示：
- **日期选择器** - 可选择任意日期查看历史数据
- 累计确诊、今日新增、累计康复、累计死亡 统计卡片
- 疫情趋势图（新增与累计，显示到所选日期）
- 各地区确诊分布（横向柱状图）
- 病例增长率变化图
- 风险等级分布图（饼图）

### 7. bouncing_ball.html - 小球动画
一个有趣的红色小球在三角形区域内反弹的动画页面，带有交互控制按钮。

## 环境配置

### 安装依赖

```bash
# 创建虚拟环境（如果尚未创建）
python3 -m venv .venv

# 激活虚拟环境
source .venv/bin/activate

# 安装依赖
pip install pandas matplotlib openpyxl
```

### 依赖说明

- `pandas` - 数据处理与分析
- `matplotlib` - 图表绘制
- `openpyxl` - 读取 Excel 文件
- `ECharts` - 前端可视化（通过 CDN 加载，无需安装）

## 使用流程

### 快速开始（推荐）

```bash
# 1. 导出数据
python export_data.py

# 2. 启动服务器（会自动在浏览器打开）
python serve_dashboard.py
```

### 完整流程

1. **准备数据**：确保 `香港各区疫情数据_20250322.xlsx` 数据文件在项目根目录

2. **处理数据**：
```bash
# 先查看数据
python view_data.py

# 分析数据
python analyze_data.py

# 导出数据供大屏使用
python export_data.py
```

3. **查看可视化大屏**：
   - **方式一（推荐）**：启动服务器 `python serve_dashboard.py`
   - **方式二**：使用浏览器直接打开 `index.html` 文件
   - 确保 `dashboard_data.json` 文件已生成（通过运行 `export_data.py`）

4. **查看小球动画**：
   - 直接在浏览器打开 `bouncing_ball.html`
   - 或通过服务器访问 `http://127.0.0.1:8765/bouncing_ball.html`

## 数据格式

原始数据 Excel 文件应包含以下列：
- 报告日期
- 地区名称
- 新增确诊
- 累计确诊
- 新增死亡
- 新增康复
- 风险等级

## 注意事项

- 项目使用 Python 3.x 开发
- 建议使用虚拟环境管理依赖
- 可视化大屏需要网络连接以加载 ECharts CDN
- 首次运行 `plot_data.py` 时，Matplotlib 会构建字体缓存，可能需要一些时间
- serve_dashboard.py 默认使用端口 8765，如遇端口冲突可修改代码中的 PORT 变量
