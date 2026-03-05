# AI 培训课程项目

> 🎓 AI 培训课程多课程解决方案 - 智能客服系列课程

---

## 🎯 项目概述

这是一个多课程体系的 AI 培训课程项目，提供从课程产品文档、授课全流程到实战代码示例的完整解决方案。

### 课程体系
- ✅ **Course 01**：企业 AI 落地第一课：从 0 到 1 搭建智能客服（已完成）
- 🚧 **Course 02**：[规划中]

### 核心特点
- ✅ **实战性**：40% 时间实践演练，提供完整代码示例
- ✅ **工具齐全**：提供完整模板、检查清单和配置文件
- ✅ **案例真实**：全部来自真实企业实践场景
- ✅ **可落地**：带回可直接使用的方案和代码
- ✅ **全流程**：覆盖课前、课中、课后全生命周期
- ✅ **多平台支持**：兼容百度、阿里、腾讯三大云平台

---

## 📁 项目结构

```
AI 培训产品经理/
├── README.md                    # 项目总览（本文件）
├── DEVELOPMENT_GUIDE.md         # 开发指南（重要！）
├── .git/                        # Git 版本控制
│
├── courses/                     # 📚 课程目录
│   └── course01-智能客服/       # 课程 1（已完成 ✅）
│       ├── INDEX.md             # 课程产品索引
│       │
│       ├── core/                # 📖 核心产品文档（7 个）
│       │   ├── 00-需求文档.md
│       │   ├── 01-课程大纲.md
│       │   ├── 02-教学方法.md
│       │   ├── 03-评估方式.md
│       │   ├── 04-课程收益.md
│       │   ├── 05-后续支持.md
│       │   └── 06-核心知识点.md
│       │
│       ├── delivery/            # 📋 交付文档（3 个）
│       │   ├── 01-课前准备清单.md
│       │   ├── 02-授课流程手册.md
│       │   └── 03-课后跟进手册.md
│       │
│       ├── support/             # 🎤 讲师支持材料
│       │   └── 01-讲师讲稿.md（1999 行完整讲稿）
│       │
│       ├── docs/                # 📚 参考资料
│       │   └── reference/       # 企业教学特点分析等
│       │
│       └── examples/            # 💻 实战代码示例
│           ├── README.md                    # 实例总览
│           ├── 开发任务.json                # 开发任务规划
│           ├── 交付说明.md                  # 交付成果说明
│           │
│           ├── ecommerce/                   # 电商示例（Phase 1 完成 ✅）
│           │   ├── intents/                 # 意图定义
│           │   │   └── ecommerce_intents.json（8 个意图，125 条语料）
│           │   ├── dialog_flows/            # 对话流程
│           │   │   ├── logistics_flow.json（物流查询）
│           │   │   └── return_flow.json（退货申请）
│           │   ├── faq/                     # FAQ 知识库
│           │   │   └── ecommerce_faq.csv（90 个 FAQ）
│           │   ├── integrations/            # API 集成示例
│           │   │   ├── order_api.py（订单 API）
│           │   │   └── logistics_api.py（物流 API）
│           │   ├── webchat/                 # Web 聊天窗口
│           │   │   ├── app.py（Flask 应用）
│           │   │   └── templates/chat.html（聊天页面）
│           │   ├── configs/                 # 配置文件模板
│           │   │   ├── baidu_config.json（百度）
│           │   │   ├── aliyun_config.json（阿里）
│           │   │   └── tencent_config.json（腾讯）
│           │   ├── data/                    # 演示数据
│           │   │   └── test_orders.json（测试订单）
│           │   ├── screenshots/             # 界面截图（5 张）
│           │   │   ├── README.md
│           │   │   ├── webchat-demo.png
│           │   │   ├── demo-chat-product.png
│           │   │   ├── demo-chat-price.png
│           │   │   ├── demo-chat-order.png
│           │   │   └── demo-chat-return.png
│           │   ├── PROJECT_SUMMARY.md       # 项目总结
│           │   ├── README.md                # 使用说明
│           │   ├── requirements.txt         # Python 依赖
│           │   ├── .env.example             # 环境变量
│           │   └── quickstart.sh            # 快速启动脚本
│           │
│           └── shared/                      # 共享资源
│               ├── utils/                   # 通用工具
│               ├── templates/               # 通用模板
│               └── docs/                    # 通用文档
│
└── shared/                      # 🔧 项目级共享资源
    ├── templates/               # 通用模板
    ├── assets/                  # 通用素材
    └── scripts/                 # 通用脚本
```

---

## �� 快速开始

### 查看课程产品
```bash
# 查看课程 01 的产品说明
cat courses/course01-智能客服/INDEX.md

# 查看课程大纲
cat courses/course01-智能客服/core/01-课程大纲.md

# 查看讲师讲稿
cat courses/course01-智能客服/support/01-讲师讲稿.md
```

### 运行实战示例
```bash
# 进入电商示例目录
cd courses/course01-智能客服/examples/ecommerce

# 一键启动 Web 聊天演示
./quickstart.sh
# 选择选项 1，访问 http://localhost:5001
```

### 查看代码示例
```bash
# 查看意图定义
cat ecommerce/intents/ecommerce_intents.json

# 查看对话流程
cat ecommerce/dialog_flows/logistics_flow.json

# 查看 API 集成示例
cat ecommerce/integrations/order_api.py

# 查看 Web 聊天应用
cat ecommerce/webchat/app.py
```

---

## 📚 Course 01：智能客服

### 产品信息
- **课程名称**：企业 AI 落地第一课：从 0 到 1 搭建智能客服
- **课程时长**：3 小时（实战工作坊）
- **目标学员**：企业技术负责人、产品经理、客服主管
- **产品状态**：✅ 可交付（含完整代码示例）

### 核心文档（7 个）
- [需求文档](courses/course01-智能客服/core/00-需求文档.md)
- [课程大纲](courses/course01-智能客服/core/01-课程大纲.md)
- [教学方法](courses/course01-智能客服/core/02-教学方法.md)
- [评估方式](courses/course01-智能客服/core/03-评估方式.md)
- [课程收益](courses/course01-智能客服/core/04-课程收益.md)
- [后续支持](courses/course01-智能客服/core/05-后续支持.md)
- [核心知识点](courses/course01-智能客服/core/06-核心知识点.md)

### 交付文档（3 个）
- [课前准备清单](courses/course01-智能客服/delivery/01-课前准备清单.md)
- [授课流程手册](courses/course01-智能客服/delivery/02-授课流程手册.md)
- [课后跟进手册](courses/course01-智能客服/delivery/03-课后跟进手册.md)

### 讲师支持
- [讲师讲稿](courses/course01-智能客服/support/01-讲师讲稿.md) - 1999 行完整讲稿
  - 开场（5 分钟）
  - 模块 1：智能客服认知与价值（40 分钟）
  - 模块 2：系统架构与选型（50 分钟）
  - 模块 3：实战演练（60 分钟）
  - 模块 4：落地策略与实施计划（30 分钟）
  - 总结与答疑（15 分钟）

### 实战示例（Phase 1 完成）
- **电商智能客服示例** ([查看详情](courses/course01-智能客服/examples/ecommerce/README.md))
  - 8 个核心意图，125 条训练语料
  - 2 个完整对话流程（物流查询、退货申请）
  - 90 个电商 FAQ 知识库
  - 订单和物流 API 集成示例
  - 可交互 Web 聊天窗口（Flask + HTML）
  - 三大云平台配置模板
  - 5 张界面截图

### 目标收益
- **企业收益**：客服成本降低 20-40%，效率提高 50-100%
- **学员收益**：掌握智能客服搭建方法，获得可落地计划和代码示例

---

## 💻 实战示例详情

### 电商智能客服示例

#### 核心功能
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

#### 技术栈
- **后端**: Python 3 + Flask 2.3.0
- **前端**: HTML5 + CSS3 + JavaScript
- **数据**: JSON + CSV
- **配置**: 多平台支持（百度、阿里、腾讯）

#### 运行方式
```bash
cd courses/course01-智能客服/examples/ecommerce
./quickstart.sh
# 访问 http://localhost:5001
```

---

## 🛠️ 开发指南

### 重要文档
- 📖 [DEVELOPMENT_GUIDE.md](DEVELOPMENT_GUIDE.md) - **开发前必读**

### 开发步骤
1. 阅读开发指南
2. 参考 Course 01 的实现
3. 在 `courses/course02-` 目录下开发
4. 遵循 Git 提交规范

### 开发规范
- ✅ 使用中文文件名（带编号）
- ✅ 遵循文档结构规范
- ✅ 及时 Git 提交
- ❌ 不要修改 Course 01 的文件

---

## 📊 开发进度

### Course 01：智能客服

| 模块 | 内容 | 状态 | 数量 |
|------|------|------|------|
| 核心文档 | 需求、大纲、方法等 | ✅ 完成 | 7/7 |
| 交付文档 | 课前、课中、课后 | ✅ 完成 | 3/3 |
| 讲师讲稿 | 3 小时完整讲稿 | ✅ 完成 | 1999 行 |
| 实战示例 | 电商智能客服 | ✅ 完成 | 19 个文件 |
| 代码示例 | 意图、流程、API 等 | ✅ 完成 | ~3,200 行 |
| 界面截图 | Web 聊天界面 | ✅ 完成 | 5 张 |

### 实战示例统计

| 组件 | 文件数 | 代码行数 | 数据量 |
|------|--------|---------|--------|
| 意图定义 | 1 | ~400 | 8 个意图，125 条语料 |
| 对话流程 | 2 | ~600 | 24 个节点 |
| FAQ 知识库 | 1 | ~90 | 90 个 FAQ |
| API 集成 | 2 | ~300 | 2 个客户端 |
| Web 应用 | 2 | ~500 | 1 个聊天窗口 |
| 配置文件 | 3 | ~200 | 3 个平台 |
| 演示数据 | 1 | ~200 | 3 个订单 |
| 文档 | 5 | ~800 | 完整说明 |
| **总计** | **19** | **~3,200** | **5 张截图** |

---

## 📞 协作说明

### 智能体协作
- **Course 01**：由第一个智能体维护
- **Course 02**：由第二个智能体开发
- **共享资源**：放在 `shared/` 目录

### 沟通机制
- 查看 `DEVELOPMENT_GUIDE.md` 了解协作规范
- 遵循 Git 提交规范记录变更
- 定期同步开发进度

---

## 🔄 版本历史

### v3.1 (2026-03-05) - Phase 1 实战示例完成
- ✅ 完成电商智能客服示例开发（19 个文件，~3,200 行代码）
- ✅ 创建 Web 聊天窗口（Flask + HTML）
- ✅ 实现 8 个核心意图和 2 个对话流程
- ✅ 构建 90 个 FAQ 知识库
- ✅ 提供订单和物流 API 集成示例
- ✅ 创建三大云平台配置模板
- ✅ 截取 5 张界面演示图
- ✅ 编写完整项目总结和使用说明

### v3.0 (2026-03-04) - 多课程重构
- 重构为多课程项目结构
- 创建开发指南文档
- 迁移 Course 01 到新结构

### v2.0 (2026-03-04) - 产品化重构
- 重构为产品化结构
- 创建完整授课全流程文档
- 增加工具模板和案例库

### v1.0 (2026-03-04) - 初始版本
- 创建课程需求清单
- 完成详细文档编写

---

## 📄 许可证

本项目文档和代码版权归作者所有，未经许可不得转载或用于商业用途。

---

**项目版本**：v3.1  
**更新日期**：2026-03-05  
**项目状态**：✅ Course 01 可交付（含实战代码），🚧 Course 02 规划中  
**开发指南**：[DEVELOPMENT_GUIDE.md](DEVELOPMENT_GUIDE.md)  
**示例演示**：http://localhost:5001（运行中）  
**GitHub**: https://github.com/www063sss-wq/AI-course-creator.git
