"""
电商智能客服 - Web 聊天窗口演示应用
基于 Flask 的简单聊天机器人演示
"""

from flask import Flask, render_template, request, jsonify
import json
import random
from datetime import datetime

app = Flask(__name__)

# 加载意图定义
def load_intents():
    try:
        with open('../intents/ecommerce_intents.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"加载意图文件失败：{e}")
        return None

# 加载 FAQ 数据
def load_faq():
    try:
        import csv
        faq_list = []
        with open('../faq/ecommerce_faq.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                faq_list.append(row)
        return faq_list
    except Exception as e:
        print(f"加载 FAQ 文件失败：{e}")
        return []

# 简单的意图匹配
def match_intent(message: str, intents: dict) -> dict:
    """简单的关键词匹配意图"""
    message_lower = message.lower()
    
    for intent in intents.get('intents', []):
        for question in intent.get('example_questions', []):
            if question[:3] in message_lower or message_lower[:3] in question[:3]:
                return intent
    
    return None

# 简单的 FAQ 匹配
def match_faq(message: str, faq_list: list) -> dict:
    """简单的 FAQ 匹配"""
    message_lower = message.lower()
    
    for faq in faq_list:
        question = faq.get('question', '')
        similar = faq.get('similar_questions', '')
        
        # 检查问题或相似问题是否匹配
        if any(keyword in message_lower for keyword in question[:5]):
            return faq
        
        # 检查相似问题
        if similar:
            for sim_q in similar.split(';'):
                if sim_q and sim_q[:3] in message_lower:
                    return faq
    
    return None

# 生成回复
def generate_response(message: str, intents: dict, faq_list: list) -> str:
    """生成回复消息"""
    
    # 先尝试匹配 FAQ
    matched_faq = match_faq(message, faq_list)
    if matched_faq:
        return matched_faq.get('answer', '抱歉，我没有找到相关信息。')
    
    # 再尝试匹配意图
    matched_intent = match_intent(message, intents)
    if matched_intent:
        # 使用响应模板
        template = matched_intent.get('response_template', '')
        if template:
            # 简单替换占位符
            response = template.replace('{功能列表}', '多种实用功能') \
                              .replace('{特点}', '高性能、易使用') \
                              .replace('{适用人群}', '广大用户') \
                              .replace('{质保期}', '1 年') \
                              .replace('{价格}', '优惠') \
                              .replace('{活动信息}', '促销中') \
                              .replace('{库存状态}', '有现货') \
                              .replace('{发货时间}', '24 小时')
            return response
        return f"您好，关于{matched_intent.get('description', '这个问题')}，我很乐意为您解答。"
    
    # 默认回复
    default_responses = [
        "抱歉，我没有理解您的问题。您可以问我关于产品功能、价格、物流、退货等问题。",
        "这个问题我还不太懂，您可以换个方式问我，或者联系人工客服。",
        "您好，我是智能客服助手，可以为您解答产品咨询、订单查询、售后服务等问题。"
    ]
    return random.choice(default_responses)

@app.route('/')
def index():
    """聊天页面"""
    return render_template('chat.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """聊天 API"""
    data = request.get_json()
    message = data.get('message', '')
    
    if not message:
        return jsonify({'error': '消息不能为空'}), 400
    
    # 加载数据
    intents = load_intents()
    faq_list = load_faq()
    
    # 生成回复
    response = generate_response(message, intents, faq_list)
    
    return jsonify({
        'response': response,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/health')
def health():
    """健康检查"""
    return jsonify({'status': 'ok', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    print("启动电商智能客服 Web 演示...")
    print("访问地址：http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
