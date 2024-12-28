from setuptools import setup, find_packages
with open("/Users/baizhe/PycharmProjects/smscli/readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="smsctl",  # 你的项目名称，例如 "sms-cli"
    version="1.0.6",  # 版本号，遵循语义化版本规范
    author="Allen Y",  # 你的名字或组织名称
    author_email="yinhaozheng77625961@gmail.com",  # 你的邮箱
    description="smsctl is a CLI for streamlined SMS management. It provides commands for managing projects, devices, tasks, groups, and chat records, letting you send, receive, and track SMS from one place. Designed for flexible workflows, it handles everything from bulk tasks to conversation monitoring.",  # 项目的简短描述
    long_description=long_description,  # 长描述，通常从 README.md 文件读取
    long_description_content_type="text/markdown",  # 长描述的格式
    url="https://github.com/haozheng95/smscli",  # 项目的GitHub仓库地址
    packages=find_packages(),  # 自动查找项目中的所有包
    classifiers=[  # 分类器，用于在 PyPI 上更好地分类你的项目
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # 选择合适的许可证
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Python 版本要求
    install_requires=[  # 项目依赖的第三方库
        "requests>=2.28.1",
        "certifi>=2024.12.14",
        "charset-normalizer>=3.4.0",
        "click>=8.1.7",
        "idna>=3.10",
        "packaging>=24.2",
        "prettytable>=3.12.0",
        "pyproject_hooks>=1.2.0",
        "tomli>=2.2.1",
        "urllib3>=2.2.3",
        "Faker>=33.1.0"
    ],
    entry_points={  # 配置命令行入口
        'console_scripts': [
            'smsctl=core.command_handler:sms_cli',  # 例如 'sms-cli=main:main'，其中 main 是 main.py 文件中的主函数
        ],
    },
    include_package_data=True,
)