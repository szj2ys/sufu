# *_*coding:utf-8 *_*
import fire
import os


def install_package(pkg):
    os.system(f'pip3 install {pkg} -i https://mirrors.aliyun.com/pypi/simple')


if __name__ == '__main__':
    fire.Fire(install_package)
