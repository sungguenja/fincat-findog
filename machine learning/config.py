import argparse

# Req. 2-1	Config.py 파일 생성
parser = argparse.ArgumentParser(description='Process some dataset.')
# 캡션 데이터가 있는 파일 경로 (예시)
parser.add_argument('--caption_file_path', type=str, default='.\\datasets\\captions.csv')

# 이미지 데이터가 있는 파일 경로
parser.add_argument('--image_folder_path', '-i', type=str, default='..\\images', help='string for image folder path')

# 테스트 데이터셋의 비율 설정
parser.add_argument('--percent_test_dataset', '-p', type=float, default=0.2, help='float for percent of test dataset')

# 불러오고자 하는 데이터셋 종류 (train data, test data)
parser.add_argument('--type_dataset', '-t', type=str, choices=['train', 'test'], default='test', help='choice "train" or "test" for loading dataset')

# 샘플링 여부
parser.add_argument('--sampling_requirment', '-s', type=bool, default=True, help='boolean for whether to sampling')

# 샘플 데이터 비율
parser.add_argument('--sample_data_ratio', '-r', type=float, default=0.01, help='floating point for sample data ratio')

# parse_args() 메소드를 사용해 주어진 인자를 args 라는 이름으로 파싱
args = parser.parse_args()

# 샘플링 여부
def do_sampling():
    return args.sampling_requirment