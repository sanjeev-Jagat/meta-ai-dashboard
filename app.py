import streamlit as st
import pandas as pd
import numpy as np
import cv2
from PIL import Image
from sklearn.ensemble import RandomForestRegressor

st.title("🔥 Meta Ads AI Dashboard ULTRA PRO")

# ======================
# TEXT ANALYSIS
# ======================
st.subheader("🧠 Text Creative Analysis")

headline = st.text_input("Enter Headline")
text = st.text_input("Enter Ad Text")

if st.button("Analyze Text"):

    score = 0

    if "free" in headline.lower():
        score += 2
    if "7" in headline:
        score += 2
    if "doctor" in text.lower():
        score += 2
    if len(headline) > 25:
        score += 1

    st.success(f"🔥 Creative Score: {score}/7")

    if score >= 5:
        st.success("🚀 High Performing Ad")
    else:
        st.warning("⚠️ Needs Improvement")

# ======================
# IMAGE ANALYSIS
# ======================
st.subheader("🖼 Image Analysis")

img_file = st.file_uploader("Upload Ad Image", type=["jpg","png"])

if img_file:
    image = Image.open(img_file)
    st.image(image)

    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    brightness = np.mean(gray)

    st.write(f"Brightness Score: {round(brightness,2)}")

    if brightness > 120:
        st.success("✅ Bright image (good for ads)")
    else:
        st.warning("⚠️ Dark image (low performance)")

# ======================
# VIDEO ANALYSIS (BASIC)
# ======================
st.subheader("🎥 Video Analysis")

video_file = st.file_uploader("Upload Video", type=["mp4"])

if video_file:
    st.video(video_file)

    st.success("✅ Video uploaded")

    st.write("👉 Tip: First 3 sec me strong hook hona chahiye")

# ======================
# SIMPLE AI MODEL
# ======================
st.subheader("📊 ROAS Prediction")

data = pd.DataFrame({
    "hl_len":[20,25,30],
    "txt_len":[15,18,20],
    "roas":[2.5,3.2,4.0]
})

X = data[["hl_len","txt_len"]]
y = data["roas"]

model = RandomForestRegressor()
model.fit(X,y)

if st.button("Predict ROAS"):

    hl = len(headline)
    tl = len(text)

    pred = model.predict([[hl,tl]])
    st.success(f"💰 Expected ROAS: {round(pred[0],2)}")