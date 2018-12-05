# Adding knowledge to the network



### Step 1: Collect description text



- Wikipedia: https://vi.wikipedia.org/wiki/%C4%90%E1%BA%A1i_h%E1%BB%8Dc_Qu%E1%BB%91c_gia_H%C3%A0_N%E1%BB%99i
- https://vi.wikipedia.org/wiki/Tr%C6%B0%E1%BB%9Dng_%C4%90%E1%BA%A1i_h%E1%BB%8Dc_C%C3%B4ng_ngh%E1%BB%87,_%C4%90%E1%BA%A1i_h%E1%BB%8Dc_Qu%E1%BB%91c_gia_H%C3%A0_N%E1%BB%99i
- Trang web của trường: https://uet.vnu.edu.vn/ (phần giới thiệu, lịch sử...)
- https://vnu.edu.vn/home/ (phần giới thiệu...)

### Step 2: Chunking text into sentences (named {K})

- Text to sentences: 
  - Simple "." or ???
  - 

### Step 3: Calculating similarity between each $k \in K$ and question $q \in Q$ to select 'context candidate sentences' (most correlated 5 $k$)

- Sentence similarity: Cosine distance (most basic)
- 

### Step 4: Feed 5 candidates as 'story' input together with the Q-A tuple to the model

- Reference code: [https://github.com/sujitpal/dl-models-for-qa](https://github.com/sujitpal/dl-models-for-qa?fbclid=IwAR2AqeUJ-GFafxFT2dRYu1q2xGoWeoRQC2zaXdAJ71CTuZeygaSymRvXcSc)