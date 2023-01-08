# Knowledge Distillation
논문 : [Distilling the Knowledge in a Neural Network (NIPS 2014)](https://arxiv.org/pdf/1503.02531.pdf)

## Introduction
머신 러닝 모델의 성능을 쉽게 끌어올리는 방법 : 앙상블(Ensemble) 기법
- 동일한 모델 구조에서 initialization을 다르게 하여 여러 번 학습
- 다른 구조 NN을 여러 개 만든 뒤 나오는 결과 평균내거나 합치기

**단점**
- 실제 ensemble된 모델 사용하기에 소모되는 컴퓨팅 파워와 메모리 대비 얻어지는 성능의 효율이 떨어짐

### Contribution
- Ensemble의 generalization 능력을 작은 규모의 single neural network가 전달(transfer) 받기
- 큰 규모의 Neural Network가 지닌 지식(knowledge)를 작은 규모 Neural Network으로 전달하기

## Distillation
- 이 논문에서 지식(knowledge)은 모델이 softmax하여 낸 결과에 포함되어 있다고 봄
- Ensemble 모델의 softmax 결과를 새로운 NN에 잘 전달한다면 기존 큰 규모의 ensemble 모델이 갖고 있는 지식들을 작은 규모의 single NN가 학습에 활용하여 기존과 비슷한 성능을 지닐 수 있다고 함

![softmax](https://i.stack.imgur.com/HYyQT.jpg)
![soft](https://jamiekang.github.io/media/2017-05-21-distilling-the-knowledge-in-a-neural-network-fig1.jpg)

----------------
![model](https://velog.velcdn.com/images%2Fahp2025%2Fpost%2F872cc5ea-f5c7-4b8f-8b54-65ec4a082859%2Fknowledge_distillation.png)
1. 복잡한 모델(Teacher)에 대해서 높은 T로 soft target 만들기 -> soft labels
2. 간단한 모델(student-distilled)에 대해서 같은 T로 soft target 만들기 -> soft predictions
3. 간단한 모델(student-distilled)에 대해서 T=1로 hard target 만들기 -> hard predictions
4. 첫 번째 loss function으로 soft labels와 soft predictions 간의 Cross-Entropy Loss 구함
5. 두 번째 loss function으로 hard predictions와 ground truth 간의 Cross-Entropy Loss 구함
   - transfer set에 대한 정확한 lable을 모델이 알게 하여 성능을 향상 

### Matching logits is a special case of distillation
![matching loss](https://luofanghao.github.io/blog/images/KD3.jpg)
