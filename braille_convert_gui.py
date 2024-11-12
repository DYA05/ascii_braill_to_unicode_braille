import tkinter as tk
from tkinter import font
import os

# BRL to uni 맵핑값
mapping1 = {
' ': ' ',
'!': '⠮',
'"': '⠐',
'#': '⠼',
'$': '⠫',
'%': '⠩',
'&': '⠯',
"'": '⠄',
'(': '⠷',
')': '⠾',
'*': '⠡',
'+': '⠬',
',': '⠠',
'-': '⠤',
'.': '⠨',
'/': '⠌',
'0': '⠴',
'1': '⠂',
'2': '⠆',
'3': '⠒',
'4': '⠲',
'5': '⠢',
'6': '⠖',
'7': '⠶',
'8': '⠦',
'9': '⠔',
':': '⠱',
';': '⠰',
'<': '⠣',
'=': '⠿',
'>': '⠜',
'?': '⠹',
'@': '⠈',
'A': '⠁',
'B': '⠃',
'C': '⠉',
'D': '⠙',
'E': '⠑',
'F': '⠋',
'G': '⠛',
'H': '⠓',
'I': '⠊',
'J': '⠚',
'K': '⠅',
'L': '⠇',
'M': '⠍',
'N': '⠝',
'O': '⠕',
'P': '⠏',
'Q': '⠟',
'R': '⠗',
'S': '⠎',
'T': '⠞',
'U': '⠥',
'V': '⠧',
'W': '⠺',
'X': '⠭',
'Y': '⠽',
'Z': '⠵',
'[': '⠪',
'\\': '⠳',
']': '⠻',
'^': '⠘',
'_': '⠸',
'`': '⠈',
'a': '⠁',
'b': '⠃',
'c': '⠉',
'd': '⠙',
'e': '⠑',
'f': '⠋',
'g': '⠛',
'h': '⠓',
'i': '⠊',
'j': '⠚',
'k': '⠅',
'l': '⠇',
'm': '⠍',
'n': '⠝',
'o': '⠕',
'p': '⠏',
'q': '⠟',
'r': '⠗',
's': '⠎',
't': '⠞',
'u': '⠥',
'v': '⠧',
'w': '⠺',
'x': '⠭',
'y': '⠽',
'z': '⠵',
'{': '⠪',
'|': '⠳',
'}': '⠻',
'~': '⠘',
'\n': '\n', #줄바꿈
'\t': '\t', #tab
}

# 점자 규정 to uni 매핑값
mapping2 = {
' ': ' ',
'!': '⠮',
'"': '⠐',
'#': '⠼',
'$': '⠫',
'%': '⠩',
'&': '⠯',
"'": '⠄',
'(': '⠷',
')': '⠾',
'*': '⠡',
'+': '⠬',
',': '⠠',
'-': '⠤',
'.': '⠨',
'/': '⠌',
'0': '⠴',
'1': '⠂',
'2': '⠆',
'3': '⠒',
'4': '⠲',
'5': '⠢',
'6': '⠖',
'7': '⠶',
'8': '⠦',
'9': '⠔',
':': '⠱',
';': '⠰',
'<': '⠣',
'=': '⠿',
'>': '⠜',
'?': '⠹',
'@': '⠈',
'A': '⠁',
'B': '⠃',
'C': '⠉',
'D': '⠙',
'E': '⠑',
'F': '⠋',
'G': '⠛',
'H': '⠓',
'I': '⠊',
'J': '⠚',
'K': '⠅',
'L': '⠇',
'M': '⠍',
'N': '⠝',
'O': '⠕',
'P': '⠏',
'Q': '⠟',
'R': '⠗',
'S': '⠎',
'T': '⠞',
'U': '⠥',
'V': '⠧',
'W': '⠺',
'X': '⠭',
'Y': '⠽',
'Z': '⠵',
'[': '⠪',
'\\': '⠳',
']': '⠻',
'^': '⠘',
'_': '⠸',
'`': ' ',
'a': '⠁',
'b': '⠃',
'c': '⠉',
'd': '⠙',
'e': '⠑',
'f': '⠋',
'g': '⠛',
'h': '⠓',
'i': '⠊',
'j': '⠚',
'k': '⠅',
'l': '⠇',
'm': '⠍',
'n': '⠝',
'o': '⠕',
'p': '⠏',
'q': '⠟',
'r': '⠗',
's': '⠎',
't': '⠞',
'u': '⠥',
'v': '⠧',
'w': '⠺',
'x': '⠭',
'y': '⠽',
'z': '⠵',
'{': '⠪',
'|': '⠳',
'}': '⠻',
'~': '⠘',
'\n': '\n', #줄바꿈
'\t': '\t', #tab
}


# 메인 윈도우 생성 (폰트 설정 이전에 먼저 해야 함)
root = tk.Tk()
root.title("점자폰트 to 유니코드 1.1")

# 동작방식 선택 함수
selected_mode = tk.StringVar()
selected_mode.set('BRL') #기본값

def uni_convert(text):
    str_list = list(text)
    conv = []
    for i in str_list:
        if i in mapping1.keys():
            if selected_mode.get() == 'BRL':
                conv.append(mapping1[i])
            elif selected_mode.get() == '점자규정집':
                conv.append(mapping2[i])   
        else:
            conv.append('?')
    s = ''.join(conv)
    return(s)

def on_input(event):
    # 1번 텍스트박스에서 입력된 텍스트
    input_text = text_box1.get("1.0", "end-1c")
    
    # 2번 텍스트박스에 변경된 폰트로 텍스트 표시
    text_box2.config(state=tk.NORMAL)
    text_box2.delete("1.0", tk.END)
    text_box2.insert(tk.END, input_text)
    text_box2.config(state=tk.DISABLED)
    
    
    # 3번 텍스트박스에 변환된 텍스트 표시 (커스텀 변환 방식 적용)
    transformed_text = uni_convert(input_text)
    text_box3.config(state=tk.NORMAL)
    text_box3.delete("1.0", tk.END)
    text_box3.insert(tk.END, transformed_text)
    text_box3.config(state=tk.DISABLED)

def on_button():
    # 1번 텍스트박스에서 입력된 텍스트
    input_text = text_box1.get("1.0", "end-1c")
    
    # 2번 텍스트박스에 변경된 폰트로 텍스트 표시
    text_box2.config(state=tk.NORMAL)
    text_box2.delete("1.0", tk.END)
    text_box2.insert(tk.END, input_text)
    text_box2.config(state=tk.DISABLED)
    
    # 3번 텍스트박스에 변환된 텍스트 표시 (커스텀 변환 방식 적용)
    transformed_text = uni_convert(input_text)
    text_box3.config(state=tk.NORMAL)
    text_box3.delete("1.0", tk.END)
    text_box3.insert(tk.END, transformed_text)
    text_box3.config(state=tk.DISABLED)

def clear_text_box1():
    text_box1.delete("1.0", tk.END)
    on_button()

def paste_from_clipboard():
    clipboard_text = root.clipboard_get()
    text_box1.insert(tk.END, clipboard_text)
    on_button()

def copy_to_clipboard():
    text = text_box3.get("1.0", "end-1c")
    root.clipboard_clear()  # 클립보드 내용 지우기
    root.clipboard_append(text)  # 클립보드에 텍스트 추가
    root.update()  # 클립보드 업데이트
    on_button()



# 기본창 크기 설정
root.geometry("670x600")  # 예를 들어 800x600 픽셀로 설정

# 외부 폰트 파일 경로 지정
# 시스템에 설치된 폰트 이름을 사용
font1 = font.Font(family="SimBraille", size=20)
font2 = font.Font(family="D2coding", size=12)
font3 = font.Font(family="D2coding", size=20)

# 상단 메뉴바 생성
menu_bar = tk.Menu(root)
# 동작 메뉴 생성
mode_menu = tk.Menu(menu_bar, tearoff=0)

# 라디오 버튼으로 동작 방식 선택
mode_menu.add_radiobutton(label="BRL to unicode", variable=selected_mode, value="BRL", command=on_button)
mode_menu.add_radiobutton(label="점자규정집 to unicode", variable=selected_mode, value="점자규정집", command=on_button)
# 메뉴바에 동작 메뉴 추가
menu_bar.add_cascade(label="동작 방식", menu=mode_menu)

# 메뉴바 추가
root.config(menu=menu_bar)




# 버튼 프레임을 최상단에 추가
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

# 지우기 버튼
clear_button = tk.Button(button_frame, text="입력 내용 지우기", command=clear_text_box1, height=2, width=20)
clear_button.pack(side=tk.LEFT, padx=20, expand=True)  # 버튼 사이 간격을 padx로 조정

# 붙여넣기 버튼
paste_button = tk.Button(button_frame, text="클립보드에서 붙여넣기", command=paste_from_clipboard, height=2, width=20)
paste_button.pack(side=tk.LEFT, padx=20, expand=True)  # 동일한 간격

# 클립보드 복사 버튼
copy_button = tk.Button(button_frame, text="변환 값 클립보드에 복사", command=copy_to_clipboard, height=2, width=20)
copy_button.pack(side=tk.LEFT, padx=20, expand=True)  # 동일한 간격


# 첫 번째 텍스트 박스 (입력 가능)
label1 = tk.Label(root, text="점자 입력(점자폰트)", font=("Arial", 12))
label1.pack()

frame1 = tk.Frame(root)
frame1.pack(fill=tk.BOTH, expand=True)

scrollbar1 = tk.Scrollbar(frame1)
scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)

text_box1 = tk.Text(frame1, height=5, font=font1, wrap=tk.NONE, yscrollcommand=scrollbar1.set)
text_box1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar1.config(command=text_box1.yview)
text_box1.bind("<KeyRelease>", on_input)  # 입력/수정시 자동 실행



# 두 번째 텍스트 박스 (입력된 텍스트 출력, 폰트 변경)
label2 = tk.Label(root, text="입력값 유니코드 출력", font=("Arial", 12))
label2.pack()

frame2 = tk.Frame(root)
frame2.pack(fill=tk.BOTH, expand=True)

scrollbar2 = tk.Scrollbar(frame2)
scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)

text_box2 = tk.Text(frame2, height=3, font=font2, wrap=tk.NONE, state=tk.DISABLED, yscrollcommand=scrollbar2.set)
text_box2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar2.config(command=text_box2.yview)

# 세 번째 텍스트 박스 (변환된 텍스트 출력, 폰트 변경)
label3 = tk.Label(root, text="점자 변환(유니코드)", font=("Arial", 12))
label3.pack()

frame3 = tk.Frame(root)
frame3.pack(fill=tk.BOTH, expand=True)

scrollbar3 = tk.Scrollbar(frame3)
scrollbar3.pack(side=tk.RIGHT, fill=tk.Y)

text_box3 = tk.Text(frame3, height=5, font=font3, wrap=tk.NONE, state=tk.DISABLED, yscrollcommand=scrollbar3.set)
text_box3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar3.config(command=text_box3.yview)

# GUI 실행
root.mainloop()                  