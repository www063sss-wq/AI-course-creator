# 智能客服课程实例开发计划

## 📋 概述

本目录包含课程 01《企业 AI 落地第一课：从 0 到 1 搭建智能客服》的完整实战演示实例。

## 🎯 目标

为学员提供：
- **可运行的代码示例**：直接可用的意图定义、对话流程、API 集成
- **多行业场景**：电商、教育、医疗三大典型场景
- **完整配置**：主流平台（百度、阿里、腾讯）配置模板
- **详细文档**：使用说明、部署指南、API 文档

## 📁 目录结构

```
examples/
├── ecommerce/              # 电商示例（优先级：高）
│   ├── intents/           # 意图定义
│   ├── dialog_flows/      # 对话流程
│   ├── faq/              # FAQ 知识库
│   ├── integrations/      # API 集成
│   ├── webchat/          # Web 聊天窗口
│   ├── configs/          # 配置文件
│   ├── data/             # 演示数据
│   └── README.md         # 电商示例说明
├── education/            # 教育示例（优先级：中）
│   └── ...
├── healthcare/           # 医疗示例（优先级：低）
│   └── ...
├── shared/               # 共享资源
│   ├── utils/
│   ├── templates/
│   └── docs/
├── README.md             # 本文件
├── DEPLOYMENT.md         # 部署指南（待创建）
└── .env.example          # 环境变量示例
```

## 📊 开发计划

### Phase 1：电商示例开发（8 小时）⭐⭐⭐

**场景覆盖**：
- 售前咨询（30 个 FAQ）
- 订单查询（25 个 FAQ）
- 售后服务（35 个 FAQ）

**意图开发**（8 个）：
1. `product_consult` - 产品功能咨询
2. `price_inquiry` - 价格咨询
3. `stock_check` - 库存查询
4. `order_logistics_query` - 物流查询
5. `order_status_query` - 订单状态查询
6. `after_sale_return` - 退货申请
7. `after_sale_exchange` - 换货申请
8. `complaint` - 投诉建议

**对话流程**（2 个）：
1. 物流查询流程（3 轮对话）
2. 退货申请流程（4 轮对话）

**交付物**：
- ✅ 意图定义文件（JSON 格式）
- ✅ 对话流程配置（JSON 格式）
- ✅ 90 个 FAQ（CSV 格式）
- ✅ API 集成示例（Python）
- ✅ Web 聊天窗口示例（HTML/JS）
- ✅ 配置文件模板
- ✅ 演示数据
- ✅ 使用说明文档

### Phase 2：教育示例开发（6 小时）⭐⭐

**场景覆盖**：
- 课程咨询（40 个 FAQ）
- 报名缴费（30 个 FAQ）
- 学习支持（35 个 FAQ）

**交付物**：
- 意图定义文件
- 对话流程配置
- 105 个 FAQ
- 使用说明文档

### Phase 3：医疗示例开发（6 小时）⭐

**场景覆盖**：
- 预约挂号（25 个 FAQ）
- 科室导诊（30 个 FAQ）
- 报告查询（20 个 FAQ）

**交付物**：
- 意图定义文件
- 对话流程配置
- 75 个 FAQ
- 使用说明文档

### Phase 4：文档和完善（4 小时）⭐⭐⭐

**任务**：
- 总 README 编写
- 部署指南编写
- API 文档编写
- 全示例测试
- 代码质量优化
- 演示视频录制

## 🔧 技术要求

### 编程语言
- Python 3.8+
- JavaScript ES6+

### 支持平台
- 百度智能云
- 阿里云小蜜
- 腾讯云智服

### 开发工具
- Git（版本控制）
- VS Code（代码编辑）
- Postman（API 测试）

### 依赖库
```python
requests>=2.28.0
flask>=2.0.0
python-dotenv>=0.20.0
```

## ✅ 成功标准

1. **准确率**：所有意图识别准确率>90%
2. **流畅性**：对话流程顺畅，无逻辑错误
3. **覆盖率**：FAQ 覆盖 80% 常见问题
4. **可用性**：代码可运行，无语法错误
5. **文档**：完整易懂，易于学习
6. **演示**：示例可演示，效果良好

## 📝 开发任务详情

详细开发任务请查看：[`开发任务.json`](./开发任务.json)

该 JSON 文件包含：
- 完整的意图定义（名称、描述、训练语料、槽位）
- 对话流程配置（步骤、槽位填充、API 调用）
- FAQ 清单
- 交付物列表
- 开发阶段和时间估算
- 技术要求和成功标准

## 🔍 审查清单

在开始开发前，请审查以下内容：

- [ ] 目录结构是否合理？
- [ ] 意图定义是否完整？
- [ ] 对话流程是否清晰？
- [ ] FAQ 是否覆盖全面？
- [ ] 代码示例是否可运行？
- [ ] 文档是否完整易懂？
- [ ] 是否符合课程教学目标？

## 📋 下一步

1. **审查开发任务**：查看 `开发任务.json` 了解详细任务
2. **确认优先级**：Phase 1（电商示例）优先级最高
3. **准备开发环境**：安装 Python、Node.js、Git
4. **获取 API 密钥**：注册百度智能云/阿里云/腾讯云账号
5. **开始开发**：按照任务文档开始 Phase 1 开发

## 💡 使用说明（开发完成后）

### 快速开始

```bash
# 1. 克隆项目
git clone https://github.com/www063sss-wq/AI-course-creator.git
cd AI-course-creator/courses/course01-智能客服/examples

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入 API 密钥

# 4. 运行示例
python ecommerce/demo.py

# 5. 打开浏览器
# 访问 http://localhost:5000
```

### 测试意图识别

```python
from intents import EcommerceIntents

intents = EcommerceIntents()
result = intents.predict("我的订单到哪了")
print(result)
# 输出：{'intent': 'order_logistics_query', 'confidence': 0.95}
```

### 测试对话流程

```python
from dialog_flows import ReturnFlow

flow = ReturnFlow()
response = flow.process_step(1, {"order_id": "123456"})
print(response)
# 输出：查询到订单 iPhone 15，请问退货原因是？
```

## 📞 协作说明

- **开发指南**：查看项目根目录的 `DEVELOPMENT_GUIDE.md`
- **问题反馈**：在 GitHub 创建 Issue
- **代码审查**：提交 Pull Request

## 📄 许可证

本项目文档版权归作者所有，未经许可不得转载或用于商业用途。

---

**版本**：1.0.0  
**更新日期**：2026-03-05  
**状态**：📋 待审查
