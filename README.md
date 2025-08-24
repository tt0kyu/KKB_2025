KKB 2025 입사 과제

📋 프로젝트 개요

본 프로젝트는 KKB 2025년 신입 개발자 채용을 위한 기술 과제입니다.



🛠️ 기술 스택



Language: Python 3.11

Libraries:

&nbsp;- cryptography (암호화/복호화)





💡 구현 내용

주요 기능

&nbsp;- AES-GCM 복호화 구현

&nbsp;- Go로 작성된 암호화 코드 분석

&nbsp;- Python으로 호환되는 복호화 로직 구현



💡 핵심 알고리즘

Cryptography 라이브러리 AEAD 문서를 참고하여 구현했습니다.

python# AES-GCM 복호화 핵심 로직

def decrypt(data, key):

&nbsp;   """

&nbsp;   AES-GCM으로 암호화된 데이터를 복호화합니다.

&nbsp;   

&nbsp;   Args:

&nbsp;       data (bytes): 암호화된 데이터 (nonce + ciphertext)

&nbsp;       key (bytes): 복호화 키

&nbsp;   

&nbsp;   Returns:

&nbsp;       bytes: 복호화된 평문

&nbsp;   

&nbsp;   Reference:

&nbsp;       - https://cryptography.io/en/latest/hazmat/primitives/aead/

&nbsp;   """

&nbsp;   cipher = AESGCM(key)

&nbsp;   nonce = data\[:12]        # AES-GCM 표준 nonce 크기 (96-bit)

&nbsp;   ciphertext = data\[12:]   # 실제 암호화된 데이터

&nbsp;   plaintext = cipher.decrypt(nonce, ciphertext, None)

&nbsp;   return plaintext



