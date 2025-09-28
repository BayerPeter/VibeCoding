# 投诉协助系统

一个用于管理药品产品投诉和生成调查报告的系统。

## 前提条件

1. Python 3.8 或更高版本
2. pip（Python 包管理器）

## 安装与设置

1. 克隆或下载此仓库
2. 确保 Python 已添加到系统的 PATH 中
3. 双击 `run_server.bat` 或从命令行运行它

该批处理文件将：
- 检查 Python 安装
- 创建必要的目录
- 安装所需的包
- 初始化数据库
- 启动服务器

## 使用系统

服务器启动后，您可以通过 http://localhost:8080 访问系统。

### 主要功能

1. **提交投诉**
   - 前往 http://localhost:8080/complaints/create
   - 填写投诉描述
   - 可选地附加图片
   - 提交以获取自动分析

2. **查看投诉**
   - 前往 http://localhost:8080/complaints
   - 查看所有提交的投诉
   - 访问详细报告

3. **调查报告**
   - 前往 http://localhost:8080/reports
   - 查看所有调查报告
   - 跟踪 CAPA 行动

### API 文档

- 可在 http://localhost:8080/docs 访问
- 显示所有 API 端点和模式

## 系统功能

- 自动投诉分析
- 报告生成
- 图片附件支持
- 投诉历史跟踪
- CAPA 管理
- 当 RAG 服务不可用时支持虚拟数据

## 故障排除

1. 如果服务器未启动：
   - 确保已安装 Python 并在 PATH 中
   - 检查端口 8080 是否可用
   - 查找控制台中的错误消息

2. 如果无法访问 Web 界面：
   - 验证服务器是否正在运行
   - 尝试先访问 http://localhost:8080/docs
   - 检查防火墙设置

## 目录结构

- `/app` - 主应用代码
  - `/templates` - HTML 模板
  - `/static` - 静态文件
  - `/services` - 服务模块
- `/uploads` - 上传的文件
- `/instance` - 实例特定文件
