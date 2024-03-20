# 2024 Spring
## Algorithm Class


## 2024 03 06

// Chapter 1.1~1.4

// Chapter 2.1~2.2 (Till Mergesort)


## 2024 03 13

// Chapter 2.2 ~ 2.8

// Quick Sort
```
void quicksort(index low, index high){
    index pivotpoint;
    if(high > low){
        partition(low, high, pivotpoint);
        quicksort(low, pivotpoint - 1);
        quicksort(pivotpoint + 1, high);
    }
}

void partition(index low, index high, index& pivotpoint){
    index i, j;
    keytype pivotitem;

    pivotitem = S[low];
    j = low;
    for(i = low + 1; i<=high; i++){
        if(S[i]<pivotitem){
            j++;
            S[i] and S[j] exchange;
        }
    }
    pivotpoint = j;
    S[low] and S[pivotpoint] exchange;
}
```
//Large Int Computation
```
large_integer prod(large_integer u, large_integer v){
    large_integer x, y, w, z;
    int n, m;
    n = max(length(n), length(v));
    if(u == 0 || v == 0){
        return 0;
    }
    else if(n <= threshold)
        return u * v;
    else{
        m = [n/2];
        x = u divide 10^m;
        y = u rem 10^m;
        w = v divide 10^m;
        z = v rem 10^m;
        return prod(x, w) * 10^2m + (prod(x, z) + prod(w, y)) * 10^m + prod(y, z);  
    }
}
```
// Chapter 3 is really crucial
// Chapter 3.1 ~

C n取k -> 二項式係數
Divide and conquer版本
```
int bin(int n, int k){
    if(k == 0 || n == k){
        return 1;
    }
    else
        return bin(n-1, k-1) + bin(n-1, k)
}
```
DP 版本
```
int binCoeff(int n, int k){
    index i, j;
    int B[0..n][0..k];
    for(i =0; i<=n; i++){
        for(j = 0; j <= min(i, k); j++){
            if(j == 0||j==i){
                B[i][j] = 1;
            }
            else{
                B[i][j] = B[i-1][j-1] + B[i-1][j];
            }
        }
    }
    return B[n][k];
}
```

## 2024 03 20

// Chapter 3.2~3.3
討論Floyd最短路徑演算法和為甚麼不找最遠路徑(因為會無限循環)

// Chapter 3.2(小考考一次這個)
Floyd Warshall Algo 1
```
void floyd(int n, const number W[][], number D[][]){
    index i, j, k;
    D = W;
    for(k = 1; k <= n; k++){
        for(i = 1; i <= n; i++){
            for(j = 1; j <= n; j++){
                D[i][j] = minimum(D[i][j], D[i][k] + D[k][j]);
            }
        }
    }
}
```
Floyd Warshall Algo 2
```
void floydAdv(int n, const number W[][], number D[][], index P[][]){
    index i, j, k;
    for(i = 1; i <= n; i++){
        for(j = 1; j <= n; j++){
            P[i][j] = 0;
        }
    }
    D = W;
    for(k = 1; k <= n; k++){
        for(i = 1; i <= n; i++){
            for(j = 1; j <= n; j++){
                if(D[i][k] + D[k][j] < D[i][j]){
                    P[i][j] = k;
                    D[i][j] = D[i][k] + D[k][j];
                }
            }
        }
    }
}
void path(index q, r){
    if(P[q][r] != 0){
        path(q, P[q][r]);
        cout << "v" << P[q][r];
        path(P[q][r], r);
    }
}
```
