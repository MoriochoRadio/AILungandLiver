# models/

L-POT (간·폐 CT 결절 탐지) 시스템의 모델·가중치·SpiralConv 인덱스.

## 파일 목록

| 파일 | 크기 | 장기 | 용도 | 저장 방식 |
|---|---|---|---|---|
| `spiralnet.py` | 7 KB | 공통 | `SpiralConv` + `ImprovedSpiralNet` + `HybridSpiralNetPointNetTransformer` 구현 | git 일반 |
| `model_loader.py` | 5 KB | 공통 | 폐·간 모델 + spiral 인덱스 로드 | git 일반 |
| `model_manager.py` | 8 KB | 공통 | organ 별 추론 매니저 (`predict_for_organ`) | git 일반 |
| `__init__.py` | 148 B | — | `ImprovedSpiralNet`, `HybridSpiralNetPointNetTransformer` 노출 | git 일반 |
| **`new_2.pth`** | **54 MB** | **폐 (lung)** | 폐 결절 탐지 모델 가중치 | **Git LFS** |
| **`mask_merged_ver4.pth`** | **54 MB** | **간 (liver)** | 간 결절 탐지 모델 가중치 | **Git LFS** |
| `spiral_9.npy` | 96 KB | 공통 | SpiralConv 의 vertex spiral 이웃 인덱스 (.gitignore 예외) | git 일반 |

## 모델 아키텍처

```
HybridSpiralNetPointNetTransformer
├── ImprovedSpiralNet (encoder-decoder + SE block + spiral conv)
└── PointNet branch (MLP + Transformer attention)
```

- 입력: `(N_vertices, 7)` per-vertex features (xyz + normal + curvature 등)
- 출력: `(N_vertices,)` 결절(1) / 정상(0) 시그모이드 확률
- 폐/간 모델은 **동일 아키텍처, 다른 가중치**

## 파일명에 대하여

- `new_2.pth`: 두 번째 학습 버전 (학기 중 ver_1 → ver_2)
- `mask_merged_ver4.pth`: 마스크 병합 4번째 버전
- 학부 학습 시행착오 흔적으로 정식 명명 (`lung_v1.0.0.pth`) 없이 보존했습니다.

## 데이터셋 / 학습 정책

- 학습은 공개 의료 영상 데이터셋 (TCIA 계열 추정) 기반
- **학습 데이터 (.dcm, .nii) 는 본 레포에 포함되지 않음** (의료 영상 데이터 정책)
- 가중치는 ★ Team T.O.P 의 학기 산출물이며, 임상 사용 금지

## 사용 예시

```python
from pathlib import Path
from models.model_loader import ModelLoader
from models.model_manager import ModelManager

loader = ModelLoader(base_path=Path('.'))
loaded = loader.load()      # 폐 + 간 모델 동시 로드
manager = ModelManager(loaded)

# 폐 결절 예측
preds, probs = manager.predict_for_organ('lung', features, return_probabilities=True)

# 간 결절 예측
preds, probs = manager.predict_for_organ('liver', features, return_probabilities=True)
```
