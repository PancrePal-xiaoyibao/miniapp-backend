# 小胰宝本地化部署架构设计

## 1. 项目概述

本项目旨在将原有的云开发版小胰宝小程序改造为支持本地化部署的完整解决方案，实现前后端分离架构。

## 2. 系统架构

### 2.1 整体架构

```
miniapp-local/
├── client/                # 小程序前端
│   ├── config/           # 配置文件
│   ├── services/         # API服务封装
│   ├── utils/            # 工具函数
│   └── ... (原小程序结构)
├── server/               # 后端服务
│   ├── config/          # 服务端配置
│   ├── controllers/     # 控制器
│   ├── models/          # 数据模型
│   ├── routes/          # 路由定义
│   ├── services/        # 业务逻辑
│   └── utils/           # 工具函数
└── docs/                # 项目文档
```

### 2.2 技术栈选型

#### 前端（client）
- 框架：微信小程序原生框架
- 请求库：统一封装的HTTP请求模块
- 状态管理：小程序原生数据管理

#### 后端（server）
- 运行时：Node.js
- Web框架：Express.js
- 数据库：MongoDB
- ORM：Mongoose
- API规范：RESTful

## 3. 核心功能模块

### 3.1 用户认证模块
- 微信登录授权
- JWT token管理
- 用户信息管理

### 3.2 AI对话模块
- 对话历史管理
- AI模型调用封装
- 实时消息推送

### 3.3 病情管理模块
- 检验报告管理
- 治疗记录追踪
- 数据可视化

### 3.4 病友宝典模块
- 文档管理
- 内容搜索
- 分类导航

## 4. 数据库设计

### 4.1 核心集合

```javascript
// 用户集合
users: {
  _id: ObjectId,
  openid: String,
  userInfo: Object,
  createdAt: Date
}

// 对话历史集合
chat_history: {
  _id: ObjectId,
  userId: ObjectId,
  messages: Array,
  createdAt: Date
}

// 病情记录集合
medical_records: {
  _id: ObjectId,
  userId: ObjectId,
  type: String,
  data: Object,
  createdAt: Date
}

// 宝典文档集合
handbook_docs: {
  _id: ObjectId,
  title: String,
  content: String,
  category: String,
  updatedAt: Date
}
```

## 5. API接口设计

### 5.1 认证接口
- POST /api/auth/login
- GET /api/auth/userinfo

### 5.2 AI对话接口
- POST /api/chat/message
- GET /api/chat/history

### 5.3 病情管理接口
- POST /api/medical/record
- GET /api/medical/records
- PUT /api/medical/record/:id

### 5.4 宝典接口
- GET /api/handbook/docs
- GET /api/handbook/doc/:id
- GET /api/handbook/search

## 6. 部署方案

### 6.1 开发环境
- 前端：微信开发者工具
- 后端：本地Node.js服务
- 数据库：本地MongoDB实例

### 6.2 生产环境
- 前端：微信小程序发布
- 后端：Node.js服务器部署
- 数据库：MongoDB集群

## 7. 安全方案

### 7.1 数据安全
- 数据传输加密（HTTPS）
- 敏感数据加密存储
- 定期数据备份

### 7.2 访问控制
- JWT认证
- 接口权限控制
- 请求频率限制

## 8. 后续优化方向

1. 引入缓存层提升性能
2. 添加监控告警系统
3. 优化AI模型调用效率
4. 增强数据分析功能
5. 提供运营管理后台




--- 二期工作


## 9. 管理后台设计

### 9.1 核心功能
- 内容管理系统（CMS）
  - 宝典文档的创建、编辑、删除
  - 内容分类管理
  - 富文本编辑器支持
  
- AI配置管理
  - AI模型参数配置
  - Prompt模板管理
  - Agent行为配置
  - API密钥管理

- 运营数据
  - 用户数据统计
  - AI对话质量监控
  - 使用情况分析

### 9.2 技术方案
- 前端：React + Ant Design
- 后端：复用现有Express服务
- 权限：基于角色的访问控制（RBAC）

### 9.3 数据模型补充
```javascript
// 管理员用户
admin_users: {
  _id: ObjectId,
  username: String,
  password: String,
  role: String,
  createdAt: Date
}

// AI配置表
ai_configs: {
  _id: ObjectId,
  type: String,      // 配置类型：model/prompt/agent
  name: String,      // 配置名称
  config: Object,    // 具体配置内容
  isActive: Boolean, // 是否启用
  updatedAt: Date
}

### 9.4 新增API接口
- POST /api/admin/auth/login    // 管理员登录
- GET /api/admin/configs        // 获取AI配置
- PUT /api/admin/configs/:id    // 更新AI配置
- POST /api/admin/handbook      // 创建宝典内容
- GET /api/admin/statistics     // 获取统计数据

### 1. 必要性分析
1. 内容管理需求
   
   - 病友宝典内容需要定期更新和维护
   - 直接在数据库中修改内容既不安全也不方便
   - 内容编辑需要预览、格式化等功能支持
2. AI配置管理需求
   
   - AI模型的配置（baseURL、API key）可能需要动态调整
   - Agent和Prompt的配置需要专业人员调试和优化
   - 不同场景可能需要不同的AI配置方案
3. 运营需求
   
   - 需要查看用户使用数据和统计信息
   - 监控AI对话质量
   - 管理用户反馈
### 2. 建议的管理后台功能模块
建议在架构文档中添加管理后台相关内容：


### 3. 实施建议

1. **优先级**
   - 建议将管理后台作为第二阶段开发内容
   - 先完成小程序核心功能，再开发管理功能

2. **实施步骤**
   - 先实现基础的内容管理功能
   - 再添加AI配置管理
   - 最后完善数据统计和监控功能

3. **注意事项**
   - 严格控制管理后台的访问权限
   - 确保AI配置的修改有审核机制
   - 做好数据备份和操作日志

这个管理后台将大大提升系统的可维护性和运营效率，建议将其纳入整体架构规划中。