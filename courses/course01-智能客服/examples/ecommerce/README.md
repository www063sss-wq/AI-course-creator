# 电商智能客服示例

完整的电商行业智能客服示例，包含售前咨询、订单查询、售后服务等核心场景。

## 📁 目录结构

```
ecommerce/
├── intents/                    # 意图定义
│   └── ecommerce_intents.json  # 8 个核心意图，125 个训练语料
├── dialog_flows/               # 对话流程
│   ├── logistics_flow.json     # 物流查询对话流程
│   └── return_flow.json        # 退货申请对话流程
├── faq/                        # FAQ 知识库
│   └── ecommerce_faq.csv       # 90 个电商 FAQ
├── integrations/               # API 集成示例
│   ├── order_api.py           # 订单 API 集成
│   └── logistics_api.py       # 物流 API 集成
├── webchat/                    # Web 聊天窗口
│   ├── app.py                 # Flask 应用
│   └── templates/
│       └── chat.html          # 聊天页面
├── configs/                    # 配置文件模板
│   ├── baidu_config.json      # 百度智能云配置
│   ├── aliyun_config.json     # 阿里云配置
│   └── tencent_config.json    # 腾讯云配置
├── data/                       # 演示数据
│   └── test_orders.json       # 测试订单数据
├── .env.example               # 环境变量示例
├── requirements.txt           # Python 依赖
└── README.md                  # 本文件
```

## 🚀 快速开始

### 1. 环境准备

```bash
# 安装 Python 依赖
pip install -r requirements.txt

# 复制环境变量配置
cp .env.example .env

# 编辑.env 文件，填入你的 API 密钥
```

### 2. 启动 Web 聊天演示

```bash
cd webchat
python app.py
```

访问：http://localhost:5000

### 3. 测试 API 集成

```bash
# 测试订单 API
python integrations/order_api.py

# 测试物流 API
python integrations/logistics_api.py
```

## 📊 核心功能

### 意图识别 (8 个核心意图)

| 意图名称 | 描述 | 类别 | 训练语料 |
|---------|------|------|---------|
| product_consult | 产品功能咨询 | 售前咨询 | 20 条 |
| price_inquiry | 价格咨询 | 售前咨询 | 15 条 |
| stock_check | 库存查询 | 售前咨询 | 10 条 |
| order_logistics_query | 物流状态查询 | 订单查询 | 20 条 |
| order_status_query | 订单状态查询 | 订单查询 | 15 条 |
| after_sale_return | 退货申请 | 售后服务 | 15 条 |
| after_sale_exchange | 换货申请 | 售后服务 | 10 条 |
| complaint | 投诉建议 | 售后服务 | 20 条 |

### 对话流程 (2 个核心流程)

1. **物流查询对话流程** (`logistics_flow.json`)
   - 自动识别订单号
   - 槽位填充与验证
   - 实时物流轨迹查询
   - 满意度评价

2. **退货申请对话流程** (`return_flow.json`)
   - 订单资格验证
   - 退货原因收集
   - 退货方式选择
   - 自动生成退货单

### FAQ 知识库 (90 个 FAQ)

覆盖 4 大类别：
- 售前咨询：30 个 FAQ
- 订单查询：25 个 FAQ
- 售后服务：25 个 FAQ
- 通用问题：10 个 FAQ

## 🔧 配置说明

### 百度智能云配置

编辑 `configs/baidu_config.json`:

```json
{
  "bot_config": {
    "app_id": "YOUR_APP_ID",
    "api_key": "YOUR_API_KEY",
    "secret_key": "YOUR_SECRET_KEY",
    "unit_id": "YOUR_UNIT_ID"
  }
}
```

### 阿里云配置

编辑 `configs/aliyun_config.json`:

```json
{
  "bot_config": {
    "access_key_id": "YOUR_ACCESS_KEY_ID",
    "access_key_secret": "YOUR_ACCESS_KEY_SECRET",
    "instance_id": "YOUR_INSTANCE_ID"
  }
}
```

### 腾讯云配置

编辑 `configs/tencent_config.json`:

```json
{
  "bot_config": {
    "secret_id": "YOUR_SECRET_ID",
    "secret_key": "YOUR_SECRET_KEY",
    "bot_id": "YOUR_BOT_ID"
  }
}
```

## 📝 使用示例

### 1. 意图识别测试

```python
import json

# 加载意图定义
with open('intents/ecommerce_intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

# 查看某个意图
for intent in intents['intents']:
    if intent['intent_name'] == 'product_consult':
        print(f"意图：{intent['description']}")
        print(f"训练语料数量：{intent['training_data_count']}")
        print(f"示例问题：{intent['example_questions'][:5]}")
```

### 2. FAQ 匹配测试

```python
import csv

# 加载 FAQ
with open('faq/ecommerce_faq.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if '价格' in row['question']:
            print(f"问题：{row['question']}")
            print(f"答案：{row['answer']}")
```

### 3. 对话流程测试

```python
import json

# 加载物流查询流程
with open('dialog_flows/logistics_flow.json', 'r', encoding='utf-8') as f:
    flow = json.load(f)

print(f"流程名称：{flow['flow_name']}")
print(f"节点数量：{len(flow['nodes'])}")
print(f"触发意图：{flow['trigger_intent']}")
```

## 🎯 教学使用场景

### 场景 1: 课堂演示

1. 启动 Web 聊天应用
2. 演示用户提问"产品怎么用？"
3. 展示意图识别结果
4. 展示 FAQ 匹配过程
5. 展示回复生成

### 场景 2: 学员实验

1. 学员修改意图定义文件
2. 添加新的训练语料
3. 测试意图识别效果
4. 对比修改前后差异

### 场景 3: 对话流程设计

1. 分析现有对话流程
2. 设计新的对话节点
3. 配置槽位填充规则
4. 测试多轮对话效果

### 场景 4: API 集成实战

1. 学习 API 客户端编写
2. 集成真实订单系统
3. 集成物流查询 API
4. 处理异常情况

## ✅ 审查清单

- [x] 意图定义完整（8 个意图，125 条语料）
- [x] 对话流程配置正确（2 个流程）
- [x] FAQ 知识库完整（90 个 FAQ）
- [x] API 集成示例可运行
- [x] Web 聊天窗口可访问
- [x] 配置文件模板完整
- [x] 演示数据真实可用
- [x] 文档说明清晰

## 📚 相关文档

- [开发任务说明](../开发任务.json)
- [交付说明](../交付说明.md)
- [课程主页](../../INDEX.md)

## 💡 扩展建议

1. **添加更多意图**: 如产品推荐、投诉处理等
2. **完善对话流程**: 添加换货、维修等流程
3. **集成真实 API**: 对接真实电商系统
4. **增加多轮对话**: 实现更复杂的对话逻辑
5. **添加数据分析**: 统计用户问题、满意度等

## 📞 技术支持

如有问题，请联系课程技术支持或查看相关文档。
