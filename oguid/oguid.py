"""
OGU ID-email converter
"""
import re

def email_to_caddie(email: str) -> str:
    """
    24e9999@ogu.ac.jp -> 24E9999
    """
    # "@" 以降を削除
    substring_before_at = email.split('@')[0]

    # 大文字に変換
    result = substring_before_at.upper()
    return result


def email_to_webservice(email: str) -> str:
    """
    24e9999@ogu.ac.jp -> 2024E 9999    
    """
    result = email_to_caddie(email)
    return caddie_to_webservice(result)


def caddie_to_webservice(id: str) -> str:
    """
    24E9999 -> 2024E 9999
    """
    return _add_space("20" + id)


def caddie_to_email(id: str) -> str:
    """
    24E9999 -> 24e9999@ogu.ac.jp
    """
    return id.lower() + "@ogu.ac.jp"


def webservice_to_caddie(id: str) -> str:
    """
    2024E 9999 -> 24E9999
    """
    return id.replace(" ", "")[2:]


def webservice_to_email(id: str) -> str:
    result = webservice_to_caddie(id)
    return caddie_to_email(result)


def _add_space(input_str: str) -> str:
    # 正規表現を使用して、英字と数字の間に半角スペースを挿入
    result_str = re.sub(r'([a-zA-Z]+)(\d+)', r'\1 \2', input_str)
    return result_str