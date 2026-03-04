#!/bin/bash

# 电商智能客服示例 - 快速启动脚本

echo "======================================"
echo "  电商智能客服示例 - 快速启动"
echo "======================================"
echo ""

# 检查 Python 版本
echo "📋 检查 Python 版本..."
python3 --version
if [ $? -ne 0 ]; then
    echo "❌ 错误：未找到 Python3，请先安装 Python3"
    exit 1
fi
echo "✅ Python 版本检查通过"
echo ""

# 检查依赖
echo "📦 检查并安装依赖..."
if [ ! -f "requirements.txt" ]; then
    echo "❌ 错误：未找到 requirements.txt"
    exit 1
fi

pip3 install -r requirements.txt -q
if [ $? -ne 0 ]; then
    echo "❌ 错误：依赖安装失败"
    exit 1
fi
echo "✅ 依赖安装完成"
echo ""

# 检查环境变量配置
echo "🔧 检查环境变量配置..."
if [ ! -f ".env" ]; then
    echo "⚠️  未找到.env 文件，从.env.example 复制..."
    cp .env.example .env
    echo "⚠️  请编辑.env 文件，填入你的 API 密钥"
    echo ""
fi
echo "✅ 环境变量配置完成"
echo ""

# 显示菜单
echo "======================================"
echo "  请选择启动模式:"
echo "======================================"
echo "1. 启动 Web 聊天演示"
echo "2. 测试订单 API 集成"
echo "3. 测试物流 API 集成"
echo "4. 查看意图定义"
echo "5. 查看 FAQ 知识库"
echo "6. 查看对话流程"
echo "7. 退出"
echo ""

read -p "请输入选项 (1-7): " choice

case $choice in
    1)
        echo ""
        echo "�� 启动 Web 聊天演示..."
        echo "访问地址：http://localhost:5000"
        echo "按 Ctrl+C 停止服务"
        echo ""
        cd webchat
        python3 app.py
        ;;
    2)
        echo ""
        echo "🔍 测试订单 API 集成..."
        echo ""
        python3 integrations/order_api.py
        ;;
    3)
        echo ""
        echo "🔍 测试物流 API 集成..."
        echo ""
        python3 integrations/logistics_api.py
        ;;
    4)
        echo ""
        echo "�� 查看意图定义..."
        echo ""
        python3 -c "
import json
with open('intents/ecommerce_intents.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(f\"意图总数：{len(data['intents'])}\")
    print(f\"训练语料总数：{sum(i['training_data_count'] for i in data['intents'])}\")
    print('')
    for intent in data['intents']:
        print(f\"• {intent['intent_name']}: {intent['description']} ({intent['training_data_count']}条)\")
"
        ;;
    5)
        echo ""
        echo "📚 查看 FAQ 知识库..."
        echo ""
        python3 -c "
import csv
categories = {}
with open('faq/ecommerce_faq.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cat = row['category']
        categories[cat] = categories.get(cat, 0) + 1
    print(f\"FAQ 总数：{sum(categories.values())}\")
    print('')
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f\"• {cat}: {count}个\")
"
        ;;
    6)
        echo ""
        echo "💬 查看对话流程..."
        echo ""
        python3 -c "
import json
flows = ['dialog_flows/logistics_flow.json', 'dialog_flows/return_flow.json']
for flow_file in flows:
    with open(flow_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(f\"流程：{data['flow_name']}\")
        print(f\"描述：{data['description']}\")
        print(f\"节点数：{len(data['nodes'])}\")
        print(f\"触发意图：{data['trigger_intent']}\")
        print('')
"
        ;;
    7)
        echo ""
        echo "👋 再见！"
        exit 0
        ;;
    *)
        echo ""
        echo "❌ 无效选项，请输入 1-7"
        exit 1
        ;;
esac
