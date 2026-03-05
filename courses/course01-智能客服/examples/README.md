# 智能客服课程 - 实战示例

> 💻 电商智能客服完整代码示例 - 可运行、可演示、可教学

---

## 📚 示例概览

本目录包含智能客服课程的完整实战代码示例，用于课堂演示和学员实验。

### 已完成的示例

| 示例 | 行业 | 状态 | 规模 | 完成时间 |
|------|------|------|------|---------|
| [ecommerce/](ecommerce/README.md) | 电商 | ✅ 完成 | 19 个文件，~3,200 行代码 | 2026-03-05 |

### 规划中的示例

| 示例 | 行业 | 状态 | 预计规模 |
|------|------|------|---------|
| education/ | 教育 | 🚧 规划中 | ~3,000 行代码 |
| healthcare/ | 医疗 | 🚧 规划中 | ~3,000 行代码 |

---

## 🎯 电商智能客服示例

### 核心功能
1. **意图识别系统**
   - 8 个核心意图（售前咨询、订单查询、售后服务）
   - 125 条训练语料
   - 支持槽位填充

2. **对话流程引擎**
   - 物流查询对话流程（10 个节点）
   - 退货申请对话流程（14 个节点）
   - 支持多轮对话和条件分支

3. **FAQ 知识库**
   - 90 个电商 FAQ
   - 4 大类别（售前、订单、售后、通用）
   - 支持相似问题匹配

4. **API 集成示例**
   - 订单 API 集成客户端
   - 物流 API 集成客户端
   - 完整的错误处理

5. **Web 聊天窗口**
   - Flask 后端应用
   - 美观的前端界面
   - 实时对话功能
   - 快捷回复按钮

### 技术栈
- **后端**: Python 3 + Flask 2.3.0
- **前端**: HTML5 + CSS3 + JavaScript
- **数据**: JSON + CSV
- **配置**: 多平台支持（百度、阿里、腾讯）

### 快速开始
```bash
cd ecommerce
./quickstart.sh
# 访问 http://localhost:5001
```

### 详细文档
- [电商示例使用说明](ecommerce/README.md)
- [电商示例项目总结](ecommerce/PROJECT_SUMMARY.md)
- [界面截图说明](ecommerce/screenshots/README.md)

---

## 📁 目录结构

```
examples/
├── README.md                      # 本文件
├── 开发任务.json                  # 开发任务规划
├── 交付说明.md                    # 交付成果说明
│
├── ecommerce/                     # 电商示例（Phase 1 完成 ✅）
│   ├── intents/                   # 意图定义
│   │   └── ecommerce_intents.json # 8 个意图，125 条语料
│   ├── dialog_flows/              # 对话流程
│   │   ├── logistics_flow.json    # 物流查询
│   │   └── return_flow.json       # 退货申请
│   ├── faq/                       # FAQ 知识库
│   │   └── ecommerce_faq.csv      # 90 个 FAQ
│   ├── integrations/              # API 集成示例
│   │   ├── order_api.py           # 订单 API
│   │   └── logistics_api.py       # 物流 API
│   ├── webchat/                   # Web 聊天窗口
│   │   ├── app.py                 # Flask 应用
│   │   └── templates/chat.html    # 聊天页面
│   ├── configs/                   # 配置文件模板
│   │   ├── baidu_config.json      # 百度配置
│   │   ├── aliyun_config.json     # 阿里配置
│   │   └── tencent_config.json    # 腾讯配置
│   ├── data/                      # 演示数据
│   │   └── test_orders.json       # 测试订单
│   ├── screenshots/               # 界面截图
│   │   ├── README.md
│   │   ├── webchat-demo.png
│   │   └── demo-chat-*.png
│   ├── PROJECT_SUMMARY.md         # 项目总结
│   ├── README.md                  # 使用说明
│   ├── requirements.txt           # Python 依赖
│   ├── .env.example               # 环境变量
│   └── quickstart.sh              # 快速启动脚本
│
└── shared/                        # 共享资源（规划中）
    ├── utils/                     # 通用工具
    ├── templates/                 # 通用模板
    └── docs/                      # 通用文档
```

---

## 🚀 使用方式

### 1. 课堂演示
```bash
# 启动 Web 聊天演示
cd ecommerce
./quickstart.sh
# 选择选项 1，访问 http://localhost:5001
```

### 2. 查看代码示例
```bash
# 查看意图定义
cat ecommerce/intents/ecommerce_intents.json

# 查看对话流程
cat ecommerce/dialog_flows/logistics_flow.json

# 查看 API 集成
cat ecommerce/integrations/order_api.py
```

### 3. 运行测试
```bash
# 测试订单 API
python3 ecommerce/integrations/order_api.py

# 测试物流 API
python3 ecommerce/integrations/logistics_api.py
```

---

## 📊 开发进度

### Phase 1: 电商示例（✅ 完成）
- 意图定义：8 个核心意图，125 条训练语料
- 对话流程：2 个完整流程（物流查询、退货申请）
- FAQ 知识库：90 个电商 FAQ
- API 集成：订单 API、物流 API
- Web 应用：Flask 聊天窗口
- 配置文件：3 个云平台模板
- 演示数据：3 个测试订单
- 界面截图：5 张
- 文档说明：完整 README 和总结

**总计**: 19 个文件，~3,200 行代码

### Phase 2: 教育示例（🚧 规划中）
- K12 教育场景
- 语言培训场景
- 职业教育场景

### Phase 3: 医疗示例（🚧 规划中）
- 医院导诊场景
- 健康咨询场景
- 预约挂号场景

---

## 🎓 教学应用

### 场景 1: 课堂演示（15 分钟）
1. 启动 Web 聊天应用
2. 演示用户提问"产品怎么用？"
3. 展示意图识别和 FAQ 匹配过程
4. 展示智能回复生成

### 场景 2: 学员实验（30 分钟）
1. 修改意图定义文件
2. 添加新的训练语料
3. 测试意图识别效果
4. 对比修改前后差异

### 场景 3: 对话流程设计（45 分钟）
1. 分析现有对话流程
2. 设计新的对话节点
3. 配置槽位填充规则
4. 测试多轮对话效果

### 场景 4: API 集成实战（60 分钟）
1. 学习 API 客户端编写
2. 集成真实订单系统
3. 集成物流查询 API
4. 处理异常情况

---

## 📚 相关文档

- [课程主页](../INDEX.md)
- [开发任务](开发任务.json)
- [交付说明](交付说明.md)
- [电商示例详细说明](ecommerce/README.md)

---

## 💡 扩展建议

### 短期优化（1-2 小时）
1. 添加更多意图（产品推荐、投诉处理）
2. 完善对话流程（换货、维修流程）
3. 增加测试用例
4. 优化 UI 样式

### 中期扩展（4-8 小时）
1. 集成真实 API（订单系统、物流系统）
2. 增加多轮对话复杂度
3. 添加数据分析功能
4. 支持多平台部署

### 长期规划（16+ 小时）
1. 开发完整后台管理系统
2. 添加用户画像和个性化推荐
3. 实现语音交互功能
4. 开发移动端应用

---

**版本**: v3.1  
**更新日期**: 2026-03-05  
**项目状态**: ✅ Phase 1 完成，🚧 Phase 2 规划中  
**GitHub**: https://github.com/www063sss-wq/AI-course-creator.git
