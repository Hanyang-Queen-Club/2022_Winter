# Text Summarization with Pretrained Encoder
## 0. Background
### Extractive VS. Abstractive
<img width="600" alt="image" src="https://user-images.githubusercontent.com/32005272/212538267-7d2d0faf-a4b1-49d3-b197-bc8e84c6346a.png">
**Extractive**
- 문서에서 가장 중요한 문장을 식별하여 수행 -> sentence classification으로 수행

**Abstractive**
- Encoder : source 문서 $x=[x_1,...,x_n]$ -> continuous representation $z=[z_1,...,z_n]$
- Decoder : $z \rightarrow y=[y_1,...y_m]$을 token-by-token으로 생성(auto-regressive)
$$p(y_1,...,y_m|x_1,...,x_n)$$

## 1.Introduction
Pretrained Language Model (PLM)은 Paragraph-Level NLU 문제들을 해결하는데 Encoder로 사용됨  
Text 요약에서 PLM의 영향을 실험
### Contribution
- Extractive & Abstractive 요약에서 **General Framework**가 PLM(BERT)의 잠재성 알아보기
- Extractive와 Abstractive 합치면 더 좋은 요약 생성
- **Two-stage Approach : Encoder Fine-tune 2번**
  1. Extractive
  2. Abstractive

## 2. Fine-tuning BERT for Summarization
### Summarization Encoder
<img width="790" alt="image" src="https://user-images.githubusercontent.com/32005272/212538721-2d74e44f-ea3b-407c-a727-731c42271938.png">

- 요약에선 다중 문장 입력을 encoding 하고 조작해야 함
- 개별 문장 표현 위해 추가 [CLS] 토큰을 각 문장 앞에 삽입 ... 각 [CLS] 토큰은 앞 문장 feature에 대해 수집
- **Interval Segment Embedding**을 사용하여 문서 내의 여러 문장 구별
  - $sent_i$마다 Segment Embedding &E_A$ 또는 $E_B$ 할당 ... $i$가 홀수인지 짝수인지에 따라
  $$[sent_1, sent_2, sent_3, sent_4, sent_5]$$
  $$[E_A, E_B, E_A, E_B, E_A]$$
  
### Extractive Summarization
- $[sent_1,...,sent_m] \in d$, $d$ : document
- $y_i \in \{0,1\} \rightarrow sent_i$가 summary에 포함되는 문장인지

BERTSUM
**Inter-sentence Transformer Layer**
- $t_i$ : top layer의 $i$번째 [CLS] 토큰 벡터,
  - $sent_i$의 representation으로 사용
  - $h_0 = PosEmb(T)$, $T$: BERTSUM에서 나온 sentence vector
![image](https://user-images.githubusercontent.com/32005272/212539442-851f162a-fb96-4ba7-9b3e-13d854718c17.png)


  $$\tilde{h}^l = LN(h^{l-1} + MHAtt(h^{l-1})$$
  $$h^l = LN(\tilde{h}^l + FFN(\tilde{h}^l)$$
  $$\hat{y_i}=\sigma (W_O h_i^l + b_O)$$

- $h_i^L$ : $sent_i$의 벡터, ( $L$번째(top) layer)
- $L=1,2,3$ 중 $L=2$가 best
- Binary Classification entropy loss( $\hat{y_i}$, $y_i$ )

### Abstractive Summarization
- Encoder : Pre-trained BERTSUM
- Decoder : 랜덤하게 초기화한 6-layered Transformer

- Encoder는 Pre-trained, Decoder는 Pre-train 아니라 Encoder, Decoder 간 불일치
- fine-tuning 불안정 - encoder는 overfitting, decoder는 underfitting
- **optimizer 분리**
  - Adam optimizers 
    - Encoder : ${\beta}_1 = 0.9$
    - Decoder : ${\beta}_2 = 0.999$  
  - 서로 다른 warmup step과 learning rate
    - $lr_\mathcal{E} = \tilde{lr_\mathcal{E}} \cdot min(step^{-0.5}, step \cdot warmup_{\mathcal{E}}^{-1.5})$
    - $lr_\mathcal{D} = \tilde{lr_\mathcal{D}} \cdot min(step^{-0.5}, step \cdot warmup_{\mathcal{D}}^{-1.5})$
  - Encoder는 정확한 gradient와 학습 가능, Decoder는 안정적으로 학습 가능
- **Two-stage fine-tuning**
  1. Encoder를 Extractive 요약 task로 fine-tune
  2. 그 다음 Abstractive 요약 task로 fine-tune

----
Default Abstractive Model : $BERTSUMABS$  
Two-stage Fine-tuned Model : $BERTSUMEXTABS$
