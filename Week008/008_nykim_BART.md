# BART : Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension
Paper : [BART : Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/pdf/1910.13461.pdf)

## Model
BART는 denoising Autoencoder(입력 데이터를 최대한 압축시키고, 압축한 데이터를 다시 본래 입력 형태로 복원시키는 신경망)
- 압축 부분 Encoder, 복원 부분 Decoder
- 압축 과정에서 추출한 의미 있는 데이터를 latent vector(=feature)라고 부름
![image](https://user-images.githubusercontent.com/32005272/215009623-47bd60eb-71ba-45de-90dd-eb7786b43941.png)

Bidirectional Encoder, Left-to-Right Autoregressive Decoder

![image](https://user-images.githubusercontent.com/32005272/215009796-d1c41e8e-5abd-45c5-855f-e3663d3fc858.png)
![image](https://user-images.githubusercontent.com/32005272/215009826-fe0b39dd-22d3-4e04-93ab-0420ab07a329.png)
![image](https://user-images.githubusercontent.com/32005272/215009863-5fb14fc9-f069-4bfc-b6e6-d3cdcdcd0bf3.png)

### 1. Architecture
BERT와의 차이점
1. Decoder의 각 layer는 Encoder의 마지막 hidden layer에서 cross-attention을 수행(Transformer의 Seq2Seq 모델 안에서처럼)
2. BERT는 단어 예측 전 추가 Feed-Forward network를 사용하지만 BART는 사용 안 함.

### 2. Pre-training BART
1. Token Masking
    - BERT에서처럼, 랜덤한 token들이 [MASK]로 대체됨
2. Token Deletion
    - 랜덤한 token들이 삭제됨. masking과 다르게 모델은 input의 삭제된 위치를 알아내야 한다.
3. Text Infilling
    - span 샘플링(포아송 분포 $\lambda=3$)
    - 각 span은 단일 [MASK] 토큰으로 교체, 0 길이의 span들은 [MASK] 토큰을 삽입
    - 모델에게 얼마나 많은 token들이 span에서 없어졌는지 예측하는 것을 배우게 함
4. Sentence Permutation
    - Document는 문장들로 나누어지고 랜덤한 순서로 섞임
5. Document Rotation
    - token은 uniform random하게 골라지고 document는 해당 token으로 시작하기 위해 돌려짐. 이 task는 모델이 document의 시작점을 찾게끔 훈련함

## Fine-tuning BART
### 1. Sequence Classification Tasks
- Encoder와 Decoder에 같은 input
- Decoder의 마지막 token의 마지막 hidden states는 multi-class linear classifier에 input으로 들어감
- BERT의 [CLS] token과 연관 - BART는 Decoder token의 representation이 완전한 input에서 Decoder states와 attend하도록 추가 토큰을 **끝** 부분에 추가함
![image](https://user-images.githubusercontent.com/32005272/215017536-b166e20b-76d6-4b27-9f13-1d0f1dfcc166.png)

### 2. Token Classificaton Tasks
- 완전한 document를 encoder와 decoder에 넣고 decoder의 맨 위 hidden state를 각 단어의 representation으로 사용
- 이 representatoin이 token classification에 사용됨

### 3. Sequence Generation Tasks
- 정보는 input에서 복사되지만 조작됨(denoising pre-training objective와 연관됨)
- Encoder input은 input sequence, Decoder는 output을 Autoregressive하게 생성

### 4. Machine Translation
- BART encoder embedding layer를 새로 랜덤하게 초기화된 encoder로 교체하여 사용
- End-to-End로 학습(새 encoder가 외국 단어를 BART가 영어로 de-noise 가능하도록 input mapping하도록 학습)
- 새 Encoder는 오리지널 BART 모델과 분리된 사전을 사용
- Source Encoder를 two step으로 학습
  - BART 파라미터를 대부분 freeze하고 랜덤하게 초기화된 Source encoder, BART positional embedding, BART encoder의 첫 번째 encoder의 self-attention input projection matrix만 업데이트
  - 모델의 모든 파라미터를 적은 수의 iteration으로 학습

![image](https://user-images.githubusercontent.com/32005272/215019386-6535608a-97e8-4841-8d63-0dfc2b3f2423.png)

# Summarization with BART
