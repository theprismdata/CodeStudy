def caesar_cipher(s, n):
    result = ""
    for char in s:
        if char.isalpha():
            # 알파벳인 경우
            is_upper = char.isupper()
            char = char.lower()
            # 'a'의 아스키 코드 값을 이용하여 알파벳 이동 계산
            move = ord(char) - ord('a')
            move = (move + n) % 26
            result += chr(move + ord('a')) if not is_upper else chr(move + ord('A'))
        else:
            # 알파벳이 아닌 경우 그대로 추가
            result += char
    return result

# 예시 실행
s = "a B z"
n = 4
print(caesar_cipher(s, n))  # 출력: DE