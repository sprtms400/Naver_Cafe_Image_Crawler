# 해당 모듈에선 시스템 운용에 필요한 파일들을 파싱하는 함수들을 정의합니다.

def parse_galleries_file(file_path):
    galleries = []  # 결과를 저장할 배열
    try:
        with open(file_path, 'r') as file:  # 파일을 읽기 모드로 열기
            for line in file:  # 파일의 각 줄에 대해 반복
                # 줄바꿈 문자를 제거하고 배열에 추가
                galleries.append(line.strip())
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
    except Exception as e:
        print(f"파일을 읽는 동안 오류가 발생했습니다: {e}")
    return galleries