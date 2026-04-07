import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("🔥 Meta Ads AI Dashboard PRO")

# ======================
# INPUT SECTION
# ======================
headline = st.text_input("Enter Headline")
text = st.text_area("Enter Ad Text")

# ======================
# ML MODEL (ROAS)
# ======================
st.subheader("📊 ROAS Prediction")

data = pd.DataFrame({
    "hl_len": [22, 24, 24, 19, 24],
    "txt_len": [17, 18, 17, 12, 24],
    "roas": [2.5, 1.8, 4.2, 3.0, 3.5]
})

X = data[["hl_len", "txt_len"]]
y = data["roas"]

model = LinearRegression()
model.fit(X, y)

if st.button("Predict ROAS"):
    if headline and text:
        hl_len = len(headline)
        txt_len = len(text)

        pred = model.predict([[hl_len, txt_len]])[0]
        st.success(f"💰 Predicted ROAS: {round(pred,2)}")
    else:
        st.error("⚠️ Enter headline & text")

# ======================
# AD GENERATOR
# ======================
st.subheader("🤖 Generate Winning Ads")

if st.button("Generate Ads"):
    ideas = [
        f"{headline} in 7 days 🔥",
        f"Doctor recommended: {headline}",
        f"No surgery needed – {headline}",
        f"100% natural way: {headline}",
        f"Fix your problem: {headline}"
    ]

    for idea in ideas:
        st.write("👉", idea)

# ======================
# WHATSAPP AUTOMATION
# ======================
st.subheader("💬 Send Lead to WhatsApp")

phone = "91XXXXXXXXXX"  # apna number daalo

if headline and text:
    message = f"I want details:\n{headline}\n{text}"
    url = f"https://wa.me/{phone}?text={message}"
    st.markdown(f"[👉 Send to WhatsApp]({url})")
else:
    st.info("Enter details to enable WhatsApp button")
