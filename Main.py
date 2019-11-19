import subprocess
import objviewer
import theFirstOfCV as cv

# Blueprint Generator from 3D object
# version 0.0.4a
# by. 김성욱 a.k.a pangin as College Student
# in memory #수리_들어간다!

logo = "LOGO:NULL"

intro = "3D 객체 2D 도면화 소프트웨어 프로토타입입니다. 소프트웨어가 위치한 경로 상의 ./input/ 폴더를 찾아 안에 obj 파일과 mtl 파일을 넣어주시고, 파일 이름을 확장자와 같이 입력해주신 다음, 엔터 키를 입력해주세요."
wait = "잠시만 기다려주세요."
prompt_message_4_cv = "도면 생성 전 분석을 위해 생성된 이미지 파일을 소프트웨어가 위치한 경로 상의 ./tmp/png/ 폴더를 찾아 안에 png 형식으로 넣어주시고, 파일 이름을 확장자와 같이 입력해주신 다음, 엔터 키를 입력해주세요."
prompt_message_4_vertorize = "도면 생성을 위해 분석된 결과 이미지 파일을 소프트웨어가 위치한 경로 상의 ./tmp/before_vectorize/bmp/ 폴더를 찾아 bmp 형식으로 넣어주시고, 파일 이름을 확장자와 같이 입력해주신 다음, 엔터 키를 입력해주세요."

before_invert = "./tmp/before_vectorize/tmp.png"
after_invert = "./tmp/before_vectorize_inverted/png/tmp.png"

print(logo)
#obj_filename = "./input/" + input(intro)
# screenshot_name = "./tmp/tmp"
print(wait)

#objviewer.run_objviewer(obj_filename)

png_filename = "./tmp/png/" + input(prompt_message_4_cv)
# png_filename = "./tmp/png/tmp.png"
cv.run_openCV(png_filename)

file_name_4_vectorize = "./tmp/before_vectorize_inverted/bmp/" + input(prompt_message_4_vertorize)
# subprocess.check_output(["potrace", "-i", "-s", file_name_4_vectorize, "-n", "-o", "./tmp/vectorized/output.svg"])
# autotrace -centerline -color-count 2 -output-file output.svg -output-format SVG input.png
subprocess.check_output(["autotrace", "-centerline", "-color-count", "2", "-output-file", "./tmp/vectorized/output.svg", "-output-format", "SVG", file_name_4_vectorize])