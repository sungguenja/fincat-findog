# Linear Regression and How to minimize cost

## Linear Regression

![image-20200909120719078](images/image-20200909120719078.png)

![image-20200909120828822](images/image-20200909120828822.png)

* 계산을 간단하게 하기 위해 b를 생략 -> W가 matrix라 b가 W 속에 포함됨

![image-20200909121909696](images/image-20200909121909696.png)

![image-20200909121941322](images/image-20200909121941322.png)

![image-20200909122019265](images/image-20200909122019265.png)



## How to minimize cost?

![image-20200909122110502](images/image-20200909122110502.png)

### Gradient descent algorithm

![image-20200909122212197](images/image-20200909122212197.png)

![image-20200909122238075](images/image-20200909122238075.png)

![image-20200909122449744](images/image-20200909122449744.png)

* 경사를 따라 하강하면서 cost가 최소가 되는 지점을 찾음 (더는 기울기가 변하지 않는 점 = 최저점)
* 경사가 급할 수록 더 많이 이동함
* Gradient -> 미분을 통해 구함

![image-20200909122652230](images/image-20200909122652230.png)

* 계산을 간단하게 하기 위해 m 대신 2m으로 나눠줌 -> cost의 특성에는 아무런 영향이 없음

![image-20200909122802025](images/image-20200909122802025.png)

* W값을 계속해서 업데이트함
* alpha : learning rate (학습률) -> W가 얼마나 빠르게, 많이 업데이트 될지를 결정 -> 이 값을 잘 지정하는 것도 중요한 숙제 중 하나

![image-20200909122925330](images/image-20200909122925330.png)

![image-20200909123134204](images/image-20200909123134204.png)

![image-20200909123246690](images/image-20200909123246690.png)

* Gradient algorithm : 주변의 경사를 따라 점점 낮은 곳으로 가서 최저점을 찾는 알고리즘
  * 시작점을 어디로 잡냐에 따라 전체의 최저점(global minimum)을 찾지 못할 수도 있음
  * 주위에서 가장 낮은 지점 (기울기가 0이 되는 지점) : local minimum 
  * local minimum이 여러 개가 존재할 때 global minimum으로 도달한다는 것을 보장할 수 없음 -> 이런 상황에서는 Gradient algorithm을 사용할 수 없음

![image-20200909123808550](images/image-20200909123808550.png)

* 위와 같이 볼록한 함수 : Convex function
* local minimum이 1개라 local minimum과 global minimum이 일치하는 경우
* 어디에서 시작하든지 항상 global minimum에 도달하는 것을 보장할 수 있음 -> 마음 놓고 Gradient algorithm을 사용할 수있음



### Cost function in pure Python

![image-20200909124326619](images/image-20200909124326619.png)

```python
import numpy as np

X = np.array([1, 2, 3])
Y = np.array([1, 2, 3])

def cost_func(W, X, Y):
    c = 0
    for i in range(len(x)):
        c += (W * X[i] - Y[i]) ** 2
    return c / len(X)

for feed_W in np.linspace(-3, 5, num=15):  # -3에서 5까지 15개의 구간으로 쪼갬
    curr_cost = cost_func(feed_W, X, Y)
    print('{:6.3f} | {:10.5f}'.format(feed_W, curr_cost))
```

![image-20200909124347262](images/image-20200909124347262.png)

![image-20200909124454415](images/image-20200909124454415.png)



### Cost function in TensorFlow

```python
X = np.array([1, 2, 3])
Y = np.array([1, 2, 3])

def cost_func(W, X, Y):
    hypothesis = X * W
    return tf.reduce_mean(tf.square(hypothesis - Y))

W_values = np.linspace(-3, 5, num=15)
cost_values = []

for feed_W in W_values:
    curr_cost = cost_func(feed_W, X, Y)
    cost_values.append(curr_cost)
    print('{:6.3f} | {:10.5f}'.format(feed_W, curr_cost))
```



### Gradient descent

![image-20200909124652974](images/image-20200909124652974.png)

```python
alpha = 0.01
gradient = tf.reduce_mean(tf.multiply(tf.multiply(W, X) - Y, X))
descent = W - tf.multiply(alpha, gradient)  # 새로운 W값
W.assign(descent)
```



### Full Code

```python
tf.set_random_seed(0)  # for reproducibility -> random seed 초기화해서 재현할 수 있게 함

x_data = [1., 2., 3., 4.]
y_data = [1., 3., 5., 7.]

W = tf.Variable(tf.random_normal([1], -100., 100.))  # 정규분포를 따르는 random number 1개로 변수를 만듦
# random number 대신 W = tf.Variable([5.0])처럼 특정한 값을 넣어줘도 결과는 같음 (초기의 cost와 W는 아주 다르더라도 cost는 0으로, W는 특정한 값으로 수렴함)

for step in range(300):
    hypothesis = W * X
    cost = tf.reduce_mean(tf.square(hypothesis - Y))
    
    # Gradient descent
    alpha = 0.01
    gradient = tf.reduce_mean(tf.multiply(tf.multiply(W, X) - Y, X))
	descent = W - tf.multiply(alpha, gradient)  # 새로운 W값
	W.assign(descent)
    
    if step % 10 == 0:
        print('{:5} | {:10.4f} | {:10.6f}'.format(step, cost.numpy(), W.numpy()[0]))
```

![image-20200909125328453](images/image-20200909125328453.png)

