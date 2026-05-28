# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_submodules, collect_all

ROOT = os.getcwd()

# utils 및 torch 관련 숨겨진 모듈 수집
hidden_utils = collect_submodules('utils')
torch_datas, torch_binaries, torch_hidden = collect_all('torch')

# 데이터 폴더 (liver/lung 각각)
my_datas = [
    # 모델 파일
    (os.path.join(ROOT, 'models', 'new_2.pth'), 'models'),
    (os.path.join(ROOT, 'models', 'mask_merged_ver4.pth'), 'models'),
    (os.path.join(ROOT, 'models', 'spiral_9.npy'), 'models'),

    # 데이터 폴더
    (os.path.join(ROOT, 'datas', 'liver', 'features'), 'datas/liver/features'),
    (os.path.join(ROOT, 'datas', 'liver', 'labels'), 'datas/liver/labels'),
    (os.path.join(ROOT, 'datas', 'lung', 'features'), 'datas/lung/features'),
    (os.path.join(ROOT, 'datas', 'lung', 'labels'), 'datas/lung/labels'),
]

a = Analysis(
    ['dashboard_main.py'],
    pathex=[ROOT],
    binaries=torch_binaries,
    datas=my_datas + torch_datas,
    hiddenimports=hidden_utils + torch_hidden,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='L-POT',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon="./LPOT.ico",  # 빌드 시 프로젝트 루트에 LPOT.ico 두기
    # 💡 완전 단일 실행파일 모드
    onefile=True,                     # ✅ exe 하나로 합치기
    onefile_tempdir=False,            # 실행시 임시폴더 안풀고 바로 실행
)
