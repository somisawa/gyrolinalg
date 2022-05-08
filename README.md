# gyrolinalg
NumPy-based gyrovector calculation library based on Poincare disk with Mobius gyrostructure.

## Usage

### 設定
次元やdiskの半径(1/C)を [gyrolinalg/constant.py](https://github.com/somisawa/gyrolinalg/blob/main/gyrolinalg/constant.py) で設定しよう

### ジャイロベクタの作成

```python
import gyrolinalg as gLA
from gyrolinalg import GyroVec

a = np.array([0.5, 0.5])
b = np.array([0.4, 0.1])
zero = GyroVec.zero()
v = GyroVec(a)
w = GyroVec(b)
```

### 例
非可換性の確認
```python
print(v + w)
# array([0.65299685, 0.55835962])

print(w + v)
# array([0.76656151, 0.38801262])
```

積
```python
print(2 * v)
# array([0.66666667, 0.66666667])

print(v + v)
# array([0.66666667, 0.66666667])
```

指数写像・対数写像
```python
print(gLA.exp(v, b))
# array([0.39886683, 0.06091112])

print(gLA.log(v, w))
# array([-0.13907259, -0.29359769])
```
※ なんかlog expを計算しても厳密に元と一致しない。実装ミス？数値的な話？
ただし，小さいCで計算するとEuclideanケースの指数・対数写像に一致するので実装間違ってないと思うんだよな。
