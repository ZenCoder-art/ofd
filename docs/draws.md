# 基于模型融合的在线招聘欺诈检测

## 技术路线图

```mermaid
graph TB;
    A[基于多模型融合的在线招聘欺诈检测] --> B[数据收集];
    B --> C1[第一份英文公开数据集];
    B --> C2[第二份英文公开数据集]
    C1 --> D[数据合并与预处理]
    C2 --> D[数据合并与预处理]
    D --> E1[重复值处理]
    D --> E2[缺失值处理]
    D --> E3[异常值处理]
    D --> E4[特征提取:语义特征]
    E1 --> F[构建基础分类模型]
    E2 --> F
    E3 --> F
    E4 --> F
    F --> G1[逻辑回归模型]
    F --> G2[决策树模型]
    F --> G3[随机森林模型]
    F --> G4[支持向量机模型]
    F --> G5[神经网络模型];
    G1 --> H1[参数设置与训练]
    H1 --> J1[模型评估]
    G2 --> H2[参数设置与训练]
    H2 --> J2[模型评估]
    G3 --> H3[参数设置与训练]
    H3 --> J3[模型评估]
    G4 --> H4[参数设置与训练]
    H4 --> J4[模型评估]
    G5 --> H5[参数设置与训练]
    H5 --> J5[模型评估]
    J1 --> K[模型融合]
    J2 --> K
    J3 --> K
    J4 --> K
    J5 --> K
    K --> L1[投票法]
    K --> L2[均值法]
    K --> L3[Stacking]
    K --> L4[Blending]
    L1 --> M1[硬投票法]
    L1 --> M2[绝对多数投票法]
    L2 --> M3[普通均值法（软投票法）]
    L2 --> M4[加权平均法]
    L3 --> M5[一般Stacking过程]
    L3 --> M6[元学习器优化]
    L4 --> M7[一般Blending过程]
    L4 --> M8[Blending与平均法双层融合]
    M1 --> N[模型评估与检验]
    M2 --> N
    M3 --> N
    M4 --> N
    M5 --> N
    M6 --> N
    M7 --> N
    M8 --> N
    N --> O[模型部署与应用]
    B --> C3[中文数据集]
    C3 --> D1[数据预处理]
    D1 --> E5[检验训练好的融合模型]
```

```mermaid
graph TB
    A[基于模型融合的在线招聘欺诈检测]-->|数据收集|B[第一份英文数据集];
    A-->|数据收集|C[第二份英文数据集];
    A-->|数据收集|D[中文招聘欺诈数据集];
    B-->E[数据合并与预处理]
    C-->E
    D-->E
    E-->F[特征工程]
    F-->G[决策树模型]
    F-->H[随机森林模型]
    F-->I[逻辑回归模型]
    G-->J{模型融合}
    H-->J
    I-->J
    subgraph 模型融合
        J-->K[投票法]
        J-->L[均值法]
        J-->M[Stacking法]
        J-->N[Blending法]
        J-->O[级联优化与特征增强]
        end
```

## Bagging 算法流程图

```mermaid
graph TB;
    A((原始训练集))-->|有放回的抽样|B[采样集1]
    A-->|有放回的抽样|C[采样集2]
    A-->|有放回的抽样|D[...]
    A-->|有放回的抽样|E[采样集n]
    B-->|训练|F[模型1]
    C-->|训练|G[模型2]
    D-->|训练|H[...]
    E-->|训练|I[模型n]
    F-->|预测|J(预测集1)
    G-->|预测|K(预测集2)
    H-->|预测|L(...)
    I-->|预测|M(预测集n)
    J-->|投票|N{决策}
    K-->|投票|N
    L-->|投票|N
    M-->|投票|N
```

## Boosting 算法流程图

```mermaid
graph LR;
    A((原始训练集))-->|训练|B[弱分类器1]
    A-->|转化|C[训练集1]
    C-->|训练|D[弱分类器2]
    C-->|转化|E[训练集2]
    E-->|训练|F[...]
    E-->|转化|G[...]
    B-->|预测|H[综合预测结果]
    D-->|预测|H
    F-->|预测|H
```

## Stacking 模型融合算法流程图

```mermaid
graph LR;
    A[一组一级学习器]-->|在训练集上进行预测|B[元学习器的训练集]
    A-->C[测试集]
    B-->|训练|D[元学习器]
    C-->|测试|D
    D-->E[预测结果]
```

## Blending 模型融合算法流程图

```mermaid
graph LR
    %% 主流程
    subgraph 训练阶段
        A[原始训练集]:::data
        -->|随机拆分| B[训练子集50%-90%]:::data
        A -->|留出| C[留出验证集10%-50%]:::data

        B --> D[一级学习器训练]:::model
        D --> E[生成验证预测]:::result
    end

    subgraph 元学习阶段
        C & E --> F[元特征矩阵]
        F --> G[元学习器训练]:::meta
    end

    subgraph 预测阶段
        H[测试集]:::data --> I[一级学习器预测]:::model
        I --> J[测试预测结果]:::result
        G --> K[元学习器集成预测]:::meta
        J --> K
        K --> L[最终预测结果]:::result
    end
```

## 异常值处理算法流程

```mermaid
graph TB
    A[原始数据集]-->B[数值型变量异常处理];
    A-->C[文本型变量异常处理]
    subgraph 文本型变量
        C-->D[噪声剥离层]
        C-->E[形态归一化]
    end
    subgraph 数值型变量
        B-->F[格式有效性检测]
        B-->G[非数字字符记录处理]
    end
```

## 决策树示例图

```mermaid
graph TB
A{属性a}-->|Yes|B{属性b}
A-->|No|C[结果a]
B-->|Yes|D{属性c}
B-->|No|E[结果b]
D-->|Yes|F[结果c]
D-->|No|G[结果d]
```

## ColumnTransformer 示例图

```mermaid
graph TB
A[原始数据集]-->B[text字段]
A-->C[有序分类型变量]
A-->D[其余分类型变量]
A-->S[数值型变量]
B-->F[TFIDF向量化]
C-->G[OridinalEncoder]
D-->K[OneHotEncoder]
S-->I[MinMaxScaler]
F-->J[ColumnTransformer]
G-->J
K-->J
I-->J
```

## 模型融合框架图

```mermaid
graph LR
A[原始数据]-->B[特征工程]
subgraph 数据输入层
    B-->C[OntHotEncoder]
    B-->D[OridinalEncoder]
    B-->E[TargetEncoder]
    B-->F[StandardScaler]
    B-->G[TFIDFVectorizer]
    end
subgraph 模型集成层
    C-->H[模型集成]
    D-->H
    E-->H
    F-->H
    G-->H
    H-->I[决策树模型]
    H-->J[逻辑回归模型]
    H-->K[随机森林模型]
    end
subgraph 融合策略层
    I-->L[模型融合]
    J-->L
    K-->L
    L-->M[均值法]
    L-->N[投票法]
    L-->O[Stacking法]
    L-->P[Blending法]
    end
```

## 数据预处理流程图

```mermaid
graph LR
A[原始数据集]-->B[fake-job-postings]
A-->C[FakePostings]
A-->D[中文招聘欺诈数据集]
B-->E[删除无关字段]
C-->CC[不做任何处理]
D-->F[删除无关字段和字段重命名]
E-->G[数据合并]
CC-->G[数据合并]
F-->G[数据合并]
```

## 重复值

```mermaid
pie
    title 数据集重复值分布
    "重复值" : 293
    "唯一值" : 28455
```

## 缺失值处理流程

```mermaid
graph LR
A[原始数据集]-->B[分类型变量]
A-->C[文本型变量]
A-->D[二元型变量]
A-->E[离散型变量]
B-->F[location变量]
B-->G[其他分类型变量]
F-->H[删除缺失值]
G-->I[填充为Missing]
D-->J[填充为-1]
C-->K[description变量]
C-->L[其他文本型变量]
K-->M[删除缺失值]
L-->N[填充为Missing]
E-->O[填充为0-0]
```

## 模型权重占比图

```mermaid
pie
    title 模型权重占比分布图
    "DecisionTree": 1
    "LogisticRegression": 1
    "RandomForest": 100
```

```mermaid
graph TB
A[模型1]-->r1[预测结果1]
B[模型2]-->r2[预测结果2]
C[模型3]-->r3[预测结果3]
r1-->D{加权平均融合}
r2-->D
r3-->D
D-->|大于阈值|E[正类]
D-->|小于阈值|F[负类]
```

```mermaid
graph TB
A[模型1]-->r1[预测结果1]
B[模型2]-->r2[预测结果2]
C[模型3]-->r3[预测结果3]
r1-->D{机器学习模型预测}
r2-->D
r3-->D
D-->|大于阈值|E[正类]
D-->|小于阈值|F[负类]
```

```mermaid
graph TB
A[决策树模型]-->r1[一级元学习器]
B[逻辑回归模型]-->r1[一级元学习器]
C[随机森林模型]-->r1[一级元学习器]
r1-->D[逻辑回归模型]
r1-->E[随机森林模型]
D-->r2[二级学习器]
E-->r2[二级学习器]
```

```mermaid
pie
    title 数据标签占比
    "欺诈": 11270
    "非欺诈": 16843
```

```mermaid
graph TD
A[数据]-->b1[逻辑回归模型]
A-->b2[决策树模型]
A-->b3[随机森林模型]
b1-->c1[预测结果1]
b2-->c2[预测结果2]
b3-->c3[预测结果3]
c1-->r[投票得出最终预测结果]
c2-->r
c3-->r
```

```mermaid
graph LR
A[数据]-->b1[逻辑回归模型]
A-->b2[决策树模型]
A-->b3[随机森林模型]
b1-->c1[预测结果1]
b2-->c2[预测结果2]
b3-->c3[预测结果3]
c1-->r[加权平均得出最终预测结果]
c2-->r
c3-->r
```

```mermaid
graph TB
    start((开始))
    start --> 单层
    start --> 双层
    subgraph 单层[单层Stacking模型]
        A[数据]-->b1[逻辑回归模型]
        A-->b2[决策树模型]
        A-->b3[随机森林模型]
        b1-->c1[预测结果1]
        b2-->c2[预测结果2]
        b3-->c3[预测结果3]
        c1-->r[汇总预测结果]
        c2-->r
        c3-->r
        r-->d[元学习器]
        d-->e[最终预测结果]
    end
    subgraph 双层[双层Stacking模型]
        AA[数据]-->bb1[逻辑回归模型]
        AA-->bb2[决策树模型]
        AA-->bb3[随机森林模型]
        bb1-->cc1[预测结果1]
        bb2-->cc2[预测结果2]
        bb3-->cc3[预测结果3]
        cc1-->rr[汇总预测结果]
        cc2-->rr
        cc3-->rr
        rr-->dd1[决策树模型]
        rr-->dd2[随机森林模型]
        dd1-->ee1[预测结果1]
        dd2-->ee2[预测结果2]
        ee1-->ee3[汇总预测结果]
        ee2-->ee3
        ee3-->ff[二级元学习器]
        ff-->gg[最终预测结果]
    end
```
