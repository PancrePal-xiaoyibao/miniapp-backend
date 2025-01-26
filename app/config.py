import json
import os
from pathlib import Path

class Config:
    def __init__(self):
        self.config_path = Path(__file__).parent / 'config.json'
        self.load_config()

    def load_config(self):
        """加载配置文件"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self._config = json.load(f)
        except Exception as e:
            raise Exception(f'加载配置文件失败: {str(e)}')

    @property
    def database(self):
        """数据库配置"""
        return self._config['database']

    @property
    def fastgpt(self):
        """FastGPT配置"""
        return self._config['fastgpt']

    @property
    def tencent_cloud(self):
        """腾讯云配置"""
        return self._config['tencent_cloud']

    @property
    def sealos(self):
        """Sealos配置"""
        return self._config['sealos']

    @property
    def server(self):
        """服务器配置"""
        return self._config['server']

    @property
    def security(self):
        """安全配置"""
        return self._config['security']

# 创建全局配置实例
config = Config()