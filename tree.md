# 医疗健康 AI 助手小程序后端项目结构

```
backend/
├── README.md                # 项目说明文档
├── app/                    # 应用主目录
│   ├── __init__.py
│   ├── api/               # API 接口目录
│   │   ├── __init__.py
│   │   ├── conversations.py  # 对话管理 API
│   │   ├── logs.py          # 日志管理 API
│   │   ├── text_chat.py     # 文本对话 API
│   │   ├── vision_chat.py   # 图像对话 API
│   │   ├── upload.py        # 文件上传 API
│   │   ├── users.py         # 用户管理 API
│   │   └── v1/             # API 版本控制目录
│   ├── config.json        # 配置文件
│   ├── config.py          # 配置管理
│   ├── main.py            # 应用入口
│   ├── models/            # 数据模型目录
│   │   ├── __init__.py
│   │   ├── conversations.py  # 对话数据模型
│   │   ├── data/            # 数据模型子目录
│   │   ├── files.py         # 文件数据模型
│   │   ├── images.py        # 图片数据模型
│   │   ├── system_logs.py   # 系统日志数据模型
│   │   └── users.py         # 用户数据模型
│   └── utils/             # 工具函数目录
│       ├── __init__.py
│       ├── auth.py          # 认证/授权工具
│       ├── database.py      # 数据库操作工具
│       ├── db/              # 数据库工具子目录
│       ├── oss.py           # 腾讯云 OSS 工具
│       ├── sealososs.py     # Sealos OSS 工具
│       └── security/        # 安全相关工具目录
├── function.md            # 功能说明文档
├── requirements.txt       # 项目依赖
├── tree.md               # 目录结构说明文档
└── 配置环境.md             # 环境配置说明文档
```

## 目录说明

### 核心目录

- `app/`: 应用主目录，包含所有源代码
  - `api/`: API 接口定义，按功能模块组织
  - `models/`: 数据模型定义，与数据库表对应
  - `utils/`: 工具函数，包含认证、数据库、存储等功能

### 配置文件

- `config.py`: 应用配置管理，包含数据库连接、API密钥等配置的读取和管理
- `config.json`: 具体的配置项，包含数据库、FastGPT、腾讯云等服务的配置信息
- `requirements.txt`: Python 包依赖

### 文档

- `README.md`: 项目说明
- `function.md`: 功能文档
- `配置环境.md`: 环境配置说明
- `tree.md`: 本文件，项目结构说明

## 特点

- 模块化结构，便于维护和扩展
- API 版本控制，支持接口演进
- 清晰的工具函数分类
- 完整的文档支持
- 统一的配置管理
