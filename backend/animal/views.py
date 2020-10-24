from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Animal_Picture
from drf_yasg.utils import swagger_auto_schema
# api 관련 함수는 200번째 줄부터
# Create your views here.
# tensorflow and ML package
from tensorflow.compat.v2.keras.models import model_from_json
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random
import os
from sklearn.datasets import load_files       
from keras.utils import np_utils
from glob import glob
import json
from tensorflow.config import experimental

gpus = experimental.list_physical_devices('GPU')
if gpus:
    try:
    # Currently, memory growth needs to be the same across GPUs
        for gpu in gpus:
            experimental.set_memory_growth(gpu, True)
        logical_gpus = experimental.list_logical_devices('GPU')
        print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
    except RuntimeError as e:
        # Memory growth must be set before GPUs have been initialized
        print(e)
# 글로벌 변수 선언
FAST_RUN = False
IMAGE_WIDTH = 128
IMAGE_HEIGHT = 128
IMAGE_SIZE = (IMAGE_WIDTH,IMAGE_HEIGHT)
IMAGE_CHANNELS = 3 # 컬러 사진이므로 채널이 3(rgb)
batch_size = 15

# json 파일 열기
module_dir = os.path.dirname(__file__)
json_file = open(module_dir+'/CNN_dog_cat_model.json','r')
loaded_model_json = json_file.read()
json_file.close()

# json 파일로부터 model 로드하기
loaded_model = model_from_json(loaded_model_json)

# 로드한 model에 weight 로드하기
loaded_model.load_weights(module_dir+'/CNN_dog_cat_model.h5')
loaded_model.compile(optimizer='adam',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

def is_dog_cat(filename):
    file_dir = module_dir[:-6]
    file_dir += 'media\\images\\'
    filename = [str(filename)]
    file_df = pd.DataFrame({
        'filename':filename
    })
    nb_samples = file_df.shape[0]

    file_gen = ImageDataGenerator(rescale=1./255)
    file_generator = file_gen.flow_from_dataframe(
        file_df,
        file_dir,
        x_col='filename',
        y_col=None,
        target_size=IMAGE_SIZE,
        class_mode=None,
        batch_size=batch_size,
        shuffle=False
    )
    # 모델 예측
    predict = loaded_model.predict_generator(file_generator,steps=np.ceil(nb_samples/batch_size))

    # 평가
    file_df['category'] = np.argmax(predict,axis=-1)

    file_df['category'] = file_df['category'].replace({1:'dog',0:'cat'})

    now_file = file_df.head(18)
    dog_or_cat = now_file.head()['category']
    dog_or_cat = dog_or_cat[0]
    breed = None
    if dog_or_cat == 'dog':
        breed = what_dog_breed(filename)
    elif dog_or_cat == 'cat':
        breed = what_cat_breed(filename)
    return dog_or_cat,breed

# json 파일 열기-v2
json_file = open(module_dir+'/CNN_dog_breed_model_v2.json','r')
loaded_model_json = json_file.read()
json_file.close()

# json 파일로부터 model 로드하기
dog_model = model_from_json(loaded_model_json)

# 로드한 model에 weight 로드하기
dog_model.load_weights(module_dir+'/CNN_dog_breed_model_v2.h5')

# 강아지 고양이 종 구분을 위한 함수
from keras.preprocessing import image                  
from tqdm import tqdm
from PIL import ImageFile                            
ImageFile.LOAD_TRUNCATED_IMAGES = True   
from keras.callbacks import ModelCheckpoint  

EPOCHS = 10
dog_model.compile(loss='categorical_crossentropy', optimizer="rmsprop", metrics=['accuracy'])
checkpointer = ModelCheckpoint(filepath='saved_models/bestmodel.hdf5', 
                               verbose=1, save_best_only=True)
def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)

def paths_to_tensor(img_paths):
    list_of_tensors = [path_to_tensor(img_path) for img_path in tqdm(img_paths)]
    return np.vstack(list_of_tensors)

from keras.applications.vgg19 import VGG19
from keras.applications.vgg19 import preprocess_input as preprocess_input_vgg19
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input as preprocess_input_resnet50

def extract_VGG19(file_paths):
    tensors = paths_to_tensor(file_paths).astype('float32')
    preprocessed_input = preprocess_input_vgg19(tensors)
    return VGG19(weights='imagenet', include_top=False).predict(preprocessed_input, batch_size=32)

def extract_Resnet50(file_paths):
    tensors = paths_to_tensor(file_paths).astype('float32')
    preprocessed_input = preprocess_input_resnet50(tensors)
    return ResNet50(weights='imagenet', include_top=False).predict(preprocessed_input, batch_size=32)

def what_dog_breed(filename):
    file_dir = module_dir[:-6]
    file_dir += 'media\\images\\' + filename[0]
    predict = dog_model.predict([extract_VGG19([file_dir]),extract_Resnet50([file_dir])])
    predict = np.argmax(predict)
    dog = {0:'아펜핀셔',1:'아프간 하운드',2:'에어데일 테리어',3:'아키타견',4:'알레스칸 말라뮤트',
    5:'아메리칸 에스키모',6:'아메리칸 폭스하운드',7:'아메리칸 스태퍼드셔 테리어',
    8:'아메리칸 워터 스패니얼',9:'아나톨리아 셰퍼드',10:'오스트레일리안 캐틀독',
    11:'오스트레일리언 셰퍼드',12:'오스트레일리안 테리어',13:'바센지',
    14:'바셋하운드',15:'비글',16:'비어디드 콜리',17:'보스롱',18:'베들링턴 테리어',
    19:'말리노이즈',20:'벨지안 셰퍼드',21:'벨기에 테뷰런',22:'버니즈 마운틴 도그',
    23:'비숑 프리제',24:'블랙 앤 탄 쿤하운드',25:'블랙 러시안 테리어',26:'블러드 하운드',
    27:'블루틱 쿤하운드',28:'보더 콜리',29:'보더 테리어',30:'보르조이',31:'보스턴 테리어',
    32:'부비에 데 플랑드르',33:'복서',34:'보이킨 스패니얼',35:'브리아드',36:'브리트니',
    37:'브뤼셀 그리펀',38:'불 테리어',39:'불독',40:'불마스티프',41:'케언 테리어',42:'케이넌 도그',
    43:'카네코르소',44:'카디건 웰시 코기',45:'카발리에 킹 찰스 스패니얼',46:'체서피크 베이 리트리버',
    47:'치와와',48:'차이니스 크레스티드',49:'샤페이',50:'차우차우',51:'클럼버 스파니엘',52:'코카 스파니엘',
    53:'콜리',54:'컬리 코티드 리트리버',55:'닥스훈트',56:'달마시안',57:'댄디 딘몬트 테리어',
    58:'도베르만 핀셔',59:'도그 드 보르도',60:'잉글리시 코커 스패니얼',61:'르웰린',
    62:'잉글리시 스프링어 스패니얼',63:'킹 찰스 스패니얼',64:'엔틀버쳐 마운틴 독',65:'필드 스패니얼',
    66:'피니시 스피츠',67:'플랫 코티드 리트리버',68:'프렌치 불도그',69:'저먼 핀셔',
    70:'저먼 셰퍼드',71:'저먼 쇼트헤어드 포인터',72:'저먼 와이어헤어드 포인터',73:'자이언트 슈나우저',
    74:'글렌 오브 이말 테리어',75:'골든 리트리버',76:'고든 세터',77:'그레이트 데인',
    78:'그레이트 피레니즈',79:'그레이터 스위스 마운틴 도그',80:'그레이하운드',81:'하바나 실크 독',
    82:'이비전 하운드',83:'아이슬랜드 시프도그',84:'아이리시 레드 앤드 화이트 세터',85:'아이리시 세터',
    86:'아이리시 테리어',87:'아이리시 워터 스패니얼',88:'아이리시 울프하운드',
    89:'이탈리안 그레이하운드',90:'제페니스 친',91:'키스혼드',92:'케리 블루 테리어',
    93:'코몬돌',94:'쿠바츠',95:'레브라도 리트리버',96:'레이클랜드 테리어',97:'레온베르거',
    98:'라사압소',99:'로첸',100:'말티즈',101:'맨체스터 테리어',102:'잉글리쉬 마스티프',
    103:'미니어처 슈나우저',104:'나폴리탄 마스티프',105:'뉴펀들랜드',
    106:'노퍽 테리어',107:'노르웨이안 부훈트',108:'노르웨이언 엘크하운드',109:'노르웨이 룬트훈트',
    110:'노리치 테리어',111:'노바 스코셔 덕 톨링 레트리버',112:'올드 잉글리시 쉽독',113:'오터 하운드',
    114:'빠삐용',115:'파슨 러셀 테리어',116:'페키니즈',117:'펨브록 웰시 코기',
    118:'프티 바세 그리퐁 방댕',119:'파라오 하운드',120:'플롯 하운드',121:'포인터',
    122:'포메라니안',123:'푸들',124:'포르투갈 워터 독',125:'세인트 버나드',126:'오스트레일리안 실키 테리어',
    127:'스무스 폭스 테리어',128:'티베탄 마스티프',129:'웰시 스프링어 스패니얼',
    130:'와이어헤어드 포인팅 그리폰',131:'멕시칸 헤어리스 도그',132:'요크셔 테리어'}
    return dog[predict]

# json 파일 열기-v2
json_file = open(module_dir+'/CNN_cats_breed_model.json','r')
loaded_model_json = json_file.read()
json_file.close()

# json 파일로부터 model 로드하기
cat_model = model_from_json(loaded_model_json)

# 로드한 model에 weight 로드하기
cat_model.load_weights(module_dir+'/CNN_cats_breed_model.h5')

EPOCHS = 10
cat_model.compile(loss='categorical_crossentropy', optimizer="rmsprop", metrics=['accuracy'])
checkpointer = ModelCheckpoint(filepath='saved_models/bestmodel.hdf5', 
                               verbose=1, save_best_only=True)

def what_cat_breed(filename):
    file_dir = module_dir[:-6]
    file_dir += 'media\\images\\' + filename[0]
    predict = cat_model.predict([extract_VGG19([file_dir]),extract_Resnet50([file_dir])])
    predict = np.argmax(predict)
    cat = {0:'아비시니안',1:'아메리칸 밥테일',2:'아메리칸 컬',3:'아메리칸 쇼트헤어',4:'아메리칸 와이어헤어',
    5:'타이캣',6:'발리니즈',7:'벵골',8:'버먼',9:'봄베이고양이',10:'브리티시 쇼트헤어',11:'버마고양이',
    12:'버밀라',13:'삼색털 고양이',14:'스핑크스',15:'샤르트뢰',16:'쵸시',17:'친칠라',18:'코니시 렉스',
    19:'킴릭',20:'데본렉스',21:'딜루트 칼리코',22:'딜루트 토터셀',23:'도메스틱 롱 헤어',24:'도메스틱 미디움 헤어',
    25:'도메스틱 쇼트 헤어',26:'이집션 마우',27:'엑조틱 쇼트헤어',28:'엑스트라 토즈',29:'하바나',30:'히말라얀',
    31:'재패니즈밥테일',32:'자바니즈',33:'코랏',34:'라팜',35:'메인쿤',36:'맹크스',37:'먼치킨',38:'네벨룽',39:'노르웨이 숲고양이',
    40:'오시캣',41:'오리엔탈 롱헤어',42:'오리엔탈 숏헤어',43:'오리엔탈 테비',44:'페르시안',45:'픽시 밥',46:'라가머핀',
    47:'래그돌',48:'러시안 블루',49:'스코티쉬 폴드',50:'셀커크 렉스',51:'시암고양이',52:'시베리안 고양이',53:'실버 캣',
    54:'싱가푸라',55:'스노우슈',56:'소말리 고양이',57:'스핑크스',58:'얼룩 고양이',59:'호랑고양이',60:'톤키니즈',
    61:'얼룩 고양이',62:'톨 토이즈셀',63:'터키시 앙고라',64:'터키시 반',65:'턱시도 고양이',66:'요크 쇼콜라'}
    return cat[predict]

@swagger_auto_schema()
@api_view(['GET'])
def what_is_this(request,picture_pk):
    """
        동물 사진의 pk를 보내면
        어떤 동물인지와 종까지 알려줌
    """
    picture = get_object_or_404(Animal_Picture,pk=picture_pk)
    filename = str(picture.picture).split('/')[-1]
    animal,breed = is_dog_cat(filename)
    data = {'animal':animal,'breed':breed,'pk':picture_pk,'img_path':str(picture.picture)}
    return HttpResponse(json.dumps(data,ensure_ascii=False),content_type='application/json')