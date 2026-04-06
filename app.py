# Vector26-Health import streamlit as st
import pandas as pd
import numpy as np
import time

# --- 頁面配置：iPhone 16 深度優化 ---
st.set_page_config(page_title="Vector 26: Health Link", layout="centered", initial_sidebar_state="collapsed")

# --- CSS：打造高科技醫療介面 ---
st.markdown("""
    <style>
    .main { background-color: #000000; color: #00FFCC; font-family: 'SF Pro Display', sans-serif; }
    .stButton>button { width: 100%; border-radius: 15px; height: 3.5rem; background: linear-gradient(45deg, #00BFA5, #004D40); color: white; border: none; font-weight: bold; font-size: 1.1rem; }
    .card { border: 1px solid #00FFCC; padding: 20px; border-radius: 15px; background: rgba(0, 255, 204, 0.05); margin-bottom: 15px; }
    h1, h2, h3 { color: #00FFCC; }
    </style>
    """, unsafe_allow_html=True)

# --- 側邊欄：硬體對接狀態 ---
with st.sidebar:
    st.header("📡 硬件鏈接矩陣")
    st.status("ExBody 鏡頭: 已連線", state="complete")
    st.status("InBody 傳感器: 已連線", state="complete")
    st.status("iPhone 16 LiDAR: 待命", state="running")

# --- 主畫面 ---
st.title("🛡️ VECTOR 26")
st.write("Overland Park 物理進化系統 | 第一輪試駕")

# --- 第一步：用戶分類 ---
st.markdown("### 🧬 受測者初始化")
age = st.slider("請選擇受測者年齡", 5, 90, 25)
if age <= 18:
    category = "GEN-ALPHA (發育引導)"
elif 19 <= age <= 45:
    category = "PEAK-VECTOR (效能強化)"
elif 46 <= age <= 64:
    category = "VITAL-RESET (結構維持)"
else:
    category = "SILVER-SHIELD (盾護防禦)"
st.info(f"當前模式：{category}")

# --- 第二步：3D 掃描入口 ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📸 多角度 3D 影像採集")
st.write("請站在 ExBody 鏡頭前，並手持 iPhone 16 進行側面校準。")

if st.button("啟動 OSIRIS-SYNC 同步掃描"):
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)
    st.success("✅ 多視角影像已融合。數位孿生模型已生成。")
    
    # 模擬 3D 應力矢量圖
    chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['脊椎力矩', '關節載荷'])
    st.area_chart(chart_data)
st.markdown('</div>', unsafe_allow_html=True)

# --- 第三步：三位一體方案輸出 ---
st.markdown("### 🏆 強化方案 (Prehab > Rehab)")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("🏥 **物理治療**")
    st.caption("脊椎減壓與矢量校正動作")

with col2:
    st.write("🏋️ **精確訓練**")
    st.caption("基於 InBody 的弱項肥大訓練")

with col3:
    st.write("🥗 **營養學**")
    st.caption("AlphaFold 蛋白合成建議")

if st.download_button("📩 下載數位康復護照 (PDF)", "DATA-LOG-26", file_name="V26_Passport.txt"):
    st.balloons()
