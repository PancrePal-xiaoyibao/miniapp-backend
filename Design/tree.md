# 医疗健康 AI 助手小程序后端项目结构

```
backend/
├── README.md                # 项目说明文档
├── app/                    # 应用主目录
│   ├── __init__.py
│   ├── api/               # API 接口目录
│   │   ├── __init__.py
│   ├── v1/                # API v1 版本目录
│   │   ├── __init__.py
│   │   ├── conversations.py  # 对话管理 API
│   │   ├── logs.py          # 日志管理 API
│   │   ├── text_chat.py     # 文本对话 API
│   │   ├── vision_chat.py   # 图像对话 API
│   │   ├── upload.py        # 文件上传 API
│   │   ├── users.py         # 用户管理 API
│   ├── models/            # 数据模型目录
│   │   ├── __init__.py
│   │   └── data/          # 数据模型定义
│   │       ├── __init__.py
│   │       ├── conversations.py  # 对话数据模型
│   │       ├── files.py         # 文件数据模型
│   │       ├── images.py        # 图片数据模型
│   │       ├── system_logs.py   # 系统日志数据模型
│   │       ├── users.py         # 用户数据模型
│   ├── utils/             # 工具函数目录
│   │   ├── __init__.py
│   │   ├── security/      # 安全相关工具包
│   │   │   ├── __init__.py
│   │   │   ├── auth.py      # 认证/授权工具
│   │   │   ├── jwt_auth.py  # JWT 认证工具
│   │   │   └── rate_limiter.py # 限流工具
│   │   ├── db/            # 数据库工具包
│   │   │   ├── __init__.py
│   │   │   └── database.py  # 数据库操作工具
│   │   └── storage/       # 存储工具包
│   │       ├── __init__.py
│   │       ├── oss.py      # 腾讯云 OSS 工具
│   │       └── sealososs.py # Sealos OSS 工具
│   ├── config.py         # 配置管理
│   └── config.json       # 配置文件
├── docs/                 # 文档目录
│   ├── README.md          # 项目说明文档
│   ├── architecture.md    # 架构设计文档
│   ├── function.md        # 功能说明文档
│   ├── deployment.md      # 部署说明文档
│   └── environment.md     # 环境配置说明
├── main.py              # 应用入口
└── requirements.txt     # 项目依赖
```

## 目录说明

### 核心目录

- `app/`: 应用主目录，包含所有源代码
  - `api/v1/`: API v1版本接口定义，按功能模块组织
  - `models/data/`: 数据模型定义，与数据库表对应
  - `utils/`: 工具函数，按功能模块化组织

### 工具模块

- `utils/security/`: 安全相关工具，包含认证和限流
- `utils/db/`: 数据库操作工具
- `utils/storage/`: 存储服务工具，支持多种存储方案

### 配置文件

- `config.py`: 应用配置管理
- `config.json`: 配置项定义
- `requirements.txt`: Python 包依赖

### 文档

- `docs/`: 项目文档目录
  - `README.md`: 项目说明
  - `architecture.md`: 架构设计
  - `function.md`: 功能说明
  - `deployment.md`: 部署说明
  - `environment.md`: 环境配置

## 特点

- 清晰的 API 版本控制
- 模块化的数据模型组织
- 功能分类的工具模块
- 统一的文档管理
- 集中的配置管理
