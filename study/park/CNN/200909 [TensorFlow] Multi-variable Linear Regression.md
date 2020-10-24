# Multi-variable Linear Regression

![image-20200909125925707](images/image-20200909125925707.png)

![image-20200909125943659](images/image-20200909125943659.png)

* 다양한 변수를 갖고 예측하면 더 잘 예측할 수 있음 (prediction power)



### Hypothesis

![image-20200909130112669](images/image-20200909130112669.png)

* 변수의 개수 = 가중치의 개수



### Cost function

![image-20200909130154438](images/image-20200909130154438.png)



### Multi-variable

![image-20200909130236851](images/image-20200909130236851.png)

* 변수의 개수가 많아지면 이런 식으로 표현하기 힘듦 -> Matrix를 활용!



### Matrix

#### Hypothesis using matrix

![image-20200909130415730](images/image-20200909130415730.png)

* 매우 간편하게 표현할 수 있음 (변수와 가중치를 일일이 기술할 필요 X)

![image-20200909130733775](images/image-20200909130733775.png)

![image-20200909130906044](images/image-20200909130906044.png)

* 데이터의 개수에 상관없이 동일하게 표현할 수 있음

![image-20200909131026107](images/image-20200909131026107.png)

* 행렬 연산의 특징에 의해 입력 데이터의 column 개수와 출력 데이터의 column 개수로 가중치 행렬의 크기를 알 수 있음



### Hypothesis using matrix

#### Without matrix

![image-20200909131312290](images/image-20200909131312290.png)

![image-20200909132439307](images/image-20200909132439307.png)

```python
# data and label
x1 = [73., 93., 89., 96., 73.]
x2 = [80., 88., 91., 98., 66.]
x3 = [75., 93., 90., 100., 70.]
Y = [152., 185., 180., 196., 142.]

# weights
w1 = tf.Variable(10.)
w2 = tf.Variable(10.)
w3 = tf.Variable(10.)
b = tf.Variable(10.)

hypothesis = w1 * x1 + w2 * x2 + w3 * x3 + b
```

```python
# data and label
x1 = [73., 93., 89., 96., 73.]
x2 = [80., 88., 91., 98., 66.]
x3 = [75., 93., 90., 100., 70.]
Y = [152., 185., 180., 196., 142.]

# random weights
w1 = tf.Variable(tf.random_normal([1]))
w2 = tf.Variable(tf.random_normal([1]))
w3 = tf.Variable(tf.random_normal([1]))
b = tf.Variable(tf.random_normal([1]))

learning_rate = 0.000001

for i in range(1000+1):
    # tf.GradientTape() to record the gradient of the cost function
    with tf.GradientTape() as tape:
        hypothesis = w1 * x1 + w2 * x2 + w3 * x3 + b
        cost = tf.reduce_mean(tf.square(hypothesis - Y))
    # calculates the gradients of the cost
    w1_grad, w2_grad, w3_grad, b_grad = tape.gradient(cost, [w1, w2, w3, b])
    
    # update w1, w2, w3 and b
    w1.assign_sub(learning_rate * w1_grad)
    w2.assign_sub(learning_rate * w2_grad)
    w3.assign_sub(learning_rate * w3_grad)
    b.assign_sub(learning_rate * b_grad)
    
    if i % 50 == 0:
        print('{:5} | {:12.4f}'.format(i, cost.numpy()))
```

![image-20200909133143719](images/image-20200909133143719.png)



#### With matrix

![image-20200909131312290](images/image-20200909131312290.png)

![image-20200909133348477](images/image-20200909133348477.png)

```python
data = np.array([  # data가 한꺼번에 준비됨
    # X1,  X2,  X3,   y
    [ 73., 80., 75., 152. ],
    [ 93., 88., 93., 185. ],
    [ 89., 91., 90., 180. ],
    [ 73., 66., 70., 142. ]
], dtype=np.float32)

# slice data
X = data[:, :-1]  # 모든 행, 마지막 열을 제외한 열
y = data[:, [-1]]  # 모든 행, 마지막 열

W = tf.Variable(tf.random_normal([3, 1]))  # 입력 데이터의 column 개수(변수의 개수)가 3개, 출력 데이터의 column 개수가 1개 -> 가중치 행렬의 크기가 결정됨
b = tf.Variable(tf.random_normal([1]))

# hypothesis, prediction function
def predict(X):
    return tf.matmul(X, W) + b
```

![image-20200909134446582](images/image-20200909134446582.png)



### Full Code

```python
data = np.array([
    # X1,  X2,  X3,   y
    [ 73., 80., 75., 152. ],
    [ 93., 88., 93., 185. ],
    [ 89., 91., 90., 180. ],
    [ 73., 66., 70., 142. ]
], dtype=np.float32)

# slice data
X = data[:, :-1]
y = data[:, [-1]]

W = tf.Variable(tf.random_normal([3, 1]))
b = tf.Variable(tf.random_normal([1]))

learning_rate = 0.000001

# hypothesis, prediction function
def predict(X):
    return tf.matmul(X, W) + b

n_epochs = 2000
for i in range(n_epochs+1):
    # record the gradient of the cost function
    with tf.GradientTape() as tape:
        cost = tf.reduce_mean((tf.square(predict(X) - y)))
    
    # calculates the gradients of the loss
    W_grad, b_grad = tape.gradient(cost, [W, b])
    
    # updates parameters (W and b)
    W.assign_sub(learning_rate * W_grad)
    b.assign_sub(learning_rate * b_grad)
    
    if i % 100 == 0:
        print('{:5} | {:10.4f}'.format(i, cost.numpy()))
```

![image-20200909134347367](images/image-20200909134347367.png)