# 2024 Spring
## Algorithm Class
#複習

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


## 2024 03 27

// Chapter 3.4


// 3.4
討論複數矩陣在相乘的時候，計算量的差別
> ex: A(20 * 2) x B(2 * 30) x C(30 * 12) x D(12 * 8)
> 根據不同的順序，會得A((BC)D)為1232次，比((AB)C)D的10320次少很多

// Code(Time Complexity:O(n^3))
```
int minMult(int n, const int d[], index P[][]){
    index i, j, k, diagonal;
    int M[1..n][1..n];

    for(i=1;i<=n;i++){
        M[i][i] = 0;
    }
    for(diagonal = 1; diagonal <= n - 1; diagonal++){
        for(i = 1; i <= n - diagonal; i++){
            j = i + diagonal;
            M[i][j] = minimum(M[i][k] + M[k+1][j] + d[i-1]*d[k]*d[j]);
            P[i][j] = value k when reaching the minimum multiply times;
        }
    }
    return M[1][n];
}
```
```
void order(index i, index j){
    if(i==j){
        cout <<"A"<<i;
    }
    else{
        k = P[i][j];
        cout << "(";
        order(i, k);
        order(k+1, j);
        cout << ")";
    }
}
```

所以若是一個矩陣1~6
則順序會為:
```
12 23 34 45 56
   13 24 35 46
      14 25 36
         15 26
            16
```

## 2024 04 10

// 3.5

// 3.5 Optimal Binary Search Tree

TreeNode
```
struct nodetype{
    keytype key;
    nodetype* left;
    nodetype* right;
};

typedef nodetype* node pointer;
```
Normal Bin Search Tree
```
void search(node_pointer tree, keytype keyin, node_pointer& p){
    bool found;
    p = tree;
    found = false;
    while(!found){
        if(p->key == keyin){
            found = true;
        }
        else if(keyin < p-> key){
            p = p->left;
        }
        else{
            p = p->right;
        }
    }
}
```

Opt. Bin Search Tree
```
void optSearch(int n, const float p[], float& minavg, index R[][]){
    index i, j, k, diagonal;
    float A[1..n + 1][0..n];
    for(i = 1; i <= n; i++){
        A[i][i-1] = 0;
        A[i][i] = p[i];
        R[i][i] = i;
        R[i][i-1] = 0;
    }
    A[n+1][n]=0;
    R[n+1][n]=0;
    for(diagonal = 1; diagonal <= n-1; diagonal++){
        for(i = 1; i <= n-diagonal;i++){
            j=i+diagonal;
            A[i][j] = min(A[i][k-1] + A[k+1][j]) + summation(P_m,m from i to j);
            R[i][j] = k when reaching least time multiplying;
        }
        minavg = A[1][n];
    }
}
```
Construct Opt. Bin tree
```
node_pointer tree(index i, j){
    index k;
    node_pointer p;

    k = R[i][j];
    if(k == 0) return NULL;
    else{
        p = new nodetype;
        p->key = Key[k];
        p->left = tree(i, k-1);
        p->right = tree(k+1, j);
        return p;
    }
}
```

### 以上為期中以前

## 補充環節
# Huffman Coding

// Example
=> A,B,C,D,E,F,G,H
=> 22,5,11,19,2,11,25,5
using priority queue(優先佇列)

=> E, B, H, C, F, D, A, G
=> 2, 5, 5, 11, 11, 19, 22, 25 (the frequency that the digits pops out)
```
              100
             /   \1
           0/     56
           /    0/  \1
          /    25,G  31
        44         0/  \1
      0/  \1      12    19,D
     22   22,A  0/  \1
   0/  \1     5,H    7
 11,C  11,F        0/ \1
                 2,E   5,B
```



