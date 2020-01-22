# pylint: disable=unused-import
"""
pytest fixture
"""
from gevent import monkey
monkey.patch_all()  # repository 계층에서 사용되는 requests의 충돌문제

