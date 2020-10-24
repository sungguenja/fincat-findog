# Simple Linear Regression

### Regression

![image-20200908225244679](images/image-20200908225244679.png)

* 전체의 평균으로 되돌아감 (회귀)
* 굉장히 튀는(아주 작거나 아주 큰) 데이터도 결과적으로 전체의 평균으로 되돌아가려는 속성이 있다는 통계적 원리



### Linear Regression

![image-20200908225425846](images/image-20200908225425846.png)

* 데이터를 가장 잘 대변하는 직선의 방정식을 찾는 것 (선형 회귀)
* 파란 점 : 데이터
* 빨간 선 : 데이터들을 가장 잘 대변하는 직선 -> 직선의 기울기와 y절편을 찾는 것이 목표



### Hypothesis

![image-20200908225723771](images/image-20200908225723771.png)

* H(x) : 최적의 직선의 방정식을 찾기 위한 우리의 가설



### Cost

![image-20200908225838600](images/image-20200908225838600.png)

* y : 실제 데이터
* H(x) - y : `cost`/`loss`/`error` -> 이 값이 작을 수록 좋음

![image-20200908230032716](images/image-20200908230032716.png)

* `cost`를 최소화하는 방법
  * `cost`가 양수일 수도, 음수일 수도 있기 때문에 그냥 더해주는 것은 무의미함 -> 제곱해서 양수로 만들어준 후 평균을 구함



### Cost function

![image-20200908230212172](images/image-20200908230212172.png)

* W : weight
* b : bias



### Goal : Minimize cost

![image-20200908230319471](images/image-20200908230319471.png)

* cost가 최소가 되는 W와 b를 찾는 것이 학습의 목표



### Build hypothesis and cost

#### Hypothesis

![image-20200908230812366](images/image-20200908230812366.png)

```python
x_data = [1, 2, 3, 4, 5]
y_data = [1, 2, 3, 4, 5]

W = tf.Variable(2.9)  # 보통 랜덤값으로 초기화함
b = tf.Variable(0.5)  # 보통 랜덤값으로 초기화함

# hypothesis = W * x + b
hypothesis = W * x_data + b
```

*  W = 1, b = 0으로 수렴할 것으로 예상



#### Cost

![image-20200908230949494](images/image-20200908230949494.png)

```python
cost = tf.reduce_mean(tf.square(hypothesis - y_data))
```

* tf.reduce_mean()

  ```python
  v = [1., 2., 3., 4.]  # rank = 1
  tf.reduce_mean(v)  # 2.5  # rank = 0
  ```

  * 차원(rank)이 하나 줄어들면서 평균을 구함 

* tf.square()

  ```python
  tf.square(3)  # 9
  ```

  * 값을 제곱함



### Gradient descent (경사하강법)

* 경사를 하강시키면서 cost를 minimize하는 W와 b를 찾는 알고리즘

```python
# learning_rate initialize
learning_rate = 0.01  # 각각의 grad값을 어느 정도 반영할지를 결정
					  # 주로 굉장히 작은 값을 사용함

# Gradient descent
with tf.GradientTape() as tape:  # 이 블럭 안에서 변하는 변수들의 정보를 tape에 기록
    hypothesis = W * x_data + b
    cost = tf.reduce_mean(tf.square(hypothesis - y_data))
    
W_grad, b_grad = tape.gradient(cost, [W, b])  # 각각의 변수에 대한 미분값(기울기값)을 순서대로 tuple로 반환

W.assign_sub(learning_rate * W_grad)  # W를 update
b.assign_sub(learning_rate * b_grad)  # b를 update
```

```python
A.assign_sub(B)

A = A - B
A -= B
```



### Parameter(W, b) Update

```python
W = tf.Variable(2.9)
b = tf.Variable(0.5)

for i in range(100):
    # Gradient descent
    with tf.GradientTape() as tape:
        hypothesis = W * x_data + b
        cost = tf.reduce_mean(tf.square(hypothesis - y_data))
    W_grad, b_grad = tape.gradient(cost, [W, b])
    W.assign_sub(learning_rate * W_grad)
    b.assign_sub(learning_rate * b_grad)
    if i % 10 == 0:
        print("{:5}|{:10.4}|{:10.4}|{:10.6f}".format(i, W.numpy(), b.numpy(), cost)
```



### Full Code

```python
import tensorflow as tf
tf.enable_eager_execution()

# Data
x_data = [1, 2, 3, 4, 5]
y_data = [1, 2, 3, 4, 5]

# W, b initialize
W = tf.Variable(2.9)
b = tf.Variable(0.5)

# learning_rate initialize
learning_rate = 0.01

for i in range(100):  # W, b update
    # Gradient descent
    with tf.GradientTape() as tape:
        hypothesis = W * x_data + b
        cost = tf.reduce_mean(tf.square(hypothesis - y_data))
    W_grad, b_grad = tape.gradient(cost, [W, b])
    W.assign_sub(learning_rate * W_grad)
    b.assign_sub(learning_rate * b_grad)
    if i % 10 == 0:
        print("{:5}|{:10.4}|{:10.4}|{:10.6f}".format(i, W.numpy(), b.numpy(), cost)
```

![image-20200908232633564](images/image-20200908232633564.png)

* W = 1, b = 0으로 수렴함 (예상과 일치하는 결과)
* cost가 급속히 줄어 거의 0에 가까운 값이 됨 -> 우리 모델이 실제 데이터와 거의 동일함을 의미

![image-20200908232947003](images/image-20200908232947003.png)

* Epoch : update 횟수

![image-20200908233050285](images/image-20200908233050285.png)

* 새로운 데이터로 예측
  * 5를 넣었더니 5에 가까운 값이, 2.5를 넣었더니 2.5에 가까운 값이 나옴 -> 우리 모델의 예측이 잘 맞음