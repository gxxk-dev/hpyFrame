# HPYF-PluginMgr 2025 Gxxk
# 插件管理器.
# 本模块是hPyFrame(HPYF)的一部分.
# HPYF是自由软件，按照AGPL v3+进行许可.
# AGPL v3+(指 AGPL V3-or-later):https://www.gnu.org/licenses/agpl.txt
from collections import namedtuple
import json

def AddPlugin():
    ...

def RemovePlugin():
    ...

def BuildPluginCache(cachePath:str="/HPYF/userData/pluginIndex.json"):
    """
    构建用户插件索引并保存到指定位置

    arg:
        cache
    """
    ...

def DependencyProcess(dependencyList:list):
    """
    调整sys.path等参数使Plugin运行时可导入所需模块
    
    arg:
        dependencyList (list):依赖列表 应当给出每个插件的对应版本与ID
    """
    ...